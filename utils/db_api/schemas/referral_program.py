from sqlalchemy import Integer, Column, BigInteger, String, sql, Float

from utils.db_api.db_gino import TimedBaseModel


class Referral(TimedBaseModel):
    __tablename__ = 'referrals'
    referer_id = Column(BigInteger, primary_key=True)
    referer_first_name = Column(String(100))
    referer_last_name = Column(String(100))
    balance = Column(Float(precision=6), default=0.0)

    query: sql.Select
