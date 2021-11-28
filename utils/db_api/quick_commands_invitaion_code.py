import random

from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.invitation_code import InvitationCode








async def generate_referral_code(invitation_code_id: int):
    # user_name добавлен для колличества столбцов. в будущем будет связанный запрос в БД
    try:
        invitation_code = InvitationCode(invitation_code_id=invitation_code_id)
        await invitation_code.create()

    except UniqueViolationError:
        pass


async def select_all_referral_code():
    invitation_code = await InvitationCode.query.gino.all()
    return invitation_code


async def select_referral_code(user_id: int):
    invitation_code = await InvitationCode.query.where(InvitationCode.user_id == user_id).gino.first()
    return invitation_code


async def count_referral_code():
    total = await db.func.count(InvitationCode.user_id).gino.scalar()
    return total
