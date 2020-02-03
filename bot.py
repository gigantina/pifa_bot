# -*- coding: utf-8 -*-
import telebot
import config
import functions as f

weather_ = False
simple_ = False

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = f.menu()
    bot.send_message(message.chat.id,
                     'Привет, {0.first_name}!\n Я Пифа, кабарга. Создана для выполнения крайне необходимых задач) Ну а если хочешь узнать, кто это такая ваша кабарга, то вот ссылка: https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D0%B1%D0%B0%D1%80%D0%B3%D0%B0'.format(
                         message.from_user), parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def dialog(message):
    global weather_
    global simple_

    if message.text != 'Хватит' and weather_:
        gorod = str(message.text)
        temperature = f.weather(gorod)
        bot.send_message(message.chat.id, temperature)

    elif message.text != 'Хватит' and simple_:
        number = str(message.text)
        number = f.simple(number)
        bot.send_message(message.chat.id, number)

    elif message.text == 'Хватит':
        simple_ = False
        weather_ = False
        markup = f.menu()
        bot.send_message(message.chat.id, 'Ок', parse_mode='html', reply_markup=markup)

    elif message.text == '5 Новостей':
        for i in f.parser():
            bot.send_message(message.chat.id, i)

    elif message.text == 'Орел и Решка':
        choice = f.orel()
        bot.send_message(message.chat.id, choice)

    elif message.text == 'Простое число':
        simple_ = True
        markup = f.break_()
        bot.send_message(message.chat.id, 'Введи число', parse_mode='html', reply_markup=markup)

    elif message.text == 'Погода':
        weather_ = True
        markup = f.break_()
        bot.send_message(message.chat.id, 'Введи город', parse_mode='html', reply_markup=markup)

    else:
        bot.send_message(message.chat.id, 'Мой глупый автор не прописал диалоги 😢')


bot.polling(none_stop=True, interval=0)