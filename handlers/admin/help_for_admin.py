from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from data.config import admins
from loader import dp


@dp.message_handler(CommandHelp(), user_id=admins)
async def bot_help(message: types.Message):
    text = [
        'Список команд: ',
        '/start         - Начать диалог -',
        '/additem   - Добавить товар -',
        '/invite        - Пригасить пользователя -',
        '/help          - Получить справку -'
    ]
    await message.answer('\n\n'.join(text))
