# Парсер FunPay через телеграмм

Устанавливаем python 3.11.7 (моя версия).

Запускаем CMD --> cd (путь к файлу) --> pip install -r requirements.txt

Ждём конца установки.

Создаем бота в тг https://t.me/BotFather,после изменяем в = telebot.TeleBot('TOKEN БОТА') на тот которой нам выдал bot father.

Запускаем main.py и заходим в тг бота которой мы создали,получаем chat id,изменяем его в bot.send_message('CHAT ID', result_msg).

В тг с ботом пишем цифры лотов,например: https://funpay.com/lots/922/ ,боту пишем 922

Готово! Приятного использования.

![image](https://avatars.githubusercontent.com/u/149227120?s=400&u=7c7dd7262663f12f8f67aa2b71a392544b725dec&v=4)
