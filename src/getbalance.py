import json
import requests
from ut import getAccounts

s = requests.Session()
s.headers = {
    "Authorization": "Bearer eyJhbGciOiJLTVNFUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NDkyNzY1ODgsImp0aSI6ImQ2YjllYmNlLTllOTYtNGFkNi1iNDY3LWM4NDAwMjBmMDczMyIsImlhdCI6MTU0NjY4NDU4OCwiaXNzIjoiZGZ1c2UuaW8iLCJzdWIiOiJDaVFBNmNieWU0OWVJMHRHTUNnZ0tkUEd4QjRwKzhsMUtNWVZBZVFWR0MxaWkyUkxhWThTTndBL0NMUnQ0eFBhVGVqRitKSkEwY04vQkFmd1JGcnpJcW4vbk1BQWNpQWkzOCtyWlRKajlLM09jK1dwMjVvenAwR21vR2hVazg0PSIsInRpZXIiOiJiZXRhLXYxIiwidiI6MX0.ZGEA5Y6yIilgmMZP-m_Wc_0pYes0ZSpGy4bsJTgl40edsttO68mbEqxad-sqVGjtDZyiRa17yDjKF0f8iIC5Ww"
}
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
        z = s.get(url + "v0/state/tables/scopes", params=data).json()["tables"]
        for i in z:
            x[i["scope"]] = float(i["rows"][0]["json"]["balance"].split(" ")[0])
    return x


def getEOSbalance(accounts):
    return getbalanceBase("eosio.token", accounts)


if __name__ == "__main__":
    accounts = getAccounts()
    x = getEOSbalance(accounts)

    print(sorted(x.items(), key=lambda k: k[1]))
    print("余额一共为:{}".format(sum([v for k, v in x.items()])))
    print("一共{}个账号".format(len(x.keys())))
