from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import buy_callback

start_choice = InlineKeyboardMarkup(row_width=2)

all_item = InlineKeyboardButton(text="Выбери свое чудо", callback_data="assortment_cart_button")
start_choice.insert(all_item)

shopping_cart = InlineKeyboardButton(text="Корзина", callback_data="shopping_cart_button")
start_choice.insert(shopping_cart)

cancel_button = InlineKeyboardButton(text="Реферальная программа", callback_data="referal_button")
start_choice.insert(cancel_button)

cancel_button = InlineKeyboardButton(text="Help", callback_data="help_button")
start_choice.insert(cancel_button)


