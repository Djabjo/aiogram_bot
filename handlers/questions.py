from aiogram import Router, F, Bot, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


from keyboards.for_questions import Ministry_of_Justice_kb

router = Router()

class UserData(StatesGroup):
    name = State()
    orga = State()
    location = State()
    contacts = State()
    side = State()
    finmat = State()
    period = State()

@router.message(Command("start"))  
async def cmd_start(message: Message):
    await message.answer(
        "Вы довольны своей работой?",
        reply_markup=Ministry_of_Justice_kb()
        )

@router.message(F.text.lower() == "Добавить информацию в Database")
async def add_data_arhive(message: Message, state: FSMContext):
    await state.set_state(UserData.name)
    await message.answer(
        text=f"Как я могу к вам обращаться?",
        parse_mode=None,
        reply_markup=types.ReplyKeyboardRemove()
    )

@router.message(UserData.name)
async def user_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    global name_data
    name_data = message.text
    print(name_data)
    await state.set_state(UserData.orga)
    await message.answer(
        text=f"Приятно познакомиться {message.text}.\n"
             f"Укажите название вашей организации",
        parse_mode=None
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