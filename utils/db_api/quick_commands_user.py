from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.user import User


async def add_user(user_id: int, user_first_name: str = None, user_last_name: str = None):
    try:
        user = User(user_id=user_id, user_first_name=user_first_name, user_last_name=user_last_name)
        await user.create()

    except UniqueViolationError:
        pass


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def select_user(user_id: int):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user


async def count_users():
    total = await db.func.count(User.id).gino.scalar()
    return total
