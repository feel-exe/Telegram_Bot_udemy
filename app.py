import logging

from aiogram import executor
from utils import set_default_commands
import middlewares, filters, handlers
from loader import db, dp

async def on_startup(dispatcher):
    # filters.setup(dp)

    logging.info("Создаем подключение к базе данных")
    await db.create()
    logging.info("Создаем таблицу пользователей")
    await db.create_table_users()
    logging.info("Готово")


    from utils import on_startup_notify
    await on_startup_notify(dp)
    # await set_default_commands(dp)
    try:
        db.create_table_users()
    except Exception as err:
        print(err)
    db.delete_users()

if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)




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
