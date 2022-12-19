from flask import Blueprint, jsonify, render_template, request, redirect
from flask_login import login_required, current_user
from app.models import db, Product, ProductImage
from app.forms import ProductUpdateForm, ProductForm
from .auth_routes import validation_errors_to_error_messages


products_routes = Blueprint("products", __name__)


# ------------------------------ PRODUCT ROUTES ------------------------------#


# GET ALL PRODUCTS:
@products_routes.route("")
def get_products():
    """
    Query for all products and returns them in a list of product dictionaries.
    """

    products = Product.query.all()
    return {"Products": [product.to_dict() for product in products]}


# GET A SINGLE PRODUCT:
@products_routes.route("/<int:id>")
def get_one_product(id):
    """
    Query for a single product by id and return it as a dictionary.
    """

    product = Product.query.get(id)
    return product.to_dict()


# CREATE A NEW PRODUCT:
@products_routes.route("", methods=["POST"])
@login_required
def post_product():
    """
    A logged-in user can send a post request to create a new product
    """

    form = ProductForm()
    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        data = form.data

        new_product = Product(
            title=data["title"],
            description=data["description"],
            detailed_description=data["detailed_description"],
            category_id=data["category_id"],
            owner_id=current_user.get_id(),
            price=data["price"],
            preview_img_id=0,
        )

        db.session.add(new_product)
        db.session.commit()

        new_preview_img = ProductImage(
            product_id=new_product.to_dict()["id"], url=data["preview_img_url"]
        )

        db.session.add(new_preview_img)
        db.session.commit()

        setattr(new_product, "preview_img_id", new_preview_img.to_dict()["id"])

        db.session.commit()

        return new_product.to_dict()
    print(validation_errors_to_error_messages(form.errors))
    return {"errors": validation_errors_to_error_messages(form.errors)}, 403


# UPDATE A SINGLE PRODUCT:
@products_routes.route("/<int:id>/update", methods=["PUT"])
@login_required
def update_product(id):
    """
    Query for a single product by id and update the product if authorized.
    """
    product = Product.query.get(id)
    product_dict = product.to_dict()

    form = ProductUpdateForm(
        title=product_dict["title"],
        description=product_dict["description"],
        detailed_description=product_dict["detailedDescription"],
        category_id=product_dict["categoryId"],
        price=product_dict["price"],
    )

    form["csrf_token"].data = request.cookies["csrf_token"]
    if form.validate_on_submit():
        data = form.data

        setattr(product, "title", data["title"])
        setattr(product, "description", data["description"])
        setattr(product, "detailed_description", data["detailed_description"])
        setattr(product, "category_id", data["category_id"])
        setattr(product, "price", data["price"])

        db.session.commit()
        return product.to_dict()
    print(validation_errors_to_error_messages(form.errors))
    return {"errors": validation_errors_to_error_messages(form.errors)}, 403


# DELETE A SINGLE PRODUCT:
@products_routes.route("/<int:id>", methods=["DELETE"])
@login_required
def delete_product(id):
    """
    Query for a single product by id and delete the product if authorized.
    """

    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return {"message": "Successfully deleted", "status_code": 200}
