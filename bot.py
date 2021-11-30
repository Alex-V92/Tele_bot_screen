import config
import telebot
import pyautogui
from os.path import exists, isfile
from os import remove
from time import gmtime, strftime

bot = telebot.TeleBot(config.TOKEN)
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    if isfile('test.png'):
        remove('test.png')
    bot.send_message(message.chat.id, 'Отправка скриншота...')
    bot.send_message(message.chat.id, strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    pyautogui.screenshot( 'test' +'.png')
    bot.send_photo(message.chat.id,open('test.png','rb'))

if __name__ == '__main__':
    bot.polling(none_stop=True)