from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import menu_callback

buy_item_choice = InlineKeyboardMarkup(row_width=2)

next_button = InlineKeyboardButton(text="NEXT", callback_data=menu_callback.new(sub_level="next_button"))
buy_item_choice.insert(next_button)

cancel_button = InlineKeyboardButton(text="Отмена", callback_data=menu_callback.new(sub_level="cancel_button"))
buy_item_choice.insert(cancel_button)

pay_item_choice_ = InlineKeyboardMarkup(row_width=2)
pay_button = InlineKeyboardButton(text="Оплатить", callback_data=menu_callback.new(sub_level="pay_button"))
buy_item_choice.insert(pay_button)

cancel_button = InlineKeyboardButton(text="Отмена", callback_data=menu_callback.new(sub_level="cancel_button"))
buy_item_choice.insert(cancel_button)
