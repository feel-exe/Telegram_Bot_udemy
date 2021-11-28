from aiogram.utils.callback_data import CallbackData

menu_callback = CallbackData("level", "sub_level")
buy_callback = CallbackData("level", "sub_level", "buy", "item_name", "quantity")
