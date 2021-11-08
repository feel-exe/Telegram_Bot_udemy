from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.product import Product


async def add_product(id: int, name: str, email: str = None):
    try:
        user = Product(id=id, name=name, email=email)
        await user.create()

    except UniqueViolationError:
        pass


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def select_user(id: int):
    user = await User.query.where(User.id == id).gino.first()
    return user


async def count_users():
    total = await db.func.count(User.id).gino.scalar()
    return total


async def update_user_email(id, email):
    user = await User.get(id)
    await user.update(email=email).apply()