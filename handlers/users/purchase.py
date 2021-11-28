import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.start_button import start_choice
from loader import dp


@dp.message_handler(Command("items"))
async def show_items(message: Message):
    await message.answer(text="Велком ту ",
                         reply_markup=start_choice)


# # Попробуйем отловить по встроенному фильтру, где в нашем call.data содержится "pear"
# @dp.callback_query_handler(text_contains="pear")
# async def buying_pear(call: CallbackQuery):
#     # Обязательно сразу сделать answer, чтобы убрать "часики" после нажатия на кнопку.
#     # Укажем cache_time, чтобы бот не получал какое-то время апдейты, тогда нижний код не будет выполняться.
#     await call.answer(cache_time=60)
#
#     callback_data = call.data
#
#     # Отобразим что у нас лежит в callback_data
#     # logging.info(f"callback_data='{callback_data}'")
#     # В питоне 3.8 можно так
#     logging.info(f"{callback_data=}")
#
#     await call.message.answer("Вы выбрали купить грушу. Груша всего одна. Спасибо.",
#                               reply_markup=pear_keyboard)
#
#
# # Попробуем использовать фильтр от CallbackData
# @dp.callback_query_handler(buy_callback.filter(item_name="apple"))
# async def buying_apples(call: CallbackQuery, callback_data: dict):
#     await call.answer(cache_time=60)
#
#     # Выведем callback_data и тут, чтобы сравнить с предыдущим вариантом.
#     logging.info(f"{callback_data=}")
#
#     quantity = callback_data.get("quantity")
#     await call.message.answer(f"Вы выбрали купить яблоки. Яблок всего {quantity}. Спасибо.",
#                               reply_markup=apples_keyboard)
#
#
# @dp.callback_query_handler(text="cancel")
# async def cancel_buying(call: CallbackQuery):
#     await call.answer("Вы отменили эту покупку!", show_alert=True)
#
#     await call.message.edit_reply_markup(reply_markup=None)
