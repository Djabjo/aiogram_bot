from aiogram import Router, F, Bot, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


from keyboards.for_questions import Ministry_of_Justice_kb
from credo_expasoft.expa_credo import transliterate, pass_generation

router = Router()

#########################################################################################################    
# Command(start)
@router.message(Command("start"))  
async def cmd_start(message: Message):
    await message.answer(
        f"Я бот, Memorizer\n"
        f'Добро пожаловать, {message.from_user.first_name}\n'
        f"/start - начать заново\n"
        f"/data - для работы с базой данных Memorizer\n"
        f"/credo - генирация login, pass\n"
        f"/clear - очистка переписки\n" 
        )
#########################################################################################################   


#########################################################################################################
#Command(data) работа с памятью   
temporary_user_data_entered = []

class UserData(StatesGroup):
    tag = State()
    topic = State()
    text_data = State()

@router.message(Command("data"))  
async def cmd_input(message: Message):
    await message.answer(
        f"Раздел отвечает за работу с базой данных!!!\n" 
        f"Выбирите вариант для продолжения работы",
        reply_markup=Ministry_of_Justice_kb()
        )
    

@router.message(F.text.lower() == "добавить информацию в database")
async def add_data_archive(message: Message, state: FSMContext):
    await state.set_state(UserData.tag)
    await message.answer(
        f"Введите тег темы",
        reply_markup=types.ReplyKeyboardRemove()
    )


@router.message(UserData.tag)
async def tag(message: Message, state: FSMContext):
    await state.update_data(tag=message.text)
    global tag_data
    tag_data = message.text
    temporary_user_data_entered.append(tag_data)
    await state.set_state(UserData.topic)
    await message.answer(
        f"Добавте тему"
    )

@router.message(UserData.topic)
async def topic(message: Message, state: FSMContext):
    await state.set_state(UserData.topic)
    global topic_data
    topic_data = message.text
    temporary_user_data_entered.append(topic_data)
    await state.set_state(UserData.text_data)
    await message.answer(
        f"Добавте текс темы"
    )


@router.message(UserData.text_data)
async def text_topic(message: Message, state: FSMContext):
    global text_data
    text_data = message.text
    temporary_user_data_entered.append(text_data)
    await message.answer(
        f"{temporary_user_data_entered}"
    )


    await state.clear()

#########################################################################################################


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
    await state.update_data(name_fio=message.text)
    global FIO_name
    FIO_name = message.text
    FIO_name= str((transliterate(FIO_name)))
    FIO_en = FIO_name.split(" ")
    login = FIO_en[0][0].lower() + "." + FIO_en[1].lower()     
    pas = pass_generation()
    await message.answer(
        f"Имя фамилия на английском <code>{FIO_name}</code>\n"
        f"\n"
        f"#mail\n"
        f"url:  <code>https://passport.yandex.ru/auth</code>\n"
        f"mail: <code>{login}@expasoft.com\n</code>"
        f"pass: <code>{pas}</code>\n"
        f"\n"
        f"#wiki\n"
        f"url:  <code>https://confluence.expasoft.com/</code> \n"
        f"login: <code>{login}</code>\n"
        f"pass: <code>{pas}</code>\n"
        f"\n"
        f"#gitlab\n"
        f"url:  <code>https://gitlab.expasoft.com</code>\n"
        f"login: <code>{login}</code>\n"
        f"pass: должен прийти на корп почту\n"
        )
    await state.clear()
###############################################################################################


#########################################################################################################
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