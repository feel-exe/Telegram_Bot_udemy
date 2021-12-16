import asyncio

from data import config
from utils.db_api import quick_commands_user as quick_commands
from utils.db_api.db_gino import db


async def test():
    await db.set_bind(config.POSTGRES_URI)
    await db.gino.drop_all()
    await db.gino.create_all()

    print("Добавляем пользователей")
    await quick_commands.add_user(1, "One", "email")
    await quick_commands.add_user(2, "Vasya", "vv@gmail.com")
    await quick_commands.add_user(3, "1", "1")
    await quick_commands.add_user(4, "1", "1")
    await quick_commands.add_user(5, "John", "john@mail.com")
    print("Готово")

    users = await quick_commands.select_all_users()
    print(f"Получил всех пользователей: {users}")

    count_users = await quick_commands.count_users()
    print(f"Всего пользователей: {count_users}")

    user = await quick_commands.select_user(user_id=5)
    print(f"Получил пользователя: {user}")

    count_product = await quick_commands.check_user(user_id=1)
    print(f"Наличие товара: {count_product}")

    count_product = await quick_commands.check_user(user_id=6)
    print(f"Наличие товара: {count_product}")

loop = asyncio.get_event_loop()
loop.run_until_complete(test())