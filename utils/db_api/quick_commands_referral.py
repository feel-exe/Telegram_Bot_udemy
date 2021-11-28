from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.referral_program import Referral


async def add_referral(referer_id: int, referer_first_name: str = None, referer_last_name: str = None, balance: float = None):
    try:
        referral = Referral(referer_id=referer_id, referer_first_name=referer_first_name,
                            referer_last_name=referer_last_name, balance=0)
        await referral.create()

    except UniqueViolationError:
        pass


async def select_all_referrals():
    referral = await Referral.query.gino.all()
    return referral


async def select_referal(referer_id: int):
    referral = await Referral.query.where(Referral.referer_id == referer_id).gino.first()
    return referral


async def count_referral():
    total = await db.func.count(Referral.user_id).gino.scalar()
    return total


bonus = 10


async def update_referral_balance(referer_id, bonus: float = bonus):
    referral = await Referral.get(referer_id)
    old_balance = referral.balance
    new_balance = old_balance + bonus

    await referral.update(balance=+new_balance).apply()
