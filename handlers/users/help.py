import logging
from aiogram import types
from aiogram.dispatcher.filters import Command, CommandHelp
from aiogram.types import Message, CallbackQuery

from data.config import admins
from keyboards.inline.callback_datas import menu_callback
from keyboards.inline.help_button import help_choice
from keyboards.inline.menu_button import menu_choice
from loader import dp


@dp.callback_query_handler(text_contains="help_button", user_id=admins)
async def call_help_admins(call: CallbackQuery):
    text = [
        "H E L P             H E L P",
        "Здесь много всего из разных уголков мира",
        "Приятного тебе выбора\n\n",
        "КАК ИСКАТЬ",
        "По кнопке ВЫБРАТЬ будут доступны все чудеса\n",
        "РЕФЕРАЛЬНАЯ ПРОГРАММА",
        "Ты получаешь бонус к покупке когда приглашаешь друга",
        "просто отправь ему ссылку-приглашение\n\n",
        "ТОВАРЫ",
        "администраторы могут добавлять и удалять товары из списка",
        "для этого есть кнопки ДОБАВИТЬ и УДАЛИТЬ\n\n",
        "РЕФЕРАЛЬНАЯ ПРОГРАММА",
        "можно устраивать ивенты с приглашением новых пользователе",
        "для этого просто сгенерируй invite code"

    ]
    await call.message.answer('\n\n'.join(text),
                              reply_markup=help_choice)


@dp.message_handler(CommandHelp(), user_id=admins)
async def message_help_admins(message: types.Message):
    text = [
        "H E L P             H E L P",
        "Здесь много всего из разных уголков мира",
        "Приятного тебе выбора\n\n",
        "КАК ИСКАТЬ",
        "По кнопке ВЫБРАТЬ будут доступны все чудеса\n",
        "РЕФЕРАЛЬНАЯ ПРОГРАММА",
        "Ты получаешь бонус к покупке когда приглашаешь друга",
        "просто отправь ему ссылку-приглашение\n\n",
        "ТОВАРЫ",
        "администраторы могут добавлять и удалять товары из списка",
        "для этого есть кнопки ДОБАВИТЬ и УДАЛИТЬ\n\n",
        "РЕФЕРАЛЬНАЯ ПРОГРАММА",
        "можно устраивать ивенты с приглашением новых пользователе",
        "для этого просто сгенерируй invite code"
    ]
    await message.answer('\n\n'.join(text),
                              reply_markup=help_choice)


@dp.callback_query_handler(text_contains="help_button")
async def call_help_users(call: CallbackQuery):
    text = [
        "H E L P             H E L P",
        "Здесь много всего из разных уголков мира",
        "Приятного тебе выбора\n\n",
        "КАК ИСКАТЬ",
        "По кнопке ВЫБРАТЬ будут доступны все чудеса\n",
        "РЕФЕРАЛЬНАЯ ПРОГРАММА",
        "Ты получаешь бонус к покупке когда приглашаешь друга",
        "просто отправь ему ссылку-приглашение\n\n"
    ]
    await call.message.answer('\n\n'.join(text),
                              reply_markup=help_choice)


@dp.message_handler(CommandHelp())
async def message_help_users(message: types.Message):
    text = [
        "H E L P             H E L P",
        "Здесь много всего из разных уголков мира",
        "Приятного тебе выбора\n\n",
        "КАК ИСКАТЬ",
        "По кнопке ВЫБРАТЬ будут доступны все чудеса\n",
        "РЕФЕРАЛЬНАЯ ПРОГРАММА",
        "Ты получаешь бонус к покупке когда приглашаешь друга",
        "просто отправь ему ссылку-приглашение\n\n"
    ]
    await message.answer('\n\n'.join(text),
                              reply_markup=help_choice)
