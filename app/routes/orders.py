# create a new instance of the Blueprint class named "index" that handles route the top-level route of "". Then, define a route for a function named "index" that handles "/" and returns the string "Order Up!"

from flask import (Blueprint, render_template)
from flask_login import login_required

bp = Blueprint("orders", __name__, url_prefix="")


@bp.route("/")
@login_required
def index():
    # return "Order Up!"
    return render_template("orders.html")