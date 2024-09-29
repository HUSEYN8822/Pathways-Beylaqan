from flask import Blueprint

views = Blueprint(__name__,"vieWs")


@views.route("/")
def home():
    return"home page"