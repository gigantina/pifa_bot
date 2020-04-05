# -*- coding: utf-8 -*-
import telebot
import config
import functions as f

from levels import User

bot = telebot.TeleBot(config.TOKEN)
user = User(bot)

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = f.menu()
    bot.send_message(message.chat.id,
                     'Привет, {0.first_name}!\n Я Пифа, кабарга. Создана для выполнения крайне необходимых задач) Ну а если хочешь узнать, кто это такая ваша кабарга, то вот ссылка: https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D0%B1%D0%B0%D1%80%D0%B3%D0%B0'.format(
                         message.from_user), parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def dialog(message):
    global user


    if message.text != 'Хватит' and user.weather:
        user.weather = False
        gorod = str(message.text)
        temperature = f.weather(gorod)
        bot.send_message(message.chat.id, temperature)

    elif message.text != 'Хватит' and user.number:
        number = str(message.text)
        number = f.simple(number)
        user.number = False
        bot.send_message(message.chat.id, number)

    elif message.text == 'Хватит':
        user.number = False
        user.weather = False
        markup = f.menu()
        bot.send_message(message.chat.id, 'Ok')

    elif message.text == '5 Новостей':
        for i in f.parser():
            bot.send_message(message.chat.id, i)

    elif message.text == 'Орел и Решка':
        choice = f.orel()
        bot.send_message(message.chat.id, choice)
    elif message.text == 'Простое число':
        user.number = True
        markup = f.break_()
        bot.send_message(message.chat.id, 'Введи число', parse_mode='html', reply_markup=markup)

    elif message.text == 'Погода':
        user.weather = True
        markup = f.break_()
        bot.send_message(message.chat.id, 'Введи город', parse_mode='html', reply_markup=markup)
    elif message.text == 'Погода':
        bot.send_message(message.chat.id, 'Введи город', parse_mode='html')
        perehod()

    elif message.text == 'Угадай число':
        bot.send_message(message.chat.id, x)

    else:
        bot.send_message(message.chat.id, 'Мой глупый автор не прописал диалоги 😢')


def perehod():
    def weather_in_bot(message):
        gorod = str(message.text)
        temperature = f.weather(gorod)
        bot.send_message(message.chat.id, temperature)


def numbers(x):
    y = randint(1, 1000000)
    if y == x:
        bot.send_message(message.chat.id, 'Вы победили!')
    else:
        bot.send_message(message.chat.id, 'Нет, на самом деле {}'.format(y))


bot.polling(none_stop=True, interval=0)
        temperature = f.weather(gorod)
        bot.send_message(message.chat.id, temperature)

def numbers(x):
    y = randint(1, 1000000)
    if y == x:
        bot.send_message(message.chat.id, 'Вы победили!')
    else:
        bot.send_message(message.chat.id, 'Нет, на самом деле {}'.format(y))

>>>>>>> d276710030e369136b605d481efb2948d1758740
bot.polling(none_stop=True, interval=0)
