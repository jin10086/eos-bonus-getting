import json
import requests
from ut import getAccounts


def getblance():
    accounts = getAccounts()
    s = requests.Session()
    url = "https://proxy.eosnode.tools/v1/{}"
    xxx = {}
    for i in accounts:
        z1 = s.post(
            url.format("chain/get_currency_balance"),
            json={"code": "eosio.token", "account": i, "symbol": "EOS"},
        )
        balance = float(z1.json()[0].split()[0])
        xxx[i] = balance
    return xxx


getblance()
