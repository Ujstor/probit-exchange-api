from website.api_auth import Probit
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

ID = os.environ.get('ID')
SECRET = os.environ.get('SECRET')

probit = Probit(ID, SECRET)


def balance_check():
    data = probit.balances()['data']
    return data


def orders_check():
    data = probit.open_order()['data']
    return data

