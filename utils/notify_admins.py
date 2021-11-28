import logging

from aiogram import Dispatcher

from data.config import admins
from utils.db_api import quick_commands_user as quick_user
from utils.db_api import quick_commands_admin as quick_admin


async def on_startup_notify(dp: Dispatcher):
    for admin in admins:
        try:
            await dp.bot.send_message(admin, "Бот Запущен и готов к работе с FSM!")

        except Exception as err:
            logging.exception(err)


async def on_add_admins_in_bd():
    for admin in admins:
        try:
            await quick_user.add_user(user_id=admin)

        except Exception as err:
            logging.exception(err)

        try:
            await quick_admin.add_admin(admin_id=admin)

        except Exception as err:
            logging.exception(err)
