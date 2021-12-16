from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.product import Product


async def add_product(name_product: str, specification_product: str = None, price_product: float = 0,
                      cash_photo_product: str = None):
    try:
        product = Product(name_product=name_product, specification_product=specification_product,
                          price_product=price_product, cash_photo_product=cash_photo_product)
        await product.create()

    except UniqueViolationError:
        pass


async def select_all_products():
    products = await Product.query.gino.all(order_by=Product.name_product)
    return products


async def check_product(name_product: int):
    product = await Product.query.where(Product.name_product == name_product).gino.first()
    if product is not None:
        return True
    else:
        return False


async def select_sort_all_products():
    products_list = await Product.query.order_by(Product.name_product).gino.all()
    return products_list


async def select_product(name_product: str):
    product = await Product.query.where(Product.name_product == name_product).gino.first()
    return product


async def count_products():
    total = await db.func.count(Product.name_product).gino.scalar()
    return total


async def delete_product(name_product: int):
    product = await Product.query.where(Product.name_product == name_product).gino.first()
    await product.delete()



def select_sort_all_products_test():
    products_list = Product.query.order_by(Product.name_product).gino.all()
    return products_list
