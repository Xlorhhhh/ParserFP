from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import telebot

def read_product_link():
    try:
        with open('product_link.txt', 'r') as file:
            product_link = file.readline()
    except FileNotFoundError:
        print('Файл с ссылкой на товар не найден. Введите ссылку на товар заново.')
        product_link = input('Введите ссылку на товар: ')
        with open('product_link.txt', 'w') as file:
            file.write(product_link)
    return product_link

def get_product_info(product):
    options = Options()
    options.add_argument('--headless')  
    
    driver = webdriver.Chrome(options=options)
    driver.get("https://funpay.com/lots/" + product + "/")

    sort_button = driver.find_element(By.XPATH, "//div[@class='tc-price sort']")
    driver.execute_script("arguments[0].click();", sort_button)
    
    time.sleep(4)
    
    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a', class_='tc-item')

    for i, link in enumerate(links):
        if i >= 10:
            break
        url = link.get('href')
        name = soup.find_all("div", class_="tc-desc-text")[i].text
        price = soup.find_all("div", class_="tc-price")[i].text
        
        result_msg = f"Ссылка на товар - {url}\nИмя товара - {name}\nЦена товара - {price}\n"
        bot.send_message('CHAT ID', result_msg)

bot = telebot.TeleBot('TOKEN БОТА')

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, f"Привет! Отправь мне ссылку на лот, который нужно спарсить. \nID чата:> {message.chat.id}")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    product_link = message.text.strip()
    if product_link:
        get_product_info(product_link)
    else:
        bot.send_message(message.chat.id, "Неправильный формат ссылки.")

bot.polling()
