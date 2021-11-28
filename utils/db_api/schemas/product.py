from sqlalchemy import Integer, Column, BigInteger, String, sql, FLOAT

from utils.db_api.db_gino import TimedBaseModel


class Product(TimedBaseModel):
    __tablename__ = 'products'
    name_product = Column(String(100), primary_key=True)
    specification_product = Column(String(100))
    price_product = Column(FLOAT(precision=6))
    cash_photo_product = Column(String(100))

    query: sql.Select
