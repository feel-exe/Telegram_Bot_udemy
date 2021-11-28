import logging
from aiogram import types
from aiogram.dispatcher.filters import Command, CommandHelp
from aiogram.types import Message, CallbackQuery

from data.config import admins
from keyboards.inline.callback_datas import menu_callback
from keyboards.inline.start_button import start_choice
from loader import dp


@dp.callback_query_handler(text_contains="help_button", user_id=admins)
async def call_help_admins(call: CallbackQuery):
    text = [
        'Список команд: ',
        '/start         - Начать диалог -',
        '/additem   - Добавить товар -',
        '/invite        - Пригласить пользователя по ссылке -',
        '/invitecode        - Пригласить пользователя по коду -',
        '/help          - Получить справку -'
    ]
    await call.message.answer('\n\n'.join(text))


@dp.message_handler(CommandHelp(), user_id=admins)
async def message_help_admins(message: types.Message):
    text = [
        'Список команд: ',
        '/additem   - Добавить товар -',
        '/invite        - Пригласить пользователя по ссылке -',
        '/invitecode        - Пригласить пользователя по коду -',
        '/help          - Получить справку -'
    ]
    await message.answer('\n\n'.join(text))


@dp.callback_query_handler(text_contains="help_button")
async def call_help_users(call: CallbackQuery):
    text = [
        'Список команд: ',
        '/invite        - Пригласить пользователя по ссылке -',
        '/help          - Получить справку -'
    ]
    await call.message.answer('\n\n'.join(text))


@dp.message_handler(CommandHelp())
async def message_help_users(message: types.Message):
    text = [
        'Список команд: ',
        '/invite        - Пригласить пользователя по ссылке -',
        '/help          - Получить справку -'
    ]
    await message.answer('\n\n'.join(text))
