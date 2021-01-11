from telebot import TeleBot 

bot = TeleBot('1517731651:AAGdoRXC-ggDkA3gIQ_sLqBqaJD7ToeAgEQ')


@bot.message_handler(content_types=['new_chat_members'])
def greeting(message):
    bot.reply_to(message, text='hello')


if __name__ == '__main__':
    bot.polling(none_stop=True)