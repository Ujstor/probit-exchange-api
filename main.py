from api_auth import Probit
from api_credentials import id, secret
from tabulate import tabulate

probit = Probit(id, secret)


def balance_check():
    data = probit.balances()['data']
    print(tabulate(data, headers='keys', floatfmt=".2f", showindex="always", tablefmt="github"))


def orders_check():
    data = probit.open_order()['data']
    print(tabulate(data, headers='keys', floatfmt=".8f",  showindex="always", tablefmt="github"))


balance_check()
print('\n')
orders_check()

