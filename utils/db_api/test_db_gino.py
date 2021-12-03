import asyncio

from data import config
from utils.db_api import quick_commands_product
from utils.db_api.db_gino import db


async def test():
    await db.set_bind(config.POSTGRES_URI)
    await db.gino.drop_all()
    await db.gino.create_all()

    print("Добавляем товары")

    await quick_commands_product.add_product(name_product="котик_4", specification_product="dfb",
                                             price_product=25425722, cash_photo_product="sdfg")

    await quick_commands_product.add_product(name_product="котик_3", specification_product="sdbs", price_product=25542,
                                             cash_photo_product="dfsg")

    await quick_commands_product.add_product(name_product="котик_1", specification_product="One", price_product=2542,
                                             cash_photo_product="email")

    await quick_commands_product.add_product(name_product="котик_2", specification_product="Vasya", price_product=7527,
                                             cash_photo_product="vv@gmail.com")

    await quick_commands_product.add_product(name_product="котик_5", specification_product="John", price_product=442,
                                             cash_photo_product="john@mail.com")
    print("Готово")

    product = await quick_commands_product.select_all_products()
    print(f"Получил всех товаров: {product}")

    count_product = await quick_commands_product.count_products()
    print(f"Всего товаров: {count_product}")

    user = await quick_commands_product.select_product(name_product="котик_1")
    print(f"Получил товар: {user}")

    await quick_commands_product.delete_product(name_product="котик_1")

    user = await quick_commands_product.select_product(name_product="котик_1")
    print(f"Получил товар: {user}")

    count_product = await quick_commands_product.count_products()
    print(f"Всего товаров: {count_product}")

    all_product = await quick_commands_product.select_sort_all_products()
    print(f"Сортированные товары   : {all_product[0]}")
    for item in all_product:
        print(item.name_product)

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
