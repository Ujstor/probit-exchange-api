from flask import Blueprint, render_template
from .api_requests import orders_check, balance_check

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def home():
    data1 = orders_check()
    data2 = balance_check()
    return render_template("home.html", data1=data1, data2=data2)
