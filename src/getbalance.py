import json
import requests
from draw import getAccounts


def getblance():
    accounts = getAccounts()
    s = requests.Session()
    url = "https://proxy.eosnode.tools/v1/{}"
    for i in accounts:
        z1 = s.post(
            url.format("chain/get_currency_balance"),
            json={"code": "eosio.token", "account": i, "symbol": "EOS"},
        )
        balance = float(z1.json()[0].split()[0])
        if balance > 0.2:
            print(i, balance)


getblance()
