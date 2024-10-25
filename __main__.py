import asyncio
import logging
import sys
import sqlite3

from aiogram import Bot, Dispatcher, html, types, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command 
from aiogram.types import Message
from aiogram.exceptions import TelegramBadRequest
from conf import TOKEN_aiogram

#database
db = sqlite3.connect('/home/kotov/protgekt/aiogram_bot/Database/Chat_history.db', check_same_thread=False)
cursor = db.cursor()

def db_table_val(titul: str, text: str):
	cursor.execute('INSERT INTO db (titul, text) VALUES (?, ?, ?, ?)', (titul, text))
	db.commit()


TOKEN = TOKEN_aiogram
dp = Dispatcher()

#просто отчистка чата
async def clear(message: types.Message, bot: Bot) -> None:
    try:
        # Все сообщения, начиная с текущего и до первого (message_id = 0)
        for i in range(message.message_id, 0, -1):
            await bot.delete_message(message.from_user.id, i)
    except TelegramBadRequest as ex:
        if ex.message == "Bad Request: message to delete not found":
            print("Все сообщения удалены")

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
https://developer.download.nvidia.com/compute/cuda/12.2.2/local_installers/cuda-repo-ubuntu2204-12-2-local_12.2.2-535.104.05-1_amd64.deb
#Кнопка "Предоставить данные из Database"
@dp.message(F.text.lower() == "Добавить информацию в Database")
async def history_message(message: Message):
    await message.answer("Ожидание ввода...")
    user_text = await dp.bot.wait_for(types.Message, chat_id=message.from_user.id)
    print(user_text)
    user_text =''.join(user_text)
    print(user_text)
    db_table_val(titul=str(user_text[0]), text=str(user_text[1:]))
    await message.reply("Данные были добавленны в архив")


#Кнопка "очистка чата /clear"
@dp.message(F.text.lower() == "очистка чата /clear")
async def with_clear(message: types.Message, bot: Bot):
    await clear(message, bot)

# это все для стабильно работы чата
async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

#БАЗА
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())