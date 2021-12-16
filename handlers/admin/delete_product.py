from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType, CallbackQuery
from data.config import admins
from keyboards.inline.menu_button import menu_choice_admins

from loader import dp, bot

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

    if await command_product.select_product(name_product=product_name) is None:
        await message.answer("По такому названию ничего не найдено\n"
                             "Уточни НАЗВАНИЕ ТОВАРА)",
                             reply_markup=menu_choice_admins)
        await state.finish()

    if await command_product.select_product(name_product=product_name) is not None:
        product_for_delete = await command_product.select_product(name_product=product_name)

        product_name = product_for_delete.name_product
        product_specification = product_for_delete.specification_product
        product_price = product_for_delete.price_product
        product_foto_id = product_for_delete.cash_photo_product

        await state.update_data(
            {"product_name": product_name}
        )

        await bot.send_photo(chat_id=message.from_user.id,
                             photo=product_foto_id,
                             caption=f"НАЗВАНИЕ:   {product_name} \n"
                                     f"ОПИСАНИЕ:   {product_specification} \n"
                                     f"ЦЕНА:       {product_price} \n\n"
                                     f"Удалить?   Y/n")
        await DeleteList.DL_yes_no.set()


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
