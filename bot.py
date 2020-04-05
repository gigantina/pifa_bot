# -*- coding: utf-8 -*-
import telebot
import config
import functions as f



bot = telebot.TeleBot(config.TOKEN)
user = {}


@bot.message_handler(commands=['start'])
def welcome(message):
    global user
    markup = f.menu()
    bot.send_message(message.chat.id,
                     'Привет, {0.first_name}!\n Я Пифа, кабарга. Создана для выполнения крайне необходимых задач) Ну а если хочешь узнать, кто это такая ваша кабарга, то вот ссылка: https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D0%B1%D0%B0%D1%80%D0%B3%D0%B0'.format(
                         message.from_user), parse_mode='html', reply_markup=markup)
    user[message.from_user.id] = {}
    user[message.from_user.id]['weather'] = False


@bot.message_handler(content_types=['text'])
def dialog(message):
    global user
    #user.set(message.from_user.id)
    if message.text != 'Хватит' and user[message.from_user.id]['weather']:
        gorod = str(message.text)
        temperature = f.weather(gorod)
        bot.send_message(message.chat.id, temperature)

    #elif message.text != 'Хватит' and user.number and user.code == message.from_user.id:
     #   number = str(message.text)
      #  number = f.simple(number)
       # bot.send_message(message.chat.id, number)

    elif message.text == 'Хватит':
        #user.number = False
        user[message.from_user.id]['weather'] = False
        markup = f.menu()
        bot.send_message(message.chat.id, 'Ok', reply_markup=markup)

    elif message.text == '5 Новостей':
        for i in f.parser():
            bot.send_message(message.chat.id, i)

    elif message.text == 'Орел и Решка':
        choice = f.orel()
        bot.send_message(message.chat.id, choice)

    elif message.text == 'Простое число':
        #user.number = True
        markup = f.break_()
        bot.send_message(message.chat.id, 'Введи число', parse_mode='html', reply_markup=markup)

    elif message.text == 'Погода':
        user[message.from_user.id]['weather'] = True
        markup = f.break_()
        bot.send_message(message.chat.id, 'Введи город', parse_mode='html', reply_markup=markup)

    elif message.text == 'Угадай число':
        bot.send_message(message.chat.id, x)

    else:
        print(user)
        bot.send_message(message.chat.id, 'Мой глупый автор не прописал диалоги 😢')


def numbers(x):
    y = randint(1, 1000000)
    if y == x:
        bot.send_message(message.chat.id, 'Вы победили!')
    else:
        bot.send_message(message.chat.id, 'Нет, на самом деле {}'.format(y))


bot.polling(none_stop=True, interval=0)
