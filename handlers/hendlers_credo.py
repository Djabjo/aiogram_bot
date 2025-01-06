
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from credo_expasoft.expa_credo import transliterate, pass_generation


router = Router()


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

    