from app.models import db, environment, SCHEMA, CartItem

all_cart_items = [
    {"id": 1, "cart_id": 1, "product_id": 1, "quantity": 1},
    {"id": 2, "cart_id": 1, "product_id": 2, "quantity": 2},
    {"id": 3, "cart_id": 2, "product_id": 3, "quantity": 1},
    {"id": 4, "cart_id": 2, "product_id": 4, "quantity": 3},
    {"id": 5, "cart_id": 3, "product_id": 5, "quantity": 4},
    {"id": 6, "cart_id": 3, "product_id": 6, "quantity": 1},
    {"id": 7, "cart_id": 4, "product_id": 7, "quantity": 2},
    {"id": 8, "cart_id": 4, "product_id": 8, "quantity": 4},
    {"id": 9, "cart_id": 5, "product_id": 9, "quantity": 1},
    {"id": 10, "cart_id": 5, "product_id": 10, "quantity": 1},
    {"id": 11, "cart_id": 6, "product_id": 11, "quantity": 2},
    {"id": 12, "cart_id": 6, "product_id": 12, "quantity": 1},
]

def seed_cart_items():
    cart_items = [
        CartItem(
            cart_id=item["cart_id"],
            product_id=item["product_id"],
            quantity=item["quantity"]
        )
        for item in all_cart_items
    ]

    [db.session.add(item) for item in cart_items]

    db.session.commit()

def undo_cart_items():
    # if environment == "production":
    #     db.session.execute(
    #         f"TRUNCATE table {SCHEMA}.cart_items RESTART IDENTITY CASCADE;"
    #     )
    # else:
        db.session.execute("DELETE FROM cart_items")

        db.session.commit()
