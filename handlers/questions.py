from aiogram import Router, F, Bot, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


from keyboards.for_questions import Ministry_of_Justice_kb
from credo_expasoft.expa_credo import transliterate, pass_generation

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
        f'Добро пожаловать, {message.from_user.first_name}\n'
        f"Я бот, Memorizer\n"
        f"/data - для работы с базой данных Memorizer\n"
        f"/credo - для создания credo сотрудников expasoft\n"
        f"/start - начать заново\n"
        f"/clear - очистка чата от сообщений\n" 
        )
@router.message(Command("data"))  
async def cmd_input(message: "data"):
    await message.answer('Доброго времяни суток',
        reply_markup=Ministry_of_Justice_kb()
        )
    

# @router.message(F.text.lower() == "Добавить информацию в Database")
# async def add_data_archive(message: Message, state: FSMContext):
#     await state.set_state(UserData.topic)
#     await message.answer(
#         text=f"как будет называтся тема ?",
#         parse_mode=None,
#         reply_markup=types.ReplyKeyboardRemove()
#     )

# @router.message(UserData.topic)
# async def user_input_topic(message: Message, state: FSMContext):
#     await state.update_data(topic=message.text)
#     test_DB = message.text
#     print(test_DB)
#     await message.answer(
#         text=f"Название темы будет {message.text}.\n"
#              f"укажите текст который хотите добавить",
#         parse_mode=None
#     )



#########################################################################################################
#для рабочих нужд, создает логины и пароли к сервисам    
class UserCred(StatesGroup):
    name_fio = State()

@router.message(Command("credo"))
async def cmd_credentials(message: Message, state: FSMContext):
    await state.set_state(UserCred.name_fio)
    await message.answer(
        text=f"Введите имя и фамилию сотрудника",
        parse_mode=None,
        )

@router.message(UserCred.name_fio)
async def credo_fio(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    global name_data
    name_data = message.text
    name_data = str((transliterate(name_data)))
    FIO_en = name_data.split(" ")
    login = FIO_en[0][0].lower() + "." + FIO_en[1].lower()     
    pas = pass_generation()
    await message.answer(
        f"Имя фамилия на английском <code>{name_data}</code>\n"
        f"\n"
        f"#mail\n"
        f"url:  <code>https://passport.yandex.ru/auth</code>\n"
        f"mail: <code>{login}@expasoft.com\n</code>"
        f"pass: <code>{pas}</code>\n"
        f"\n"
        f"#wiki\n"
        f"url:  <code>https://confluence.expasoft.com/</code> \n"
        f"mail: <code>{login}</code>\n"
        f"pass: <code>{pas}</code>\n"
        f"\n"
        f"#gitlab\n"
        f"url:  <code>https://gitlab.expasoft.com</code>\n"
        f"mail: <code>{login}</code>\n"
        f"pass: должен прийти на корп почту\n"
        )
    await state.clear()
###############################################################################################


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
   

#################################################################################################