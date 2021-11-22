from aiogram.dispatcher.filters import CommandStart, Command
from aiogram import types
import re

from asyncpg import UniqueViolationError

from loader import db

from aiogram.utils.deep_linking import get_start_link
from gino.dialects import asyncpg

from filters import IsPrivate
from loader import dp

from utils.db_api import quick_commands_referral as command_referral


# генерируем deep_link ссылку
@dp.message_handler(Command("invite"))
async def bot_start(message: types.Message):
    deep_link = await get_start_link(payload=f"{message.from_user.id}")
    await message.answer(f"Привет! \n"
                         f"Заходи в магазин по ссылке \n\n"
                         f"{deep_link}")

    await command_referral.add_referral(user_id=str(message.from_user.id), user_name=str(message.from_user.full_name))


# ловим deep_link ссылку
# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     # bot_username = await dp.bot.me()
#     # deep_link = f"https://t.me/{bot_username.username}?start=123"
#
#     deep_link = await get_start_link(payload=123)
#     await message.answer(f"Привет,  {message.from_user.full_name}! \n"
#                          f"Вы находитесь в личной переписке \n"
#                          f"В вашей команде есть deep_link \n"
#                          f"Вы передали аргумент {deep_link}")


# Этот хендлер используется для диплинков:
@dp.message_handler(CommandStart(deep_link=re.compile(r"^[0-9]{4,15}$")))
async def bot_start_deeplink(message: types.Message):
    # С помощью функции get_args забираем аргументы после команды start. (для примера выше - будет "123")

    deep_link_args = message.get_args()

    print(type(deep_link_args))
    print(type(message.from_user.id))
    try:
        user_ferrer = await command_referral.select_referral(user_id=message.from_user.id)
        print(deep_link_args)
        print(type(deep_link_args))

        print(user_ferrer.user_id)
        print(type(user_ferrer.user_id))

        print(user_ferrer.user_id == deep_link_args)

        if user_ferrer.user_id == deep_link_args:
            await message.answer(f'Привет, {message.from_user.full_name}!\n'
                                     f'Это магазин чудес. \n\n'
                                     f'Тебя пригласил {user_ferrer}. \n\n'
                                     f'Нажми /help')
        else:
            await message.answer(f'Привет, {message.from_user.full_name}!\n\n'
                                     f'Такой инвайт ссылки не существует, давай по новой!\n'
                                     )


    except UniqueViolationError:
        pass
    # try:
    #     user_ferrer = str(await command_referral.select_referral(user_id=str(message.from_user.id)))
    #     print(f"user_ferrer  {user_ferrer}")
    #     await message.answer(f'Привет, {message.from_user.full_name}!\n'
    #                          f'Это магазин чудес. \n\n'
    #                          f'Тебя пригласил {user_ferrer}. \n\n'
    #                          f'Нажми /help')
    # except:
    #     await message.answer(f'Привет, {message.from_user.full_name}!\n\n'
    #                          f'Такой инвайт ссылки не существует, давай по новой!\n'
    #                          )
# # В этом хендлере мы ловим простое нажатие на команду /start, не прошедшее под условие выше
# @dp.message_handler(CommandStart(deep_link=None), IsPrivate())
# async def bot_start(message: types.Message):
#     # Для создания диплинк-ссылки - нужно получить юзернейм бота
#     bot_user = await dp.bot.get_me()
#
#     # Формируем диплинк-ссылку
#     deep_link = f"http://t.me/{bot_user.username}?start=123"
#     await message.answer(f'Привет, {message.from_user.full_name}!\n'
#                          f'Вы находитесь в личной переписке. \n'
#                          f'В вашей команде нет диплинка.\n'
#                          f'Ваша диплинк ссылка - {deep_link}')
