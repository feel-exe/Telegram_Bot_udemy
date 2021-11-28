from sqlalchemy import Integer, Column, BigInteger, String, sql, Float

from utils.db_api.db_gino import TimedBaseModel


class InvitationCode(TimedBaseModel):
    __tablename__ = 'invitationcodes'
    invitation_code_id = Column(Integer, primary_key=True)

    query: sql.Select