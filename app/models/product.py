from .db import db, environment, SCHEMA, add_prefix_for_prod
from .joins import favorites


################
# PRODUCT MODEL:
################
class Product(db.Model):
    __tablename__ = "products"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(2000))
    detailed_description = db.Column(db.String(5000))
    category_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod(("categories.id"))), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod(("users.id"))), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    preview_img_id = db.Column(db.Integer, nullable=False)
    cart_img_url = db.Column(db.String(1000))

    # RELATIONSHIPS:
    # product_owner <--> user_products
    product_owner = db.relationship("User", back_populates="user_products")

    # users_who_favorited <-- favorites --> user_favorites
    users_who_favorited = db.relationship("User", back_populates="user_favorites", secondary=favorites, lazy="joined")

    # cart_item <--> product
    cart_item = db.relationship("CartItem", back_populates="product", cascade="all, delete")

    # product_category <--> category_products
    product_category = db.relationship("Category", back_populates="category_products")

    # product_images <--> image_product
    product_images = db.relationship("ProductImage", back_populates="image_product", cascade="all, delete")

    def to_dict(self):
        # print(self.product_images[0].to_dict()["id"])
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "detailedDescription": self.detailed_description,
            "categoryId": self.category_id,
            "price": self.price,
            "previewImgId": self.preview_img_id,
            "productOwner": self.product_owner.to_dict(),
            "productCategory": self.product_category.to_dict(),
            "productImages": {image.to_dict()["id"]: image.to_dict() for image in self.product_images},
            "cartImgUrl": self.cart_img_url
        }

    def __repr__(self):
        return f"<Product {self.id}: {self.title}>"


#################
# CATEGORY MODEL:
#################
class Category(db.Model):
    __tablename__ = "categories"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    # RELATIONSHIPS:
    # category_products <--> product_category
    category_products = db.relationship("Product", back_populates="product_category")

    def to_dict(self):
        return {"id": self.id, "name": self.name}

    def __repr__(self):
        return f"<Category {self.id}: {self.name}>"


######################
# PRODUCT IMAGE MODEL:
######################
class ProductImage(db.Model):
    __tablename__ = "product_images"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod(("products.id"))), nullable=False)
    url = db.Column(db.String(1500), nullable=False)

    # RELATIONSHIPS:
    # image_product <--> product_images
    image_product = db.relationship("Product", back_populates="product_images")

    def to_dict(self):
        return {"id": self.id, "productId": self.product_id, "url": self.url}

    def __repr__(self):
        return f"<Image ID: {self.id}, Product ID: {self.product_id}>"
