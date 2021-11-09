from aiogram.dispatcher.filters import CommandStart
from aiogram import types
import re
import asyncpg.exceptions

from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start_deep_link(message: types.Message):
    try:
        user = await db.add_user(
            full_name=message.from_user.full_name,
            username=message.from_user.username,
            telegram_id=message.from_user.id
        )
    except asyncpg.exceptions.UniqueViolationError:
        user = db.select_user(telegram_id=message.from_user.id)

    count_users = await db.count_users()

    user_data = list(user)
    user_data_dict = dict(user)

    username = user.get("username")
    full_name = user[2]

    await message.answer("\n".join(
            [
                f'Привет, {message.from_user.full_name}!',
                f'Ты был занесен в базу',
                f'В базе <b>{count_users}</b> пользователей',
                "",
                f"<code>User: {username} - {full_name}",
                f"{user_data=}",
                f"{user_data_dict=}</code>"
            ]))
