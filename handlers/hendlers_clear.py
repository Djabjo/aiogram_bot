from aiogram import Router, F, Bot, types
from aiogram.filters import Command
from aiogram.exceptions import TelegramBadRequest

router = Router()

#очистка чата от сообщений 
async def clear(message: types.Message, bot: Bot) -> None:
    try:
        # Все сообщения, начиная с текущего и до первого (message_id = 0)
        for i in range(message.message_id, 0, -1):
            await bot.delete_message(message.from_user.id, i)
    except TelegramBadRequest as ex:
        if ex.message == "Bad Request: message to delete not found":
            print("Все сообщения удалены")


@router.message(Command("clear"))
async def cmd_clear(message: "clear", bot: Bot):
   await clear(message, bot)