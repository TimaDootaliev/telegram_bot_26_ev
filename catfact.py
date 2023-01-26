import json

import requests
import telebot
from telebot import types

token = 'ВСТАВЬТЕ ВАШ ТОКЕН' # токен - ключ доступа к бота

bot = telebot.TeleBot(token) # в переменную сохранен тип данных Бота, чтобы можно было задавать ему команды

def get_fact(): 
    """  
    Функция для парсинга сайта с фактами о котах
    """
    url = 'https://catfact.ninja/fact/'
    response = requests.get(url).text
    return json.loads(response)['fact']


@bot.message_handler(commands=['start']) # определяем декоратор для отлова сообщения и в commands указываем, чтобы эта функция срабатывала только на команду /start
def hello_func(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True) # создаем клавиатуру, resize_keyboard - для оптимизации размера клавиатуры
    button = types.KeyboardButton('Получить факт') # создаем кнопку и помещаем в нее текст, который отображается на кнопке
    keyboard.add(button) # добавляем кнопку в клавиатуру
    bot.send_message(message.chat.id, 'Привет! Нажми на кнопку и получи факт о котах', reply_markup=keyboard) 
    # говорим боту с помощью .send_message(айди_чата - куда отправлять сообщения, текст сообщения, отдаем клавиатуру с кнопкой)
    # чтобы он отправил сообщения с указанными данными

# определяем декоратор для отлова сообщения, помещаем функцию, которая является фильтром - функция сработает только в том случае, если текст сообщения равен "Получить факт"
@bot.message_handler(func=lambda message: message.text == 'Получить факт') 
def send_fact(message: types.Message):
    fact = get_fact() # в переменную сохранили результат вызова функции для получения факта
    bot.reply_to(message, fact)
    # говорим боту, чтобы ответил на указанное сообщение фактом


bot.polling() # запускаем бота