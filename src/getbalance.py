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


if __name__ == "__main__":
    x = getblance()
    print(sorted(x.items(), key=lambda k: k[1]))
    print("余额一共为:{}".format(sum([v for k, v in x.items()])))
    print("一共{}个账号".format(len(x.keys())))
