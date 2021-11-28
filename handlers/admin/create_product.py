from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ContentType
from data.config import admins

from loader import dp
from states.add_product_state import InventoryList

from utils.db_api import quick_commands_product as command_product


@dp.message_handler(Command("additem"), state=None, user_id=admins)
async def enter_test(message: types.Message):
    await message.answer("Вы ициализировали добавление товара\n\n"
                         "Введите название товара")

    await InventoryList.IL_name.set()


@dp.message_handler(state=InventoryList.IL_name, user_id=admins)
async def answer_IL_name(message: types.Message, state: FSMContext):
    product_name = message.text
    await state.update_data(
        {"product_name": product_name}
    )

    data = await state.get_data()
    product_name = data.get("product_name")

    await message.answer("Текущее состояние: \n"
                         f"1. product_name:           {product_name} \n\n"
                         "Введите описание товара: ")

    await InventoryList.IL_specification.set()


@dp.message_handler(state=InventoryList.IL_specification, user_id=admins)
async def answer_IL_specification(message: types.Message, state: FSMContext):
    product_specification = message.text
    await state.update_data(
        {"product_specification": product_specification}
    )

    data = await state.get_data()
    product_name = data.get("product_name")
    product_specification = data.get("product_specification")

    await message.answer("Текущее состояние: \n"
                         f"1. product_name:           {product_name} \n"
                         f"2. product_specification:  {product_specification} \n\n"
                         "Установите цену: ")

    await InventoryList.IL_price.set()


@dp.message_handler(state=InventoryList.IL_price, user_id=admins)
async def answer_IL_specification(message: types.Message, state: FSMContext):
    product_price = message.text
    try:
        product_price = float(product_price)
    except:
        product_price = product_price.replace(",", ".")
        product_price = float(product_price)

    await state.update_data(
        {"product_price": product_price}
    )

    data = await state.get_data()
    product_name = data.get("product_name")
    product_specification = data.get("product_specification")
    product_price = data.get("product_price")

    await message.answer("Текущее состояние: \n"
                         f"1. product_name:           {product_name} \n"
                         f"2. product_specification:  {product_specification} \n"
                         f"3. product_price:          {product_price} \n\n"
                         "Установите фотокарточку товара: ")

    await InventoryList.IL_foto.set()


# @dp.message_handler()
@dp.message_handler(state=InventoryList.IL_foto, content_types=ContentType.PHOTO, user_id=admins)
async def answer_IL_photo(message: types.Message, state: FSMContext):
    # async def answer_IL_specification(message: types.Message):
    await message.photo[-1].download()

    await state.update_data(
        {"product_foto_id": message.photo[-1].file_id}
    )

    data = await state.get_data()
    product_name = data.get("product_name")
    product_specification = data.get("product_specification")
    product_price = data.get("product_price")

    await message.answer("Создана карточка товара: \n"
                         f"1. product_name:           {product_name} \n"
                         f"2. product_specification:  {product_specification} \n"
                         f"3. product_price:          {product_price} \n\n"
                         f"Сохранить данные?   Y/n")

    await InventoryList.IL_yes_no.set()


@dp.message_handler(state=InventoryList.IL_yes_no, user_id=admins)
async def answer_IL_specification(message: types.Message, state: FSMContext):
    yes_no = message.text

    if yes_no.lower() == "n":
        await message.answer("Ввод обнулен \n\n"
                             "Начать заново /additem")
        await state.finish()

    if yes_no.lower() == "y":
        data = await state.get_data()
        product_name = data.get("product_name") 
        product_specification = data.get("product_specification")
        product_price = data.get("product_price")
        product_foto_id = data.get("product_foto_id")

        await command_product.add_product(name_product=product_name, specification_product=product_specification,
                                          price_product=float(product_price), cash_photo_product=product_foto_id)

        await message.answer("Товар внесен в БД")
        await state.finish()
