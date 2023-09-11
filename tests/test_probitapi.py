
def test_balance_page(client):
    balance = client.get("/")
    html = balance.data.decode()
    assert balance.status_code == 200

    assert '<a href="/"><button class="btn btn-outline-success me-2" type="button">Balance</button></a>' in html
    assert '<a href="orders"><button class="btn btn-outline-success me-2" type="button">Open Orders</button></a>' in html
    assert '<th>Currency ID</th>' in html
    assert '<th>Total</th>' in html
    assert '<th>Available</th>' in html

def test_orders_page(client):
    orders = client.get("/orders")
    html = orders.data.decode()
    assert orders.status_code == 200

    assert '<a href="/"><button class="btn btn-outline-success me-2" type="button">Balance</button></a>' in html
    assert '<a href="orders"><button class="btn btn-outline-success me-2" type="button">Open Orders</button></a>' in html
    assert '<th>Market ID</th>' in html
    assert '<th>Side</th>' in html
    assert '<th>Quantity</th>' in html
    assert '<th>Limit Price</th>' in html
    assert '<th>Filled Cost</th>' in html
    assert '<th>Filled Quantity</th>' in html
    assert '<th>Open Quantity</th>' in html
    assert '<th>Status</th>' in html

def test_balances(probit):
    response = probit.balances()
    data = response.get('data', [])
    for item in data:
        assert 'available' in item
        assert 'currency_id' in item
        assert 'total' in item

def test_open_orders(probit):
    response = probit.open_order()
    data = response.get('data', [])
    for item in data:
        assert 'market_id' in item
        assert 'side' in item
        assert 'quantity' in item
        assert 'limit_price' in item
        assert 'filled_cost' in item
        assert 'filled_quantity' in item
        assert 'open_quantity' in item
        assert 'status' in item

def test_error_handling(client):
    response = client.get("/non_existent_endpoint")
    assert response.status_code == 404

