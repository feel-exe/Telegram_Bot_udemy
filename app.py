# from utils.set_bot_commands import set_default_commands
from loader import db
from utils.db_api import db_gino


async def on_startup(dp):
    import filters
    import middlewares
    # filters.setup(dp)
    # middlewares.setup(dp)

    # from utils.notify_admins import on_startup_notify
    print("Подключаем БД")
    await db_gino.on_startup(dp)
    print("Готово")

    # print("Чистим базу")
    # await db.gino.drop_all()
    # print("Готово")

    print("Создаем таблицы")
    await db.gino.create_all()

    print("Готово")
    # await on_startup_notify(dp)
    # await set_default_commands(dp)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)










# import logging
#
# from aiogram import executor
#
# from loader import dp, db
# import middlewares, filters, handlers
# from loader import  db
#
# # from utils.notify_admins import on_startup_notify
#
#
# async def on_startup(dispatcher):
#     # Уведомляет про запуск
#     logging.info("Создаем подключение к базе данных")
#     await db.create()
#
#     try:
#         await db.drop_users()
#     except:
#         pass
#
#     logging.info("Создаем таблицу пользователей")
#     await db.create_table_users()
#     logging.info("Готово.")
#
#     # await on_startup_notify(dispatcher)
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp, on_startup=on_startup)

# from aiogram import executor
# from utils import set_default_commands
# from loader import dp
# import middlewares, filters, handlers
# from loader import db
#
# async def on_startup(dispatcher):
#     # filters.setup(dp)
#
#     from utils import on_startup_notify
#     await on_startup_notify(dp)
#     # await set_default_commands(dp)
#     try:
#         db.create_table_users()
#     except Exception as err:
#         print(err)
#     db.delete_users()
#
# if __name__ == '__main__':
#     from aiogram import executor
#     from handlers import dp
#
#     executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
