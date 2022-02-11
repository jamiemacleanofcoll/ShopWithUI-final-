from controllers.order_controller import OrderController
from controllers.product_controller import ProductController
from flask import Blueprint, redirect, render_template, request, session, url_for
from models.user import Role

from .check_auth import (
    admin_rights_required,
    authorization_required,
    check_admin,
    check_user,
)

shop_bp = Blueprint("shop_bp", __name__)

product_controller = ProductController()
order_controller = OrderController(product_controller)


@shop_bp.route("/", methods=["GET"])
def products():
    products = product_controller.view_products()
    return render_template(
        "products.html",
        products=enumerate(products, start=1),
        admin=check_admin(),
        str=str,
        logged_in=check_user(),
    )


@shop_bp.route("/", methods=["POST"])
@authorization_required
def add_to_card_submit():
    data = request.form
    user_id = session["current_user"]["user_id"]

    submit_value = data["submit"]
    product_id = submit_value.split(" ")[-1]
    product_id_int = int(product_id)

    product_quantity = data[f"product_quantity.{product_id}"]
    product_quantity_int = int(product_quantity)

    if order_controller.add_to_cart(user_id, product_id_int, product_quantity_int):
        message = (
            "Ok, we added "
            + product_quantity
            + " product(s) of product "
            + product_id
            + " to your cart!"
        )
    else:
        message = "Sorry, there is not enough stock for this product."
    products = product_controller.view_products()
    return render_template(
        "products.html",
        products=enumerate(products, start=1),
        admin=check_admin(),
        str=str,
        message=message,
        logged_in=check_user(),
    )


@shop_bp.route("/checkout", methods=["GET"])
@authorization_required
def checkout():
    return render_template("checkout.html", logged_in=check_user())


@shop_bp.route("/checkout", methods=["POST"])
@authorization_required
def checkout_submit():
    data = request.form
    firstname = data["firstname"]
    lastname = data["lastname"]
    street = data["street"]
    house_number = data["house_number"]
    zip_code = data["zip_code"]
    city = data["city"]
    credit_card_owner = data["credit_card_owner"]
    credit_card_number = data["credit_card_number"]
    cvv = data["cvv"]
    valid_month = data["valid_month"]
    valid_year = data["valid_year"]

    user_id = session["current_user"]["user_id"]
    order_controller.checkout(
        user_id,
        valid_month,
        valid_year,
        credit_card_owner,
        credit_card_number,
        cvv,
        firstname,
        lastname,
        street,
        house_number,
        zip_code,
        city,
    )
    products = product_controller.view_products()
    return render_template(
        "products.html",
        products=enumerate(products, start=1),
        admin=check_admin(),
        str=str,
        message="Thanks for your purchase!!!",
        logged_in=check_user(),
    )


@shop_bp.route("/add_product", methods=["GET"])
@admin_rights_required
def add_product():
    return render_template("add_product.html", logged_in=check_user())


@shop_bp.route("/add_product", methods=["POST"])
@admin_rights_required
def add_product_submit():
    data = request.form
    product_controller.add_product(
        name=data["name"],
        description=data["description"],
        price_before_tax=data["price_before_tax"],
        price_after_tax=data["price_after_tax"],
        stock=data["stock"],
        category=data["category"],
    )
    return redirect(url_for("shop_bp.products"))
