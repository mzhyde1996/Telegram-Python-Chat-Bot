import telebot
import random

from telebot import types
from telegram import ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


# keyboard
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("♠ Random number")
item2 = types.KeyboardButton("☺ How are you?")
item3 = types.KeyboardButton("🎉Best Show")
item4 = types.KeyboardButton("📽About")
item5 = types.KeyboardButton("📱Our Social Media")
item6 = types.KeyboardButton("😳Interview of the Week")

markup.add(item1, item2, item3, item4, item5, item6)

bot = telebot.TeleBot('2022635300:AAEAaODIz8A3iK9cz7fY9K_sg0dTcM4mlvg')

@bot.message_handler(commands=['help'])
def lalala(message):
        bot.send_message(message.chat.id, "Please contact our support for help https://uk.tlc.com/contact/")

@bot.message_handler(commands=['news'])
def lalala(message):
        bot.send_message(message.chat.id, "I weigh 300 kilos. Inspiring weight loss stories: https://tlc-tv.ru/articles/ya-veshu-300-kg-vdokhnovlyayushchie-istorii-pokhudeniya/, Как сэкономить и накопить: лучшие советы из шоу Экстремальная экономия https://tlc-tv.ru/articles/kak-sekonomit-i-nakopit-luchshie-sovety-iz-shou-ekstremalnaya-ekonomiya/, Поиск родителей помог женщине обнаружить преступления 50-летней давности https://tlc-tv.ru/articles/poisk-roditeley-pomog-zhenshchine-obnaruzhit-prestupleniya-50-letney-davnosti/")        

@bot.message_handler(commands=['site'])
def lalala(message):
        bot.send_message(message.chat.id, "https://tlc-tv.ru/")


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEDJvdhd5N2CTutXatGkL1tpjjNFj3RgwACVQIAAladvQqsSyyCT6MV3yEE")
    bot.send_message(message.chat.id, "Welcome, {0.first_name}!\nI am a bot for <b>TLC channel</b>, you can get help by typing /help, read news by typing /news, get a link to the channel official website by pressing /site".format(message.from_user, bot.get_me()),
        parse_mode='html' , reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '♠ Random number':
           bot.send_message(message.chat.id, str(random.randint(0,100)))
        elif message.text == '☺ How are you?': 

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Good", callback_data='good')
            item2 = types.InlineKeyboardButton("Bad", callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Amazing, how are you?', reply_markup=markup)

        elif message.text == '🎉Best Show':
            bot.send_message(message.chat.id, "90 day fiance 👰🤵, YouTube https://www.youtube.com/channel/UCgIWIkGWCV9knhMvK3Q8usA")
            
        elif message.text == '📽About':
            bot.send_message(message.chat.id, "TlC - from the founders of Discovery Channel.")

        elif message.text == '📱Our Social Media':
            bot.send_message(message.chat.id, "Инстаграм https://www.instagram.com/tlc.russia/, YouTube https://www.youtube.com/c/TLCRussia/videos")

        elif message.text == '😳Interview of the Week':
            bot.send_message(message.chat.id, "https://tlc-tv.ru/articles/garri-i-megan-krasivaya-istoriya-lyubvi/")

        else:
            bot.send_message(message.chat.id, 'I do not know how to answer this question.😞 You can find feedback form on our official website')


@bot.callback_query_handler(func=lambda call: True)
def callback_incline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'That is wonderful 😀')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, "I am so sorry about that 😟")  
   

    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
