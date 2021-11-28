from sqlalchemy import Integer, Column, BigInteger, String, sql

from utils.db_api.db_gino import TimedBaseModel


class Admin(TimedBaseModel):
    __tablename__ = 'admins'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(100))

    query: sql.Select