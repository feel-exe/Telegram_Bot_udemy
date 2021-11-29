from aiogram.dispatcher.filters import CommandStart, Command
from aiogram import types
import re

from aiogram.types import CallbackQuery
from asyncpg import UniqueViolationError

from keyboards.inline.menu_button import menu_choice
from keyboards.inline.referal_button import referer_choice
from loader import db

from aiogram.utils.deep_linking import get_start_link
from gino.dialects import asyncpg

from filters import IsPrivate
from loader import dp

from utils.db_api import quick_commands_referral as command_referral
from utils.db_api import quick_commands_user as command_user


# находимся в разделе реферальной программы
@dp.callback_query_handler(text_contains="referal_button")
async def call_help_admins(call: CallbackQuery):
    await call.answer(cache_time=30)
    text = ["РЕФЕРАЛЬНАЯ ПРОГРАММА \n"
            "Пригаси друга и получи бонус на покупку\n\n"
            ]
    await call.message.answer('\n\n'.join(text),
                              reply_markup=referer_choice)


# генерируем deep_link ссылку через кнопку
@dp.callback_query_handler(text_contains="participation_referer")
async def call_help_admins(call: CallbackQuery):
    await call.answer(cache_time=30)
    deep_link = await get_start_link(payload=f"{call.from_user.id}")
    await command_referral.add_referral(referer_id=call.from_user.id,
                                        referer_first_name=str(call.from_user.first_name),
                                        referer_last_name=str(call.from_user.last_name))
    await call.message.answer(f"Привет! \n"
                              f"Заходи в магазин по ссылке \n\n"
                              f"{deep_link}")


@dp.callback_query_handler(text_contains="check_balance")
async def call_help_admins(call: CallbackQuery):
    await call.answer(cache_time=30)
    user_balance = await command_referral.check_referral_balance(referer_id=call.from_user.id)
    await call.message.answer(f"Твой баланс \n\n"
                              f"{user_balance} у.е.")


# # генерируем deep_link ссылку
# @dp.message_handler(Command("invite"))
# async def bot_start(message: types.Message):
#     deep_link = await get_start_link(payload=f"{message.from_user.id}")
#     await command_referral.add_referral(referer_id=message.from_user.id,
#                                         referer_first_name=str(message.from_user.first_name),
#                                         referer_last_name=str(message.from_user.last_name))
#     await message.answer(f"Привет! \n"
#                          f"Заходи в магазин по ссылке \n\n"
#                          f"{deep_link}")


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
                             reply_markup=menu_choice)


    except UniqueViolationError:
        await message.answer(f'Привет, {message.from_user.full_name}!\n\n'
                             f'Чтобы использовать этого бота введите код приглашения, либо пройдите по реферальной ссылке!\n'
                             )
