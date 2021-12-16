from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import menu_callback

buy_choice = InlineKeyboardMarkup(row_width=1)

buy_button = InlineKeyboardButton(text="Купить", callback_data=menu_callback.new(sub_level="buy_button"))
buy_choice.insert(buy_button)
