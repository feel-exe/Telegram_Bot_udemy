from aiogram.dispatcher.filters.state import StatesGroup, State


class Buy_Product(StatesGroup):
    # нажал на кнопку Купить
    BP_start = State()

    # выбрал кол-во
    BP_quantity = State()

    # Указал адрес
    BP_location = State()

    # Оплатить
    BP_pay = State()

    # Отмена покупки
    BP_cancel = State()
