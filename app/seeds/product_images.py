from app.models import db, ProductImage, environment, SCHEMA
from ._01_products_gear import products_gear_imgs
from ._02_products_style import products_style_imgs
from ._03_products_cars import products_cars_imgs
from ._04_products_tech import products_tech_imgs
from ._05_products_shelter import products_shelter_imgs
from ._06_products_vices import products_vices_imgs
from ._07_products_body import products_body_imgs
from ._08_products_etc import products_etc_imgs

def seed_product_images():
    gear_images = [
        ProductImage(
            product_id=image["product_id"],
            url=image["url"]
        )
        for image in products_gear_imgs
    ]

    style_images = [
        ProductImage(
            product_id=image["product_id"],
            url=image["url"]
        )
        for image in products_style_imgs
    ]

    cars_images = [
        ProductImage(
            product_id=image["product_id"],
            url=image["url"]
        )
        for image in products_cars_imgs
    ]

    tech_images = [
        ProductImage(
            product_id=image["product_id"],
            url=image["url"]
        )
        for image in products_tech_imgs
    ]

    shelter_images = [
        ProductImage(
            product_id=image["product_id"],
            url=image["url"]
        )
        for image in products_shelter_imgs
    ]

    vices_images = [
        ProductImage(
            product_id=image["product_id"],
            url=image["url"]
        )
        for image in products_vices_imgs
    ]

    body_images = [
        ProductImage(
            product_id=image["product_id"],
            url=image["url"]
        )
        for image in products_body_imgs
    ]

    etc_images = [
        ProductImage(
            product_id=image["product_id"],
            url=image["url"]
        )
        for image in products_etc_imgs
    ]

    [db.session.add(image) for image in gear_images]
    [db.session.add(image) for image in style_images]
    [db.session.add(image) for image in cars_images]
    [db.session.add(image) for image in tech_images]
    [db.session.add(image) for image in shelter_images]
    [db.session.add(image) for image in vices_images]
    [db.session.add(image) for image in body_images]
    [db.session.add(image) for image in etc_images]

    db.session.commit()

def undo_product_images():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.product_images RESTART IDENTITY CASCADE;"
        )
    else:
        db.session.execute("DELETE FROM product_images")

        db.session.commit()
