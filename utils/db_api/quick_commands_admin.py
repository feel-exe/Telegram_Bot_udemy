from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.admins import Admin


async def add_admin(id: int, name: str, email: str = None):
    try:
        admin = Admin(id=id, name=name, email=email)
        await admin.create()

    except UniqueViolationError:
        pass


async def select_all_users():
    admins = await Admin.query.gino.all()
    return admins


async def select_user(id: int):
    admin = await Admin.query.where(Admin.id == id).gino.first()
    return admin


async def count_users():
    total = await db.func.count(Admin.id).gino.scalar()
    return total
