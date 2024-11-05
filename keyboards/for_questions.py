from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import types 

def Ministry_of_Justice_kb() -> ReplyKeyboardMarkup:
    kb = [
        [types.KeyboardButton(text="Предоставить данные из Database")],
        [types.KeyboardButton(text="Добавить информацию в Database")],
        [types.KeyboardButton(text="очистка чата /clear")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder= 'выбирете вариант ввода'
        )
    return keyboard
        
