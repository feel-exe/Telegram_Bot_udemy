from sqlalchemy import Integer, Column, BigInteger, String, sql

from utils.db_api.db_gino import TimedBaseModel


class Admin(TimedBaseModel):
    __tablename__ = 'admins'
    admin_id = Column(BigInteger, primary_key=True)
    admin_full_name = Column(String(100))

    query: sql.Select
