from sqlalchemy import Integer, Column, BigInteger, String, sql, FLOAT

from utils.db_api.db_gino import TimedBaseModel


class Product(TimedBaseModel):
    __tablename__ = 'products'
    name_pr = Column(String(100), primary_key=True)
    specification_pr = Column(String(100))
    price_pr = Column(FLOAT(precision=6))
    photo_pr = Column(String(100))

    query: sql.Select
