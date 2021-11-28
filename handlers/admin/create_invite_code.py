from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ContentType
from data.config import admins
import random
from loader import dp
from states.add_product_state import InventoryList

from utils.db_api import quick_commands_invitaion_code as command_invite_code


def count_up_to():
    count = 151212
    while True:
        count += random.randrange(100, 120)
        yield count


@dp.message_handler(Command("invitecode"), state=None, user_id=admins)
async def enter_test(message: types.Message):
    await message.answer("/...готовлю код-приглашение... \n")
    codes = count_up_to()
    code = codes.__next__()
    await command_invite_code.generate_referral_code(invitation_code_id=code)
    await message.answer(f"{code}")
