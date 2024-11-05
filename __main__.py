import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

#токен
from conf import TOKEN_aiogram
#из папки andlers импортируем python file qуuestions
from handlers import questions

TOKEN = TOKEN_aiogram
dp = Dispatcher()

# это все для стабильно работы чата
async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.include_routers(questions.router)
    await dp.start_polling(bot)

#БАЗА
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())