from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types

from Database.database_cod import tag_output_db, topic_output_db

### обработчик Command("data") 
def itial_menu_kb() -> ReplyKeyboardMarkup:
    kb = [
        [types.KeyboardButton(text="Предоставить данные из Database")],
        [types.KeyboardButton(text="Добавить информацию в Database")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder= 'выбирете вариант ввода'
        )
    return keyboard

#клавиатура завершения работы с добавлением данных        
def completion_text_kb() -> ReplyKeyboardMarkup:
    kb = [
        [types.KeyboardButton(text="Завершить работу")],
        [types.KeyboardButton(text="Удалить запись")],
        [types.KeyboardButton(text="Редактировать")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        selective=True,
        keyboard=kb,
        resize_keyboard=True
        )
    return keyboard

def tag_selection_kb(id_user):
    tag = tag_output_db(id_user)
    buttons = []
    for i in tag:
        button = InlineKeyboardButton(text=i, callback_data=f"ta_{i}")
        buttons.append(button)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button] for button in buttons])
    return keyboard

def topic_selection_kb(id_user, tag):
    topic = topic_output_db(int(id_user), tag)
    buttons = []
    for item in topic:
        button = InlineKeyboardButton(text=item, callback_data=f"to_{item}")
        buttons.append(button)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button] for button in buttons])
    return keyboard
