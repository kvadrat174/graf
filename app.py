#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from threading import Thread
import schedule
import time
import random
import flask
from dblina import addUser, update_date, getUsers, get_vebinar
from dblina import gSheet
from datetime import datetime, date

import telebot
from telebot import types

API_TOKEN = '1408902919:AAEvdjvYAqd-F8CKYfj1kjPbo7XePG_vVAc'

boss = int(715698611)
eugeniaid = int(1021080604)

bot = telebot.TeleBot(API_TOKEN)

application = flask.Flask(__name__)

markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
itembtn1 = types.KeyboardButton('Опубликовать')
itembtn2 = types.KeyboardButton('Установить дату')
markup.add(itembtn1,itembtn2)


# Process webhook calls
@application.route('/', methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)

def geeks():
    date = datetime.now()
    d = date.day
    h = date.hour
    m = date.minute
    d1 = get_vebinar(eugeniaid)
    print(d1)
    if int(d1[0].split('-')[0]) == d and int(d1[0].split('-')[1])== h and int(d1[0].split('-')[2]) == m :
        text = 'ВНИМАНИЕ‼\n\nВебинар «Выход в ресурс» уже стартовал!🔥\n\nПрисоединяйтесь прямо сейчас, чтобы не пропустить самое важное 👇🏻'
        keyboard1 = telebot.types.InlineKeyboardMarkup()
        keyboard1.row(telebot.types.InlineKeyboardButton('Забирай медитацию', url='https://www.dropbox.com/s/8cl8hscioxrfolx/JENNY.RATION.audio.meditations%20-%20Oblako.mp3?dl=0')),
        users = getUsers()
        for elem in users:
            bot.send_message(elem[0], text, reply_markup=keyboard1)



# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    name = message.from_user.first_name
    ids = message.from_user.id
    if ids == boss or ids == eugeniaid:
        bot.send_message(message.chat.id, f'Здравствуйте, {name}', reply_markup = markup)
    else:
        keyboard6 = telebot.types.InlineKeyboardMarkup()

        keyboard6.row(telebot.types.InlineKeyboardButton('Забирай медитацию', url='https://www.dropbox.com/s/8cl8hscioxrfolx/JENNY.RATION.audio.meditations%20-%20Oblako.mp3?dl=0')),
        bot.send_message(message.chat.id, "Привет, мой друг❤\n\nЯ очень рада видеть тебя в числе участников моего вебинара «Выход в ресурс»!\n\nМеня зовут Евгения, и я буду ведущей этого вебинара. Я собрала различные духовные, психологические и телесные практики, объединив их в одну систему по эффективному выходу в ресурсное состояние.\n\nИ уже совсем скоро я раскрою тайну 6 шагов на вебинаре! ✨\n\nНаша встреча состоится совсем скоро.\n\n8 декабря в 18:00 по Мск времени.\n\nЯ очень жду нашей встречи😍\n\nСсылку на вебинар отправлю за час до его начала! Увидимся :)\n\nА пока, как и обещала, отправляю тебе медитацию ресурса прямо сейчас 👇🏻", reply_markup=keyboard6)
        name = message.from_user.first_name

        databaser = addUser(ids, name)
        if databaser == True:

            res = f'id: {ids}, name: {name},есть в базе'
            # bot.send_message(linaid, res)
            bot.send_message(boss, res)
        else:
            addUser(ids, name)
            res = f'id: {ids}, name: {name},добавлен в базу'

            bot.send_message(boss, res)

'''async def run():
    schedule.every(1).minutes.do(await geeks)

    while True:
        schedule.run_pending()
        time.sleep(2)

thread = Thread(target=run)
thread.start()'''

@bot.message_handler(content_types=['text'])
def get_data(message):

    name = message.from_user.first_name
    ids = message.from_user.id
    if ids == boss or ids == eugeniaid:
        if message.text.lower() == 'опубликовать':
            bot.send_message(ids, 'Отправьте сообщение, которое хотите опубликовать')
            bot.register_next_step_handler(message, get_problem2)

        elif message.text.lower() == 'установить дату':
            bot.send_message(ids, 'отправьте дату вебинара в формате ДЕНЬ-ЧАС-МИНУТА, например 8-18-00')
            bot.register_next_step_handler(message, get_problem1)


def get_problem1(message):
    global vebinar
    vebinar = message.text
    name = message.from_user.first_name
    ids = message.from_user.id
    databaser = update_date(ids, vebinar)

def get_problem2(message):
    global mes
    mes = message.text
    users = getUsers()
    print(users)
    for elem in users:
        bot.send_message(elem[0], mes)




bot.remove_webhook()

time.sleep(0.1)

# Set webhook
bot.set_webhook(
    url='https://api.telegram.org/bot1408902919:AAEvdjvYAqd-F8CKYfj1kjPbo7XePG_vVAc/setWebhook?url=https://zzzsladko.ru')

# Start flask server
if __name__ == "__main__":
    application.run(debug=True)