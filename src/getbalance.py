import json
import requests
from ut import getAccounts

s = requests.Session()
s.headers = {
    "Authorization": "Bearer eyJhbGciOiJLTVNFUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NTI3NDM5MDYsImp0aSI6Ijc2YWMzZTZiLWFlNmItNDNhOC04MjViLWVmMDkwZmNiODI0OSIsImlhdCI6MTU1MDE1MTkwNiwiaXNzIjoiZGZ1c2UuaW8iLCJzdWIiOiJDaVFBNmNieWUreEdNZ3hQWTQ3UlVXSWFMbFNOQ20xN2p2TWh6VkRnL1JoQUlyaHFkN2NTTndBL0NMUnRUT05MKzlmUHc1TkRzUGUxeVBKeU5BanJYYW1nUW45RTVHeHRaWXZTSUdBVi8veXlGRGZDd3RnTUxxSXdFbVlhclRNPSIsInRpZXIiOiJiZXRhLXYxIiwidiI6MX0.wv5lK1wvvBN8ntC7nVW5R5MtMxc0L4zsu5h7HakCIFsuV1fMBSRt22FcIz3N3aclg7TPNbkj1QJXCkR22vyZNA"
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
            if i["rows"]:
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
