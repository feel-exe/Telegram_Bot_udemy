from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.product import Product


async def add_product(name_pr: str, specification_pr: str = None, price_pr: float = 0, photo_pr: str = None):
    try:
        product = Product(name_pr=name_pr, specification_pr=specification_pr, price_pr=price_pr, photo_pr=photo_pr)
        await product.create()

    except UniqueViolationError:
        pass


async def select_all_products():
    products = await Product.query.gino.all()
    return products


async def select_product(name_pr: int):
    product = await Product.query.where(Product.name_pr == name_pr).gino.first()
    return product


async def count_products():
    total = await db.func.count(Product.name_pr).gino.scalar()
    return total


async def update_product_specification(name_pr, specification_pr):
    product = await Product.get(name_pr)
    await product.update(specification_pr=specification_pr).apply()


async def update_product_price(name_pr, price_pr):
    product = await Product.get(name_pr)
    await product.update(price_pr=price_pr).apply()


async def update_product_photo(name_pr, photo_pr):
    product = await Product.get(name_pr)
    await product.update(photo_pr=photo_pr).apply()
