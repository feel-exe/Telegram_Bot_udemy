from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.admins import Admin


async def add_admin(admin_id: int, admin_full_name: str = None):
    try:
        admin = Admin(admin_id=admin_id, admin_full_name=admin_full_name)
        await admin.create()

    except UniqueViolationError:
        pass


async def select_all_users():
    admins = await Admin.query.gino.all()
    return admins


async def select_user(id: int):
    admin = await Admin.query.where(Admin.admin_id == id).gino.first()
    return admin


async def count_users():
    total = await db.func.count(Admin.admin_id).gino.scalar()
    return total
