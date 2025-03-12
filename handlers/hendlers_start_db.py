from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


from keyboards.db_keyboards import itial_menu_kb, completion_text_kb, tag_selection_kb, topic_selection_kb
from Database.database_cod import  input_all_lines_db, del_last_commit_db, text_topic_output_db, checking_the_availability_db



router = Router()

#########################################################################################################    
# Command(start)
@router.message(Command("start"))  
async def cmd_start(message: Message):
    await message.answer(
        f"Я бот, Memorizer\n"
        f'Добро пожаловать, {message.from_user.first_name}\n'
        f"/data - для работы с базой данных Memorizer\n"
        f"/credo - генирация mail, login, pass\n"
        f"/clear - очистка переписки\n" 
        )



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
        f"Выбирите вариант для продолжения",
        reply_markup=itial_menu_kb()
        )
    

@router.message(F.text.lower() == "добавить информацию в database")
async def add_data_archive(message: Message, state: FSMContext):
    await state.set_state(UserData.tag)
    await message.answer(
        f"Краткое содержание перед началом работы с добавлением данных\n"
        f"\n"
        f"название тега и темы не должны превышать 64бита это примерно 4-5 слов\n"
        f"\n"
        f"если хотите что бы текст можно было копировать, вставьте HTML код\n"
        f"в начало пропишите code экранируя символами ⌞ ⌝  и /code экранируя символами ⌞ ⌝  в конец,/n"
        f" места где хотите что бы текст можно было копировать"
    )
    await message.answer(
        f"Введите тег темы",
        reply_markup=types.ReplyKeyboardRemove(
            selective=True)
    )


@router.message(UserData.tag)
async def tag(message: Message, state: FSMContext):
    await state.update_data(tag=message.text)
    global tag_data
    tag_data = message.text 
    if len(tag_data.encode('utf-8')) >= 60:
        await message.answer(
        f"дли текста привышает допустимые параметры"
        f"начните сначало /data"
        )
        await state.clear()
    else:
        temporary_user_data_entered[0] = tag_data
        await state.set_state(UserData.topic)
        await message.answer(
        f"Добавте тему"
        )


@router.message(UserData.topic)
async def topic(message: Message, state: FSMContext):
    await state.set_state(UserData.topic)
    global topic_id
    topic_id = message.text
    if len(tag_data.encode('utf-8')) >= 60:
        await message.answer(
        f"дли текста привышает допустимые параметры"
        f"начните сначало /data"
        )
        await state.clear()
    else:
        temporary_user_data_entered[1] = topic_id
        await state.set_state(UserData.text_data)
        await message.answer(
            f"Добавте текст темы"
        )


@router.message(UserData.text_data)
async def text_topic(message: Message, state: FSMContext):
    global text_data
    text_data = message.text
    temporary_user_data_entered[2] = text_data
    id_user = message.from_user.id
    input_all_lines_db(id_user = id_user, 
        tag =temporary_user_data_entered[0],
        topic = temporary_user_data_entered[1],
        text = temporary_user_data_entered[2]
        )
    await message.answer(
        f"данные успешно добавленны в базу",
        reply_markup=completion_text_kb()
        )
    await state.clear()


#########################################################################################################   
# Обработчик вывода информации из DB
@router.message(F.text.lower() == "предоставить данные из database")
async def add_data_archive(message: Message, state: FSMContext):
    global user_id
    user_id = message.from_user.id
    db_inf = checking_the_availability_db(user_id)
    if db_inf == []:
        await message.answer(
        f"В базе данных нет записей, дальнейшая работа не возможно.\n"
        f"вернитесь в начало /data и создайте запись",
        reply_markup=types.ReplyKeyboardRemove()
        )
    else:
        await message.answer(
            f"Добро пожаловать в ващу базу {message.from_user.first_name}",
            reply_markup=types.ReplyKeyboardRemove()
        )
        await message.answer(
            f"выбирете тег темы",
            reply_markup = tag_selection_kb(int(user_id))
        )


@router.callback_query(F.data.startswith('ta_'))
async def db_tag_in(call: CallbackQuery):
    await call.answer()
    await call.message.edit_reply_markup()
    global tag_id
    tag_id = str(call.data.split('_')[1])
    await call.message.answer(
        f"Выбрана тема тега {tag_id}",
        reply_markup=topic_selection_kb(str(user_id), tag_id)
        )


@router.callback_query(F.data.startswith('to_'))
async def db_texttopic_output(call: CallbackQuery):
    await call.answer()
    await call.message.edit_reply_markup()
    global topic_id
    topic_id = call.data.split('_')[1]
    text = text_topic_output_db(user_id, topic_id) 
    await call.message.answer(
        f"По данному запросу {tag_id}, {topic_id} вывожу информацию\n"
        f"\n"
        f"{text}",
        reply_markup = completion_text_kb()
        )
    

#########################################################################################################   
# Варианты завершения работы с DB
@router.message(F.text.lower() == "завершить работу")
async def finish_working_db(message: Message):
    await message.answer(
        f'нажмите /start для возврата в главное меню',
        reply_markup=types.ReplyKeyboardRemove(
            selective=True)
        )

@router.message(F.text.lower() == "редактировать")
async def edit(message: Message, state: FSMContext):
    await message.answer(
        f"В разработке, нажмите /start\n",
        reply_markup=types.ReplyKeyboardRemove(
            selective=True)
        )

@router.message(F.text.lower() == "удалить запись")
async def finish_working_db(message: Message, state: FSMContext):
    user_id = message.from_user.id
    del_last_commit_db(user_id, topic_id )
    await message.answer(
        f"последние данные были удалены, нажмите /start\n"
        f"для возврата в главное меню",
        reply_markup=types.ReplyKeyboardRemove(
            selective=True)
        )
    await state.clear()
    