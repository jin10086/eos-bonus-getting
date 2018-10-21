import json
import requests
from ut import getAccounts


def getblance(accounts):
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


def getblanceBase(contract, symbol, accounts):
    s = requests.Session()
    url = "https://proxy.eosnode.tools/v1/{}"
    xxx = {}
    for i in accounts:
        z1 = s.post(
            url.format("chain/get_currency_balance"),
            json={"code": contract, "account": i, "symbol": symbol},
        )
        balance = float(z1.json()[0].split()[0])
        xxx[i] = balance
    return xxx


def getblanceLucky():
    accounts = getAccounts()
    s = requests.Session()
    url = "https://proxy.eosnode.tools/v1/{}"
    xxx = {}
    for i in accounts:
        z1 = s.post(
            url.format("chain/get_currency_balance"),
            json={"code": "eoslucktoken", "account": i, "symbol": "LUCKY"},
        )
        if z1.json():
            balance = float(z1.json()[0].split()[0])
        else:
            balance = 0
        xxx[i] = balance
    return xxx


if __name__ == "__main__":
    accounts = getAccounts()
    x = getblance(accounts)
    print(sorted(x.items(), key=lambda k: k[1]))
    print("余额一共为:{}".format(sum([v for k, v in x.items()])))
    print("一共{}个账号".format(len(x.keys())))
