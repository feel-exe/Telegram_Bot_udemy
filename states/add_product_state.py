from aiogram.dispatcher.filters.state import StatesGroup, State


class InventoryList(StatesGroup):
    # подтверждение
    IL_start = State()

    # название товара
    IL_name = State()

    # Описание товара
    IL_specification = State()

    # Цена товара
    IL_price = State()

    # Фото товара
    IL_foto = State()
