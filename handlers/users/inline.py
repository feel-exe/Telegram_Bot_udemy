from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, CommandStart
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from data.config import allowed_users
# from keyboards.inline.buy_button import buy_choice
from loader import dp, bot
from utils.db_api import quick_commands_referral as command_referral
from data.config import admins

from states.buy_item import Buy_Product

from utils.db_api import quick_commands_product as command_product
from utils.db_api import quick_commands_user as command_user


@dp.inline_handler(text="")
async def empty_query(query: types.InlineQuery):
    user = query.from_user.id
    if await command_user.check_user(user_id=user) is None:
        await query.answer(
            results=[],
            switch_pm_text="Бот недоступен. Подключить бота",
            switch_pm_parameter="connect_user",
            cache_time=5)
        return

    list_product = await command_product.select_sort_all_products()
    list_range = [i + 1 for i in range(len(list_product))]
    list_zip = zip(list_range, list_product)

    articles = [types.InlineQueryResultArticle(
        id=f"{iter}",
        title=item.name_product,
        description=f"   {item.price_product} у.е.",
        hide_url=False,
        input_message_content=types.InputTextMessageContent(
            message_text=f"{item.name_product}",
            parse_mode="HTML",
        )
    ) for iter, item in list_zip]

    await query.answer(articles, cache_time=3,
                       switch_pm_parameter="item")


@dp.message_handler()
async def bot_store_item(message: types.Message):
    if await command_product.select_product(name_product=message.text) is None:
        await message.answer("По такому названию ничего не найдено\n"
                             "Уточни НАЗВАНИЕ ТОВАРА)")

    if await command_product.select_product(name_product=message.text) is not None:
        product_for_buy = await command_product.select_product(name_product=message.text)

        buy_choice = InlineKeyboardMarkup()
        buy = f"buy:{product_for_buy}"
        buy_apples = InlineKeyboardButton(text="Купить", callback_data=buy)
        buy_choice.insert(buy_apples)

        await bot.send_photo(chat_id=message.chat.id,
                             photo=product_for_buy.cash_photo_product,
                             caption=(f"НАЗВАНИЕ:   {product_for_buy.name_product} \n\n"
                                      f"ОПИСАНИЕ:   {product_for_buy.specification_product} \n\n\n"
                                      f"ЦЕНА:       {product_for_buy.price_product} \n\n"),
                             reply_markup=buy_choice
                             )
        # await Buy_Product.BP_start.set()


@dp.callback_query_handler(text_contains="buy_button")
async def bot_store_button(call: CallbackQuery):
    await call.answer(cache_time=30)
    print(call.data)
    # text = [
    #     f" {call.from_user.first_name}\n\n"
    #     "Вы вошли как АДМИНИСТРАТОР \n\n"
    #     "Вот небольшой функционал магазина\n"
    #     "Звездочкой ' * ' отмечен  функционал админа",
    # ]
    # await call.message.answer('\n\n'.join(text),
    #                           reply_markup=menu_choice_admins)

# @dp.callback_query_handlers(state=Buy_Product.BP_start)
# async def select_quantity(call: CallbackQuery, state: FSMContext):
#     await call.answer(cache_time=3)
#     quantity = call.text
#     await state.update_data(
#         {"quantity": quantity}
#     )
#     await call.message.answer(text="")
