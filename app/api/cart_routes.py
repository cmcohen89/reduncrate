from flask import Blueprint, jsonify, render_template, request, redirect
from flask_login import login_required, current_user
from app.models import db, Cart, CartItem


carts_routes = Blueprint("carts", __name__)


# ------------------------------ CART ROUTES ------------------------------#


@carts_routes.route("")
@login_required
def get_cart():
    """
    Query for logged-in user's active cart and returns it as a dictionary.
    """
    has_active_cart = Cart.query \
        .filter(Cart.user_id == current_user.get_id()) \
        .filter(Cart.purchased == False).count()

    if has_active_cart:
        cart = Cart.query \
            .filter(Cart.user_id == current_user.get_id()) \
            .filter(Cart.purchased == False).one()

        return cart.to_dict()

    else:
        cart = Cart(
            user_id = current_user.get_id(),
            total = 0,
            purchased = False
        )
        db.session.add(cart)
        db.session.commit()

        return cart.to_dict()



@carts_routes.route("", methods=["POST"])
@login_required
def add_cart_item():
    """
    A logged-in user can send a post request to add a product to their currently active cart.
    """
    has_active_cart = Cart.query \
        .filter(Cart.user_id == current_user.get_id()) \
        .filter(Cart.purchased == False).count()

    if has_active_cart:
        cart = Cart.query \
        .filter(Cart.user_id == current_user.get_id()) \
        .filter(Cart.purchased == False).one()

        new_cart_item = CartItem(
            cart_id = cart.to_dict()["id"],
            product_id = request.json['product_id'],
            quantity = 1
        )

        db.session.add(new_cart_item)
        db.session.commit()

        return new_cart_item.to_dict()

    else:
        cart = Cart(
            user_id = current_user.get_id(),
            total = 0,
            purchased = False
        )
        db.session.add(cart)
        db.session.commit()

        new_cart_item = CartItem(
            cart_id = cart.to_dict()["id"],
            product_id = request.json['product_id'],
            quantity = 1
        )

        db.session.add(new_cart_item)
        db.session.commit()

        return new_cart_item.to_dict()


@carts_routes.route("/<int:id>", methods=["PUT"])
@login_required
def update_cart_item(id):
    """
    Query for a single cart item by id from the current user's active cart and update the quantity.
    """
    cart_item = CartItem.query.get(id)

    setattr(cart_item, "quantity", request.json['quantity'])
    db.session.commit()
    return cart_item.to_dict()


@carts_routes.route("/<int:id>", methods=["DELETE"])
@login_required
def delete_cart_item(id):
    """
    Query for a single cart item by id and delete the cart item from the current user's active cart.
    """
    cart_item = CartItem.query.get(id)
    db.session.delete(cart_item)
    db.session.commit()
    return {
        'message': 'Successfully deleted',
        'status_code': 200
    }

@carts_routes.route("", methods=["PUT"])
@login_required
def purchase_cart():
    """
    Query for the current user's current cart and set the cart's purchased status to True.
    """
    cart = Cart.query \
            .filter(Cart.user_id == current_user.get_id()) \
            .filter(Cart.purchased == False).one()

    setattr(cart, "purchased", True)
    setattr(cart, "total", request.json['total'])
    db.session.commit()
    return cart.to_dict()


@carts_routes.route("/history")
@login_required
def get_history():
    """
    Query for the current user's purchased carts and and return them in a list of cart dictionaries.
    """
    carts = Cart.query \
                .filter(Cart.user_id == current_user.get_id()) \
                .filter(Cart.purchased == True).all()

    return {"OrderHistory": [cart.to_dict() for cart in carts]}
