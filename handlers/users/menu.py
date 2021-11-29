from aiogram import types
from aiogram.dispatcher.filters import Command, CommandHelp
from aiogram.types import Message, CallbackQuery

from data.config import admins
from keyboards.inline.callback_datas import menu_callback
from keyboards.inline.help_button import help_choice
from keyboards.inline.menu_button import menu_choice, menu_choice_admins
from loader import dp


@dp.callback_query_handler(text_contains="menu", user_id=admins)
async def call_menu_admins(call: CallbackQuery):
    await call.answer(cache_time=30)
    text = [
        f" {call.from_user.first_name}\n\n"
        "Вы вошли как АДМИНИСТРАТОР \n\n"
        "Вот небольшой функционал магазина\n"
        "Звездочкой ' * ' отмечен  функционал админа",
    ]
    await call.message.answer('\n\n'.join(text),
                              reply_markup=menu_choice_admins)


@dp.callback_query_handler(text_contains="menu")
async def call_menu_users(call: CallbackQuery):
    text = [
        f"Приветствую {call.from_user.first_name}\n\n"
        "Велком ту Магазин чудес\n"
        "Вот небольшой функционал магазина",
    ]
    await call.message.answer('\n\n'.join(text),
                              reply_markup=menu_choice)
