from app.models import db, Product, environment, SCHEMA

# make sure Product import is working correctly // paste in Gray's model into models directory?
from ._01_products_gear import products_gear, products_gear_imgs
from ._02_products_style import products_style, products_style_imgs
from ._03_products_cars import products_cars, products_cars_imgs
from ._04_products_tech import products_tech, products_tech_imgs
from ._05_products_shelter import products_shelter, products_shelter_imgs
from ._06_products_vices import products_vices, products_vices_imgs
from ._07_products_body import products_body, products_body_imgs
from ._08_products_etc import products_etc, products_etc_imgs


# add 05_shelter & 07_body
def seed_products():
    gear = [
        Product(
            title=product["title"],
            description=product["description"],
            detailed_description=product["detailed_description"],
            category_id=product["category_id"],
            owner_id=product["owner_id"],
            price=product["price"],
            preview_img_id=product["preview_img_id"],
        )
        for product in products_gear
    ]

    style = [
        Product(
            title=product["title"],
            description=product["description"],
            detailed_description=product["detailed_description"],
            category_id=product["category_id"],
            owner_id=product["owner_id"],
            price=product["price"],
            preview_img_id=product["preview_img_id"],
        )
        for product in products_style
    ]

    cars = [
        Product(
            title=product["title"],
            description=product["description"],
            detailed_description=product["detailed_description"],
            category_id=product["category_id"],
            owner_id=product["owner_id"],
            price=product["price"],
            preview_img_id=product["preview_img_id"],
        )
        for product in products_cars
    ]

    tech = [
        Product(
            title=product["title"],
            description=product["description"],
            detailed_description=product["detailed_description"],
            category_id=product["category_id"],
            owner_id=product["owner_id"],
            price=product["price"],
            preview_img_id=product["preview_img_id"],
        )
        for product in products_tech
    ]

    shelter = [
        Product(
            title=product["title"],
            description=product["description"],
            detailed_description=product["detailed_description"],
            category_id=product["category_id"],
            owner_id=product["owner_id"],
            price=product["price"],
            preview_img_id=product["preview_img_id"],
        )
        for product in products_shelter
    ]

    vices = [
        Product(
            title=product["title"],
            description=product["description"],
            detailed_description=product["detailed_description"],
            category_id=product["category_id"],
            owner_id=product["owner_id"],
            price=product["price"],
            preview_img_id=product["preview_img_id"],
        )
        for product in products_vices
    ]

    body = [
        Product(
            title=product["title"],
            description=product["description"],
            detailed_description=product["detailed_description"],
            category_id=product["category_id"],
            owner_id=product["owner_id"],
            price=product["price"],
            preview_img_id=product["preview_img_id"],
        )
        for product in products_body
    ]

    etc = [
        Product(
            title=product["title"],
            description=product["description"],
            detailed_description=product["detailed_description"],
            category_id=product["category_id"],
            owner_id=product["owner_id"],
            price=product["price"],
            preview_img_id=product["preview_img_id"],
        )
        for product in products_etc
    ]

    [db.session.add(product) for product in gear]
    [db.session.add(product) for product in style]
    [db.session.add(product) for product in cars]
    [db.session.add(product) for product in tech]
    [db.session.add(product) for product in shelter]
    [db.session.add(product) for product in vices]
    [db.session.add(product) for product in body]
    [db.session.add(product) for product in etc]

    db.session.commit()


def undo_products():
    # if environment == "production":
    #     db.session.execute(
    #         f"TRUNCATE table {SCHEMA}.products RESTART IDENTITY CASCADE;"
    #     )
    # else:
        db.session.execute("DELETE FROM products")

        db.session.commit()
