from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.add_product_state import InventoryList


# Сделаем фильтр на комманду /test, где не будет указано никакого состояния
@dp.message_handler(Command("additem"), state=None)
async def enter_test(message: types.Message):
    await message.answer("Вы ициализировали добавление товара.\n\n"
                         "Введите название товара")

    await InventoryList.IL_name.set()
    print("enter_test")

@dp.message_handler(state=InventoryList.IL_name)
async def answer_IL_name(message: types.Message, state: FSMContext):
    product_name = message.text
    await state.update_data(
        {"product_name": product_name}
    )

    data = await state.get_data()
    product_name = data.get("product_name")

    await message.answer("Текущее состояние: \n"
                         f"1. product_name: {product_name} \n\n"
                         "Введите описание товара: ")

    await InventoryList.IL_specification.set()
    print("answer_IL_name")

@dp.message_handler(state=InventoryList.IL_specification)
async def answer_IL_specification(message: types.Message, state: FSMContext):
    product_specification = message.text
    await state.update_data(
        {"product_specification": product_specification}
    )

    data = await state.get_data()
    product_name = data.get("product_name")
    product_specification = data.get("product_specification")

    await message.answer("Текущее состояние: \n"
                         f"1. product_name: {product_name} \n"
                         f"2. product_specification: {product_specification} \n\n"
                         "Установите цену: ")

    await InventoryList.IL_price.set()


@dp.message_handler(state=InventoryList.IL_price)
async def answer_IL_specification(message: types.Message, state: FSMContext):
    product_price = message.text
    await state.update_data(
        {"product_price": product_price}
    )

    data = await state.get_data()
    product_name = data.get("product_name")
    product_specification = data.get("product_specification")
    product_price = data.get("product_price")

    await message.answer("Текущее состояние: \n"
                         f"1. product_name: {product_name} \n"
                         f"2. product_specification: {product_specification} \n"
                         f"3. product_price: {product_price} \n\n"
                         "Установите фотокарточку товара: ")

    await InventoryList.IL_foto.set()


@dp.message_handler(state=InventoryList.IL_foto)
async def answer_IL_specification(message: types.Message, state: FSMContext):
    # product_foto = message.uploadMedia
    product_foto = message.text
    await state.update_data(
        {"product_foto": product_foto}
    )

    data = await state.get_data()
    product_name = data.get("product_name")
    product_specification = data.get("product_specification")
    product_price = data.get("product_price")
    product_foto = data.get("product_foto")

    await message.answer("Создана карточка товара: \n"
                         f"1. product_name: {product_name} \n"
                         f"2. product_specification: {product_specification} \n"
                         f"3. product_price: {product_price} \n"
                         f"3. product_foto: {product_foto} \n")

    """
    требуется написать фгкция по добавлению параметров товара в pgsql
    """


    await state.finish()



