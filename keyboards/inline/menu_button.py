from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import menu_callback

# menu user
menu_choice = InlineKeyboardMarkup(row_width=2)

store_button = InlineKeyboardButton(text="Выбери свое чудо",
                                    callback_data=menu_callback.new(sub_level="store_button"))
menu_choice.insert(store_button)

# shopping_cart_button = InlineKeyboardButton(text="Корзина",
#                                             callback_data=menu_callback.new(sub_level="shopping_button"))
# menu_choice.insert(shopping_cart_button)

referal_button = InlineKeyboardButton(text="Реферальная программа",
                                      callback_data=menu_callback.new(sub_level="referal_button"))
menu_choice.insert(referal_button)

help_button = InlineKeyboardButton(text="Help", callback_data=menu_callback.new(sub_level="help_button"))
menu_choice.insert(help_button)


# menu admin
menu_choice_admins = InlineKeyboardMarkup(row_width=2)

store_button = InlineKeyboardButton(text="Выбери свое чудо",
                                    callback_data=menu_callback.new(sub_level="store_button"))
menu_choice_admins.insert(store_button)

# shopping_cart_button = InlineKeyboardButton(text="Корзина",
#                                             callback_data=menu_callback.new(sub_level="shopping_button"))
# menu_choice_admins.insert(shopping_cart_button)

referal_button = InlineKeyboardButton(text="Реферальная программа",
                                      callback_data=menu_callback.new(sub_level="referal_button"))
menu_choice_admins.insert(referal_button)

help_button = InlineKeyboardButton(text="Help", callback_data=menu_callback.new(sub_level="help_button"))
menu_choice_admins.insert(help_button)

add_item_button = InlineKeyboardButton(text="Добавить товар*",
                                       callback_data=menu_callback.new(sub_level="add_item_button"))
menu_choice_admins.insert(add_item_button)

delete_item_button = InlineKeyboardButton(text="Удалить товар*",
                                          callback_data=menu_callback.new(sub_level="delete_item_button"))
menu_choice_admins.insert(delete_item_button)


# add_admin_button = InlineKeyboardButton(text="Добавить АДМИНИСТРАТОРА",
#                                        callback_data=menu_callback.new(sub_level="add_admin_button"))
# menu_choice_admins.insert(add_item_button)

invete_code_button = InlineKeyboardButton(text="Получить invite code*",
                                          callback_data=menu_callback.new(sub_level="invete_code_button"))
menu_choice_admins.insert(invete_code_button)
