import json
import requests
from ut import getAccounts

s = requests.Session()
s.headers = {
    "Authorization": "Bearer eyJhbGciOiJLTVNFUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NTYwMTQ1NzIsImp0aSI6IjM3YzBjZTQ0LTQyZmMtNDllNC1hZmI0LTYwNzE3ODJjZmQ3MCIsImlhdCI6MTU1MzQyMjU3MiwiaXNzIjoiZGZ1c2UuaW8iLCJzdWIiOiJDaVFBNmNieWV5UkJvTitWZUVhK0ZPbXpPNUpCQ2FqbzdUNXkzdnJ6bndlWnFycWxJMmNTTndBL0NMUnRaUEFJMTZYSVhkYkV5SFkwZXo5cnhCQkJ3MkU2WmRRTFFWZlFkVTB0VjUzNU1pRk9YMEMwSG8xR0dKQTIxR3pxdUxRPSIsInRpZXIiOiJiZXRhLXYxIiwidiI6MX0.IsDg5nkuKGXjpkY4m1s5NTbgRBLC90MHAyGzgTPCZ1DMPtqpVZ-UISlcQMLTfc0CJ_eJX086Bb0MBZzZaMskyw"
}
url = "https://mainnet.eos.dfuse.io/"


def getbalanceBase(account, accounts):
    token = gettoken()
    s.headers = {"Authorization": f"Bearer {token}"}
    x = {}
    for i in range(0, len(accounts), 100):
        data = {
            "account": account,
            "scopes": "|".join(accounts[i : i + 100]),
            "table": "accounts",
            "json": "true",
        }
        z = s.get(url + "v0/state/tables/scopes", params=data).json()
        if "tables" in z:
            data = z["tables"]
            for i in data:
                if i["rows"]:
                    x[i["scope"]] = float(i["rows"][0]["json"]["balance"].split(" ")[0])
        else:
            print(z)
            break
    return x


def gettoken():
    url = "https://auth.dfuse.io/v1/auth/issue"
    z1 = s.post(url, json={"api_key": "server_3c08733bd4d686d127060ffa3c371d4d"})
    return z1.json()["token"]


def getEOSbalance(accounts):
    return getbalanceBase("eosio.token", accounts)


if __name__ == "__main__":
    accounts = getAccounts()
    x = getEOSbalance(accounts)

    print(sorted(x.items(), key=lambda k: k[1]))
    print("余额一共为:{}".format(sum([v for k, v in x.items()])))
    print("一共{}个账号".format(len(x.keys())))
