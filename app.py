import os

from flask import Flask, render_template

from views.main_view import main_bp
from views.review_view import review_bp
from views.shop_view import shop_bp
from views.user_view import user_bp

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.register_blueprint(main_bp, url_prefix="/")
app.register_blueprint(user_bp, url_prefix="/users")
app.register_blueprint(shop_bp, url_prefix="/shop")
app.register_blueprint(review_bp, url_prefix="/reviews")


app.run(debug=True)
