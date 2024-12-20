from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from keyboards.db_keyboards import Ministry_of_Justice_kb, delete_text_db
from Database.database_cod import  db_table_val


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
        f"/credo - генирация mail, login, pass\n"
        f"/clear - очистка переписки\n" 
        )
#########################################################################################################   


#########################################################################################################
#Command(data) работа с памятью   
temporary_user_data_entered = ["","",""]

class UserData(StatesGroup):
    tag = State()
    topic = State()
    text_data = State()

@router.message(Command("data"))  
async def cmd_input(message: Message):
    await message.answer(
        f"Раздел отвечает за работу с базой данных\n" 
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
    temporary_user_data_entered[0] = tag_data
    await state.set_state(UserData.topic)
    await message.answer(
        f"Добавте тему"
    )

@router.message(UserData.topic)
async def topic(message: Message, state: FSMContext):
    await state.set_state(UserData.topic)
    global topic_data
    topic_data = message.text
    temporary_user_data_entered[1]= topic_data
    await state.set_state(UserData.text_data)
    await message.answer(
        f"Добавте текст темы"
    )


@router.message(UserData.text_data)
async def text_topic(message: Message, state: FSMContext):
    global text_data
    text_data = message.text
    temporary_user_data_entered[2] = text_data
    id_u = message.from_user.id
    db_table_val(id_user = id_u, 
        tag =temporary_user_data_entered[0],
        topic = temporary_user_data_entered[1],
        text = temporary_user_data_entered[2]
        )
    await message.answer(
        f"данные успешно добавленны в базу",
        reply_markup=delete_text_db()
        )

    await state.clear()

@router.message(F.text.lower() == "завершить работу")
async def finish_working_db(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        f'нажмите /start для возврата в главное меню',
        reply_markup=types.ReplyKeyboardRemove(
            selective=True)
        )
#########################################################################################################
