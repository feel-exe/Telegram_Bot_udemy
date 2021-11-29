from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import menu_callback

referer_choice = InlineKeyboardMarkup(row_width=2)

participation_referer = InlineKeyboardButton(text="Пригласить", callback_data=menu_callback.new(sub_level="participation_referer"))
referer_choice.insert(participation_referer)

check_balance = InlineKeyboardButton(text="Мой баланс", callback_data=menu_callback.new(sub_level="check_balance"))
referer_choice.insert(check_balance)

back_referer = InlineKeyboardButton(text="Back", callback_data=menu_callback.new(sub_level="menu"))
referer_choice.insert(back_referer)

