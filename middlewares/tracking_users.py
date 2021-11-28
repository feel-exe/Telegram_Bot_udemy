from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from utils.db_api.schemas.user import User
# import utils.db_api.quick_commands_user as quick_commands
from utils.db_api.quick_commands_user import *


class ACLMiddleware(BaseMiddleware):
    async def setup_chat(self, data: dict, user: types.User):
        user_id = user.id
        user_first_name = user.first_name
        user_last_name = user.last_name
        user = await select_user(user_id=user_id)

        if user is None:
            await add_user(user_id=user_id, user_first_name=user_first_name, user_last_name=user_last_name)
        else:
            pass
        # await add_user(id=user_id, name = )

    async def on_pre_process_message(self, message: types.Message, data: dict):
        await self.setup_chat(data, message.from_user)

    async def on_pre_process_callback_query(self, query: types.CallbackQuery, data: dict):
        await self.setup_chat(data, query.from_user)
