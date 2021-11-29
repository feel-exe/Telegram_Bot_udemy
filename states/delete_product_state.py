from aiogram.dispatcher.filters.state import StatesGroup, State


class DeleteList(StatesGroup):

    # название товара
    DL_name = State()

    # Подтврждение удаления
    DL_yes_no = State()
