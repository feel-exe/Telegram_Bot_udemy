from sqlalchemy import Integer, Column, BigInteger, String, sql

from utils.db_api.db_gino import TimedBaseModel


class Referral(TimedBaseModel):
    __tablename__ = 'referrals'
    user_id = Column(BigInteger, primary_key=True)
    user_name = Column(String(100))
    balance = Column(Integer(), default=0)

    query: sql.Select
