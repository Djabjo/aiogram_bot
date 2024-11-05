import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
<<<<<<< HEAD
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command 
from aiogram.types import Message, CallbackQuery
from aiogram.exceptions import TelegramBadRequest

from conf import TOKEN_aiogram

#database
db = sqlite3.connect('Database/Chat_history.db', check_same_thread=False)
cursor = db.cursor()
=======
from handlers import questions


from conf import TOKEN_aiogram

# #database
# db = sqlite3.connect('/home/kotov/protgekt/aiogram_bot/Database/Chat_history.db', check_same_thread=False)
# cursor = db.cursor()
>>>>>>> e1a0a6f667a298614076d4d6daaf95f240610e49

# def db_table_val(titul: str, text: str):
# 	cursor.execute('INSERT INTO db (titul, text) VALUES (?, ?, ?, ?)', (titul, text))
# 	db.commit()


TOKEN = TOKEN_aiogram
dp = Dispatcher()


<<<<<<< HEAD
#команда start основаня функция работы чата
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
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
    await message.answer("Выбирете дальнейшие действие", reply_markup=keyboard)

#Кнопка "Предоставить данные из Database"
@dp.message(F.text.lower() == "Добавить информацию в Database")
async def history_message(message: types.Message):
    await message.reply("Ожидается ввод", reply_markup=types.ReplyKeyboardRemove)
=======

#Кнопка "Предоставить данные из Database"
# @dp.message(F.text.lower() == "Добавить информацию в Database")
# async def history_message(message: Message):
#     await message.answer("Ожидание ввода...")
#     user_text = await dp.bot.wait_for(types.Message, chat_id=message.from_user.id)
#     print(user_text)
#     user_text =''.join(user_text)
#     print(user_text)
#     db_table_val(titul=str(user_text[0]), text=str(user_text[1:]))
#     await message.reply("Данные были добавленны в архив")
>>>>>>> e1a0a6f667a298614076d4d6daaf95f240610e49

    async def process_input(message: Message):
        user_text = message.text
        print(user_text)    
        #user_text = message.text
        #user_text =''.join(user_text)
        #print(user_text)
        #db_table_val(titul=str(user_text[0]), text=str(user_text[1:]))
        #await call.message.edit_text(f"Данные '{user_text}' были добавлены в архив")
   

# это все для стабильно работы чата
async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.include_routers(questions.router)
    await dp.start_polling(bot)

#БАЗА
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())