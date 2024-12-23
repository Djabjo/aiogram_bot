from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types 
from Database.database_cod import tag_output

### обработчик Command("data") 
def Ministry_of_Justice_kb() -> ReplyKeyboardMarkup:
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
def delete_text_db() -> ReplyKeyboardMarkup:
    kb = [
        [types.KeyboardButton(text="Завершить работу")],
        [types.KeyboardButton(text="Удалить запись")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        selective=True,
        keyboard=kb,
        resize_keyboard=True
        )
    return keyboard


def tag_selection(id_user):
    tag = tag_output(id_user)
    buttons = []
    for i in tag:
        button = InlineKeyboardButton(text=i, callback_data=i)
        buttons.append(button)
         
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button] for button in buttons])
    return keyboard