# -*- coding: utf-8 -*-
import telebot
import config
import functions

from telebot import types

weather_ = False
simple_ = False

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("5 Новостей")
    item2 = types.KeyboardButton("Простое число")
    item3 = types.KeyboardButton('Орел и Решка')
    item4 = types.KeyboardButton('Погода')
    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id,
                     'Привет, {0.first_name}!\n Я Пифа, кабарга. Создана для выполнения крайне необходимых задач) Ну а если хочешь узнать, кто это такая ваша кабарга, то вот ссылка: https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D0%B1%D0%B0%D1%80%D0%B3%D0%B0'.format(
                         message.from_user), parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def dialog(message):
    global weather_
    global simple_
    if message.text == '5 Новостей':
        for i in functions.parser():
            bot.send_message(message.chat.id, i)

    elif message.text == 'Орел и Решка':
        choice = functions.orel()
        bot.send_message(message.chat.id, choice)

    elif message.text == 'Простое число':
        simple_ = True
        bot.send_message(message.chat.id, 'Введи число')

    elif message.text == 'Погода':
        weather_ = True
        bot.send_message(message.chat.id, 'Введи город')

    elif message.text != 'Погода' and weather_:
        weather_ = False
        gorod = str(message.text)
        temperature = functions.weather(gorod)
        bot.send_message(message.chat.id, temperature)

    elif message.text != 'Простое число' and simple_:
        number = str(message.text)
        number = functions.simple(number)
        simple_ = False
        bot.send_message(message.chat.id, number)

    else:
        bot.send_message(message.chat.id, 'Мой глупый автор не прописал диалоги 😢')


bot.polling(none_stop=True, interval=0)