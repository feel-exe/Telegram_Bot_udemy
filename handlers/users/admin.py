from filters import IsPrivate
from loader import dp
from aiogram import types


@dp.message_handler(IsPrivate(), user_id=[307136400], text="admin")
@dp.message_handler(IsPrivate(), user_id=[307136400], text="secret")
async def admin_chat_secrt(message: types.Message):
    await message.answer("Это секретное сообщение, вызванное однимизадминистраторов"
                         "в личной переписке ")
