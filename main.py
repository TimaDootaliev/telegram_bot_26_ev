import telebot
from telebot import types

token = 'ВСТАВЬТЕ ВАШ ТОКЕН' # токен - ключ доступа к бота

bot = telebot.TeleBot(token) # в переменную сохранен тип данных Бота, чтобы можно было задавать ему команды

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True) # создаем клавиатуру которая отображается снизу чата, resize_keyboard - для оптимизации размера клавиатуры
button = types.KeyboardButton('Тыкни на меня') # создаем кнопку и помещаем в нее текст, который отображается на кнопке
keyboard.add(button) # добавляем кнопку в клавиатуру


# определяем декоратор для отлова сообщения и в commands указываем, чтобы эта функция срабатывала только на команду /start и /hi
@bot.message_handler(commands=['start', 'hi'])
def start_message(message: types.Message):
    chat_id = message.chat.id # сохранили уникальный номер чата
    bot.send_message(chat_id, 'Привет!', reply_markup=keyboard)
    # говорим боту с помощью .send_message(айди_чата - куда отправлять сообщения, текст сообщения, отдаем клавиатуру с кнопкой)
    # чтобы он отправил сообщения с указанными данными

# определяем декоратор для отлова сообщения, помещаем функцию, которая является фильтром - функция сработает только в том случае, если текст сообщения равен "Тыкни на меня"
@bot.message_handler(func=lambda message: message.text == 'Тыкни на меня')
def sticker(message: types.Message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEHbl5j0S_wIVgNBKFQ-xxWtxCEMl9vUgACBQADBc7CLQABkSQpEZrW0i0E')
    # говорим боту, чтобы отправил стикер с помощью .send_sticker(уникальный номер чата, уникальный номер стикера для отправки)

inline_keyboard = types.InlineKeyboardMarkup() # вид клавиатуры, которая отображается под сообщением
inline_button = types.InlineKeyboardButton('Пока', callback_data='mydata') # создаем кнопку для вышеуказанной клавиатуры. callback_data - данные, которые отправляются боту при клике на кнопку
inline_keyboard.add(inline_button) # добавляем кнопку в клавиатуру

@bot.message_handler() # если оставить скобки пустыми - бот будет реагировать на все действия в чате
def get_inline_keyboard(message: types.Message):
    bot.send_message(message.chat.id, 'Нажми на кнопку, чтобы попрощаться', reply_markup=inline_keyboard)


# .callback_query_handler - декоратор для отлова данных, которые отправляются инлайновой кнопкой (см строку 28)
@bot.callback_query_handler(func=lambda callback: callback.data == 'mydata')
def goodbye(callback: types.CallbackQuery):
    bot.send_message(callback.message.chat.id, 'До свидания!')
    bot.send_sticker(callback.message.chat.id, 'CAACAgIAAxkBAAEHbslj0TU2WOQzYNOm-Cutx6_W49aQtgACOBUAAom6KEnpyNUCL5XkrS0E')



# @bot.message_handler()
# def repeat_text(message: types.Message):
#     bot.send_message(message.chat.id, message.text)


bot.polling() # запуск бота

