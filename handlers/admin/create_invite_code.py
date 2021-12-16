from aiogram import types

from data.config import admins
import random
from loader import dp

from utils.db_api import quick_commands_invitaion_code as command_invite_code
from keyboards.inline.menu_button import menu_choice_admins

def count_up_to():
    count = 151212
    while True:
        count += random.randrange(100, 120)
        yield count


@dp.callback_query_handler(text_contains="invete_code_button", state=None, user_id=admins)
async def enter_test(call: types.Message):
    await call.answer(cache_time=1130)
    await call.message.answer("...готовлю код-приглашение... \n")
    codes = count_up_to()
    code = codes.__next__()
    await command_invite_code.generate_referral_code(invitation_code_id=code)
    await call.message.answer(f"{code}",
                              reply_markup=menu_choice_admins)
