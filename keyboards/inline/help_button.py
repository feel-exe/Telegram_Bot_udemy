from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import menu_callback

help_choice = InlineKeyboardMarkup(row_width=2)

back_help = InlineKeyboardButton(text="Back", callback_data=menu_callback.new(sub_level="menu"))
help_choice.insert(back_help)

