from flask.cli import AppGroup
from .users import seed_users, undo_users
from .categories import seed_categories, undo_categories
from .products import seed_products, undo_products
from .product_images import seed_product_images, undo_product_images
from .carts import seed_carts, undo_carts
from .cart_items import seed_cart_items, undo_cart_items
from app.models.db import db, environment, SCHEMA
from app.models import Product

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup("seed")


# Creates the `flask seed all` command
@seed_commands.command("all")
def seed():
    if environment == "production":
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_cart_items()
        undo_carts()
        undo_product_images()
        undo_products()
        undo_categories()
        undo_users()
    seed_users()
    seed_categories()
    seed_products()
    seed_product_images()
    seed_carts()
    seed_cart_items()

    all_product_seeds = Product.query.all()
    for product in all_product_seeds:
        setattr(product, "preview_img_id", product.product_images[0].to_dict()["id"])
        for product_image in product.product_images:
            if "shopify" in product_image.url:
                setattr(product, "cart_img_url", product_image.url)

    db.session.commit()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command("undo")
def undo():
    undo_cart_items()
    undo_carts()
    undo_product_images()
    undo_products()
    undo_categories()
    undo_users()
    # Add other undo functions here
