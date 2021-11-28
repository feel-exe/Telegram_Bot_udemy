from aiogram import types
from loader import dp


@dp.message_handler()
async def bot_echo(message: types.Message):
    # Получим chat_id и text
    chat_id = message.from_user.id
    text = message.text


    # Получим объект бота - вариант 3 (из модуля loader)
    from loader import bot

    # Отправим сообщение пользователю - вариант 1
    await bot.send_message(chat_id=chat_id, text=text)
