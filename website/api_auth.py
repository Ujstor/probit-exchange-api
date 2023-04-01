import time
import json
import requests
import base64


class Probit:
    def __init__(self, id, secret):
        self.id = id
        self.secret = secret
        self.base_url = "https://api.probit.com/api/exchange/v1"
        self.current_time = time.time()
        self.token_time = time.time()
        self.access_token = None
        self.client = requests.Session()

    def token(self):
        try:
            self.current_time = time.time()
            if self.current_time < self.token_time - 2:
                return self.access_token
            url = "https://accounts.probit.com/token"
            b64 = base64.b64encode(f"{self.id}:{self.secret}".encode()).decode()
            response = self.client.post(url, headers={
                'authorization': f'Basic {b64}',
                'content-type': "application/json",
            }, json={"grant_type": "client_credentials"})
            response_json = json.loads(response.text)
            self.token_time = self.current_time + response_json["expires_in"]
            self.access_token = response_json["access_token"]
            return self.access_token
        except requests.exceptions.RequestException as e:
            raise e

    def balances(self):
        try:
            url = f"{self.base_url}/balance"
            access_token = self.token()
            response = self.client.get(url, headers={
                'authorization': f'Bearer {access_token}',
                'content-type': "application/json",
            })
            return json.loads(response.text)
        except requests.exceptions.RequestException as e:
            raise e

    def open_order(self):
        try:
            url = f"{self.base_url}/open_order"
            access_token = self.token()
            response = self.client.get(url, headers={
                'authorization': f'Bearer {access_token}',
                'content-type': "application/json",
            })
            return json.loads(response.text)
        except requests.exceptions.RequestException as e:
            raise e