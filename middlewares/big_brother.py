from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types
from data.config import banned_users
import logging
from aiogram.dispatcher.handler import CancelHandler


class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        logging.info("[--------Новый аплейт---------")
        logging.info("1. Pre Process Update")
        logging.info("Следующая точка: Process Update ")
        data["middleware_data"] = 'это пройдет до on_post_process_update'
        if update.message:
            user = update.message.from_user.id
        elif update.callback_query:
            user = update.callback_query.from_user.id
        else:
            return

        if user in banned_users:
            raise CancelHandler()



    async def on_process_update(self, update: types.Update, data: dict):
        logging.info(f"2. Pre Process Update, {data}")
        logging.info("Следующая точка: PreProcess Message ")
        data["middleware_data"] = 'это пройдет до on_post_process_update'

    async def on_process_message(self, update: types.Message, data: dict):
        logging.info(f"3. Pre Process Update, {data}")
        logging.info("Следующая точка: Fisters ")
        data["middleware_data"] = 'это пройдет до on_process_message'
