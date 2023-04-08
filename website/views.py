from flask import Blueprint, render_template
from .api_requests import orders_check, balance_check

views = Blueprint('views', __name__)

@views.route('/')
def home():
    data1 = balance_check()
    return render_template("home.html", data1=data1)

@views.route('/orders')
def orders():
    data2 = orders_check()
    return render_template("orders.html", data2=data2)