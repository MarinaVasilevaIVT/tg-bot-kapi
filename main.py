import os
import random
import telebot
from telebot import types
import json

bot = telebot.TeleBot(os.environ.get('BOT_TOKEN'))

dialog = {
    'hello': {
        'in': ['/hello', 'привет', 'hello', 'hi', 'privet', 'hey'],
        'out': ['Приветствую', 'Здравствуйте', 'Привет!']
    },
    'how r u': {
        'in': ['/howru', 'как дела', 'как ты', 'how are you', 'дела', 'how is it going'],
        'out': ['Хорошо', 'Отлично', 'Good. And how are u?']
    },
    'name': {
        'in': ['/name', 'зовут', 'name', 'имя'],
        'out': [
            'Я бот-генератор фото капибар'
        ]
    },
    'love': {
        'in': ['/love', 'я люблю капибар', 'капибара', 'love'],
        'out': [
            'Я тоже очень люблю!',
            'Согласен, самые крутые животные!',
            'I love too!'
        ]
    }
}


# Buttons
button_start = types.KeyboardButton(r'🥺' + " Хочу капибару ")
button_continue = types.KeyboardButton(r'😍' + " Мне нужно больше капибар ")
button_stop = types.KeyboardButton(r'😭' + " Спасибо. Хватит ")


# Keyboards
keyboard_start = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
keyboard_start.add(button_start)
keyboard_continue = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
keyboard_continue.add(button_continue, button_stop)


# Start
@bot.message_handler(commands=['start'])
def start_helper(message):
    start_message = "Привет! Этот бот создан для поднятия настроения и любования прекрасными животными!"
    bot.send_message(message.chat.id, start_message, reply_markup=keyboard_start)


# Send photo
@bot.message_handler(regexp="Хочу капибару")
def send_kitty(message):
    file = str(random.randint(1,11))+'.jpg'
    photo = 'https://storage.yandexcloud.net/kapibara/' + file
    bot.send_photo(message.chat.id, photo, reply_markup=keyboard_continue)


# Continue
@bot.message_handler(regexp="Мне нужно больше капибар")
def send_kitty(message):
    file = str(random.randint(1,11))+'.jpg'
    photo = 'https://storage.yandexcloud.net/kapibara/' + file
    bot.send_photo(message.chat.id, photo, reply_markup=keyboard_continue)


# Stop
@bot.message_handler(regexp="Спасибо. Хватит")
def goodby(message):
    end_message = 'Пока! До скорого!'
    bot.send_message(message.chat.id, end_message, reply_markup=keyboard_start)
    
# Default Reply
@bot.message_handler(func=lambda message: True)
def echo(message):
    for t, resp in dialog.items():
        if sum([e in message.text.lower() for e in resp['in']]):
            bot.send_message(message.chat.id, random.choice(resp['out']))
            return

    bot.send_message(message.chat.id, "Я тебя не понимаю, я могу только показать капибар " + r'😭' , reply_markup=keyboard_start)
