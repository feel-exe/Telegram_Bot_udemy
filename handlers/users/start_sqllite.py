import sqlite3

from aiogram.dispatcher.filters import CommandStart
from aiogram import types
import re

from aiogram.utils.deep_linking import get_start_link

from filters import IsPrivate
from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    # name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id, name=message.from_user.full_name, )
    except sqlite3.IntegrityError as err:
        print(err)
