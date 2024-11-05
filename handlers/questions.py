from aiogram import Router, F, Bot, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.exceptions import TelegramBadRequest


from keyboards.for_questions import Ministry_of_Justice_kb

router = Router()

@router.message(Command("start"))  
async def cmd_start(message: Message):
    await message.answer(
        "Вы довольны своей работой?",
        reply_markup=Ministry_of_Justice_kb()
        )


#просто отчистка чата
async def clear(message: types.Message, bot: Bot) -> None:
    try:
        # Все сообщения, начиная с текущего и до первого (message_id = 0)
        for i in range(message.message_id, 0, -1):
            await bot.delete_message(message.from_user.id, i)
    except TelegramBadRequest as ex:
        if ex.message == "Bad Request: message to delete not found":
            print("Все сообщения удалены")

#Кнопка "очистка чата /clear"
@router.message(F.text.lower() == "очистка чата /clear")
async def with_clear(message: types.Message, bot: Bot):
    await clear(message, bot)