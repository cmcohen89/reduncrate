from .db import db, environment, SCHEMA, add_prefix_for_prod


##################
# FAVORITES TABLE:
##################
favorites = db.Table(
    "favorites",
    db.Model.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey(("users.id")), primary_key=True),
    db.Column("product_id", db.Integer, db.ForeignKey(("products.id")), primary_key=True),
)

# if environment == "production":
#     favorites.schema = SCHEMA
