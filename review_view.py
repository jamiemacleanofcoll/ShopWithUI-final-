from controllers.review_controller import ReviewController
from flask import Blueprint, redirect, render_template, request, url_for

from views.check_auth import check_user

review_controller = ReviewController()


review_bp = Blueprint("review_bp", __name__)


@review_bp.route("/<product_id>", methods=["GET"])
def reviews(product_id):
    reviews = review_controller.view_reviews(int(product_id))
    return render_template(
        "reviews.html",
        reviews=enumerate(reviews, start=1),
        str=str,
        logged_in=check_user(),
    )


@review_bp.route("/<product_id>", methods=["POST"])
def review_submit(product_id):
    data = request.form
    review_controller.add_review(
        int(product_id), data["review_title"], data["review_text"]
    )
    return redirect(url_for("review_bp.reviews", product_id=product_id))
