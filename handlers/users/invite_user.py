from aiogram.dispatcher.filters import CommandStart, Command
from aiogram import types
import re

from asyncpg import UniqueViolationError

from keyboards.inline.start_button import start_choice
from loader import db

from aiogram.utils.deep_linking import get_start_link
from gino.dialects import asyncpg

from filters import IsPrivate
from loader import dp

from utils.db_api import quick_commands_referral as command_referral
from utils.db_api import quick_commands_user as command_user


# генерируем deep_link ссылку
@dp.message_handler(Command("invite"))
async def bot_start(message: types.Message):
    deep_link = await get_start_link(payload=f"{message.from_user.id}")
    await command_referral.add_referral(referer_id=message.from_user.id,
                                        referer_first_name=str(message.from_user.first_name),
                                        referer_last_name=str(message.from_user.last_name))
    await message.answer(f"Привет! \n"
                         f"Заходи в магазин по ссылке \n\n"
                         f"{deep_link}")


# Этот хендлер используется для диплинков:
@dp.message_handler(CommandStart(deep_link=re.compile(r"^[0-9]{4,15}$")))
async def bot_start_deeplink(message: types.Message):
    # С помощью функции get_args забираем аргументы после команды start. (для примера выше - будет "123")

    deep_link_args = int(message.get_args())
    print(deep_link_args)
    try:
        user_referrer = await command_referral.select_referal(referer_id=deep_link_args)

        await command_referral.update_referral_balance(referer_id=user_referrer.referer_id, bonus=10)
        await command_user.add_user(user_id=message.from_user.id, user_first_name=message.from_user.first_name,
                                    user_last_name=message.from_user.last_name)
        await message.answer(f'Привет, {message.from_user.full_name}!\n'
                             f'Это магазин чудес. \n\n',
                             reply_markup=start_choice)


    except UniqueViolationError:
        await message.answer(f'Привет, {message.from_user.full_name}!\n\n'
                             f'Чтобы использовать этого бота введите код приглашения, либо пройдите по реферальной ссылке!\n'
                             )
