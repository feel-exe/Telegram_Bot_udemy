from .private_chat import IsPrivate
# from .test_filter import SomeF
from loader import dp

if __name__ == "filters":
    dp.filters_factory.bind(IsPrivate)
