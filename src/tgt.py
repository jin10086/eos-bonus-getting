import time
import json
from websocket import create_connection
from ut import getAccounts
import requests

s = requests.Session()


def checkBalance(accounts, contract, symbol):
    url = "https://proxy.eosnode.tools/v1/{}"
    x = {}
    for account in accounts:
        z1 = s.post(
            url.format("chain/get_currency_balance"),
            json={"code": contract, "account": account, "symbol": symbol},
        )
        if z1.json():
            balance = float(z1.json()[0].split()[0])
            x[account] = balance
        else:
            x[account] = 0
    return x


def run(account):
    ws = create_connection("wss://eostiger.io/")
    print(account)
    ws.send(
        json.dumps(
            {"cmd": "sync.heartbeat", "para": {"want": {"sync.award_history": 1}}}
        )
    )
    ws.send(
        json.dumps(
            {
                "cmd": "sync.get_register_bonus",
                "chk": int(time.time()) * 1000000,
                "para": {"uid": account, "ref": "gy2dgmztgqge"},
            }
        )
    )
    ws.send(
        json.dumps(
            {
                "cmd": "sync.get_recommend_bonus",
                "chk": int(time.time()) * 1000000,
                "para": {"uid": account},
            }
        )
    )
    ws.close()


if __name__ == "__main__":
    accounts = getAccounts()
    for account in accounts:
        if not checkBalance(account, "eostgctoken1", "TGC"):
            run(account)
