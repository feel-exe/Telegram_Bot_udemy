from loader import dp, bot
from aiogram.types import ContentType, Message


@dp.message_handler(content_types=ContentType.PHOTO)
async def catch_photo(message: Message):
    await message.photo[-1].download()
    print(message.photo[-1].download())
    await message.reply(
        "Фотография скачана\n"
        f"<pre>FILE ID = {message.photo[-1].file_id}</pre>")

    await message.reply({message.photo[-1].file_id})
