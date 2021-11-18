# from .big_brother import BigBrother
from .tracking_users import ACLMiddleware

from loader import dp

if __name__ == "middlewares":
    # dp.middleware.setup(BigBrother())
    dp.middleware.setup(ACLMiddleware())
