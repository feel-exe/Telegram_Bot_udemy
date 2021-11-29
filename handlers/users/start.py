from aiogram.dispatcher.filters import CommandStart
from aiogram import types

from data.config import admins

from keyboards.inline.menu_button import menu_choice, menu_choice_admins
from loader import dp

from utils.db_api import quick_commands_referral as command_referral


@dp.message_handler(CommandStart(), user_id = admins)
async def bot_start_deep_link(message: types.Message):
    user = message.from_user.id
    try:
        await command_referral.select_referal(referer_id=user)
        await message.answer(f"Приветствую {message.from_user.first_name}\n\n"
                             "Вы вошли как АДМИНИСТРАТОР \n\n"
                             "Вот небольшой функционал магазина\n"
                             "Звездочкой ' * ' отмечен  функционал админа",
                             reply_markup=menu_choice_admins)
        return
    except:
        await message.answer("Бот недоступен. Подключить бота")
        return

@dp.message_handler(CommandStart())
async def bot_start_deep_link(message: types.Message):
    user = message.from_user.id
    try:
        await command_referral.select_referal(referer_id=user)
        await message.answer(f"Приветствую {message.from_user.first_name}\n\n"
                             "Велком ту Магазин чудес\n"
                             "Вот небольшой функционал магазина",
                             reply_markup=menu_choice)
        return
    except:
        await message.answer("Бот недоступен. Подключить бота")
        return








# нужно испольховать для реферальных ссылок
# @dp.message_handler(CommandStart(deep_link=re.compile(r"^[a-z0-9_-]{3,15}$")))
# async def bot_start(message: types.Message):
#     await message.answer("Ты нажал старт и пеедал правилный диплтнк")\

# применительно к соданию реферальных ссылок
# @dp.message_handler(CommandStart(deep_link=re.compile(r"^u[0-9_-]{4,15}$")))
# async def bot_start(message: types.Message):
#     # Реферал - кого привели
#     # Реферер - кто привел
#     referer= message.get_args()
#     await message.answer(f"Тебя привел пользователь {referer}")


# @dp.message_handler(CommandStart(deep_link=re.compile(r"^u[0-9_-]{4,15}$")))
# @dp.message_handler(CommandStart(deep_link=re.compile(r"\d\d\d")), IsPrivate())
# async def bot_start_deep_link(message: types.Message):
#     deep_link_args = message.get_args()
#     await message.answer(f"Привет,  {message.from_user.full_name}! \n"
#                          f"Вы находитесь в личной переписке \n"
#                          f"В вашей команде есть deep_link \n"
#                          f"Вы передали аргумент {deep_link_args}")
#
#
# # генерируем deep_link ссылку
# @dp.message_handler(CommandStart(), IsPrivate())
# async def bot_start(message: types.Message):
#     # bot_username = await dp.bot.me()
#     # deep_link = f"https://t.me/{bot_username.username}?start=123"
#
#     deep_link = await get_start_link(payload=123)
#     await message.answer(f"Привет,  {message.from_user.full_name}! \n"
#                          f"Вы находитесь в личной переписке \n"
#                          f"В вашей команде есть deep_link \n"
#                          f"Вы передали аргумент {deep_link}")

# @dp.message_handler(CommandStart)
# async def bot_start(message: types.Message):
#     args = message.get_args()
#     await message.answer(f"Ты нажал старт и передал аргумент: {args}")
