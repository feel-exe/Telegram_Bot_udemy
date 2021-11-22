from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.referral_program import Referral




bonus = 10

async def add_referral(user_id: int, user_name: str = None, balance: float = None):
    # user_name добавлен для колличества столбцов. в будущем будет связанный запрос в БД
    try:
        referral = Referral(user_id=user_id, user_name=user_name, balance=balance)
        await referral.create()

    except UniqueViolationError:
        pass


async def select_all_referrals():
    referral = await Referral.query.gino.all()
    return referral


async def select_referral(user_id: int):
    referral = await Referral.query.where(Referral.user_id == user_id).gino.first()
    return referral


async def count_referral():
    total = await db.func.count(Referral.user_id).gino.scalar()
    return total


async def update_referral_balance(user_id, bonus: float = bonus):
    referral = await Referral.get(user_id)
    # old_balance =
    await referral.update(balance=+bonus).apply()






