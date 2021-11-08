from sqlalchemy import Integer, Column, BigInteger, String, sql

from utils.db_api.db_gino import TimedBaseModel


class Product(TimedBaseModel):
    __tablename__ = 'product'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(100))
    specification = Column(String(100))
    price = Column(float(100))

    referral = Column(BigInteger)

    query: sql.Select
