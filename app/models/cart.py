from .db import db, environment, SCHEMA, add_prefix_for_prod


#############
# CART MODEL:
#############
class Cart(db.Model):
    __tablename__ = "carts"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod(("users.id"))), nullable=False)  # FOREIGN KEY EVEN THOUGH 1:1?
    total = db.Column(db.Integer, nullable=False)
    purchased = db.Column(db.Boolean, default=False)

    # RELATIONSHIPS:
    # cart_items <--> item_cart
    cart_items = db.relationship("CartItem", back_populates="item_cart")

    # cart_user <--> user_cart
    # cart_user = db.relationship("User", back_populates="user_cart")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "total": self.total,
            "purchased": self.purchased,
            "cartItems": {item.to_dict()["id"]: item.to_dict() for item in self.cart_items},
            # "cartUser": self.cart_user.to_dict()
        }

    def __repr__(self):
        return f"<Cart: {self.id}, User ID: {self.user_id}>"


##################
# CART_ITEM MODEL:
##################
class CartItem(db.Model):
    __tablename__ = "cart_items"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod(("carts.id"))), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod(("products.id"))), nullable=False)  # FOREIGN KEY EVEN THOUGH 1:1?
    quantity = db.Column(db.Integer, nullable=False)

    # RELATIONSHIPS:
    # item_cart <--> cart_items
    item_cart = db.relationship("Cart", back_populates="cart_items")

    # product <--> cart_item
    product = db.relationship("Product", back_populates="cart_item")

    def to_dict(self):
        return {
            "id": self.id,
            "cartId": self.cart_id,
            "productId": self.product_id,
            "quantity": self.quantity,
            "product": self.product.to_dict()
        }

    def __repr__(self):
        return f"<Product: {self.product_id}, Cart: {self.cart_id}>"
