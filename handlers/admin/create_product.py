from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ContentType, CallbackQuery
from data.config import admins
from keyboards.inline.menu_button import menu_choice_admins

from loader import dp, bot
from states.add_product_state import InventoryList
from states.delete_product_state import DeleteList

from utils.db_api import quick_commands_product as command_product


@dp.callback_query_handler(text_contains="delete_item_button", state=None, user_id=admins)
async def call_delete_item_admins(call: CallbackQuery):
    await call.answer(cache_time=30)
    text = [
        "Введи точное название товара\n"
        "который хочешь удалить"
    ]
    await call.message.answer('\n\n'.join(text))

    await DeleteList.DL_name.set()


@dp.message_handler(state=DeleteList.DL_name, user_id=admins)
async def answer_DL_name(message: types.Message, state: FSMContext):
    product_name = message.text
    product_for_delete = await command_product.select_product(name_product=product_name)
    if product_for_delete.name_product == product_name:
        # await command_product.select_product(name_product=product_name)
        product_for_delete = await command_product.select_product(name_product=product_name)
        data_del = await state.get_data()
        product_name = data_del.get("product_name")
        product_name = product_for_delete.name_product
        product_specification = product_for_delete.specification_product
        product_price = product_for_delete.price_product
        product_foto_id = product_for_delete.cash_photo_product

        await bot.send_photo(chat_id=message.from_user.id,
                             photo=product_foto_id,
                             caption="Создана карточка товара: \n\n"
                                     f"НАЗВАНИЕ:   {product_name} \n"
                                     f"ОПИСАНИЕ:   {product_specification} \n"
                                     f"ЦЕНА:       {product_price} \n\n"
                                     f"Удалить?   Y/n")
        await DeleteList.DL_yes_no.set()
    else:
        await message.answer("По названию товар не найден",
                             reply_markup=menu_choice_admins)
        await state.finish()


@dp.message_handler(state=DeleteList.DL_yes_no, user_id=admins)
async def answer_DL_specification(message: types.Message, state: FSMContext):
    yes_no = message.text

    if yes_no.lower() == "n":
        await message.answer("Не удален)",
                             reply_markup=menu_choice_admins)
        await state.finish()

    if yes_no.lower() == "y":
        data_del = await state.get_data()
        product_name = data_del.get("product_name")

        await command_product.delete_product(name_product=product_name)

        await message.answer("Товар удален",
                             reply_markup=menu_choice_admins)
        await state.finish()


@dp.callback_query_handler(text_contains="add_item_button", state=None, user_id=admins)
async def call_add_item_admins(call: CallbackQuery):
    await call.answer(cache_time=30)
    text = [
        f" {call.from_user.first_name}\n\n"
        "Вы ициализировали добавление товара\n\n"
        "Введите НАЗВАНИЕ товара"
    ]
    await call.message.answer('\n\n'.join(text))
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
    product_foto_id = data.get("product_foto_id")

    # await message.answer(text="Создана карточка товара: \n"
    #                      f"{product_name} \n"
    #                      f"{product_specification} \n"
    #                      f"{product_price} \n\n"
    #                      f"Сохранить?   Y/n", )

    await bot.send_photo(chat_id=message.from_user.id,
                         photo=product_foto_id,
                         caption="Создана карточка товара: \n\n"
                                 f"НАЗВАНИЕ:   {product_name} \n"
                                 f"ОПИСАНИЕ:   {product_specification} \n"
                                 f"ЦЕНА:       {product_price} \n\n"
                                 f"Сохранить?   Y/n")

    # await dp.send_photo(chat_id=message.chat_id,
    #                     text="Создана карточка товара: \n"
    #                          f"{product_name} \n"
    #                          f"{product_specification} \n"
    #                          f"{product_price} \n\n"
    #                          f"Сохранить?   Y/n", )

    await InventoryList.IL_yes_no.set()


@dp.message_handler(state=InventoryList.IL_yes_no, user_id=admins)
async def answer_IL_specification(message: types.Message, state: FSMContext):
    yes_no = message.text

    if yes_no.lower() == "n":
        await message.answer("Ввод остановлен",
                             reply_markup=menu_choice_admins)
        await state.finish()

    if yes_no.lower() == "y":
        data = await state.get_data()
        product_name = data.get("product_name")
        product_specification = data.get("product_specification")
        product_price = data.get("product_price")
        product_foto_id = data.get("product_foto_id")

        await command_product.add_product(name_product=product_name, specification_product=product_specification,
                                          price_product=float(product_price), cash_photo_product=product_foto_id)

        await message.answer("Товар добавлен в лист товаров",
                             reply_markup=menu_choice_admins)
        await state.finish()
