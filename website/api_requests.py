from website.api_auth import Probit
from website.api_credentials import id, secret

probit = Probit(id, secret)


def balance_check():
    data = probit.balances()['data']
    return data


def orders_check():
    data = probit.open_order()['data']
    return data

print(balance_check())

