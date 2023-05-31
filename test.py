from telebot import TeleBot

token = '5958379856:AAHeqrlx49S04Aax3mTLjO8XW1tA-9OkWZU'
bot = TeleBot(token)
bot.delete_webhook()

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет')


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    bot.send_message(message.from_user.id,message.text)




bot.polling(none_stop=True,interval=0)