import json
import requests
from ut import getAccounts

s = requests.Session()


def gettoken():
    url = "https://auth.dfuse.io/v1/auth/issue"
    z1 = s.post(url, json={"api_key": "server_3c08733bd4d686d127060ffa3c371d4d"})
    return z1.json()["token"]


token = gettoken()
s.headers = {"Authorization": f"Bearer {token}"}
url = "https://mainnet.eos.dfuse.io/"


def getbalanceBase(account, accounts):

    x = {}
    for i in range(0, len(accounts), 100):
        data = {
            "account": account,
            "scopes": "|".join(accounts[i : i + 100]),
            "table": "accounts",
            "json": "true",
        }
        z = s.get(url + "v0/state/tables/scopes", params=data, verify=False).json()
        if "tables" in z:
            data = z["tables"]
            for i in data:
                if i["rows"]:
                    x[i["scope"]] = float(i["rows"][0]["json"]["balance"].split(" ")[0])
        else:
            print(z)
            break
    return x


def getRamPrice():
    data = {"account": "eosio", "scopes": "eosio", "table": "rammarket", "json": "true"}
    z = s.get(url + "v0/state/tables/scopes", params=data, verify=False).json()[
        "tables"
    ][0]["rows"][0]["json"]
    cBalance = z["quote"]["balance"].split(" ")[0]
    sBalance = z["base"]["balance"].split(" ")[0]
    price = float(cBalance) / float(sBalance)
    return price * 1024


def getEOSbalance(accounts):
    return getbalanceBase("eosio.token", accounts)


if __name__ == "__main__":
    accounts = getAccounts()
    x = getEOSbalance(accounts)

    print(sorted(x.items(), key=lambda k: k[1]))
    print("余额一共为:{}".format(sum([v for k, v in x.items()])))
    print("一共{}个账号".format(len(x.keys())))
