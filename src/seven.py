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
    ws = create_connection(
        "wss://socket.eoseven.com/socket.io/?EIO=3&transport=websocket"
    )
    print(account)
    ws.send("40/dice,")
    ws.send("42/dice," + json.dumps(["HistoryRouter", {"action": "history"}]))
    ws.send(
        "42/dice,"
        + json.dumps(
            ["HistoryRouter", {"action": "hugeWin", "payload": {"symbol": "EOS"}}]
        )
    )
    ws.send(
        "42/dice,"
        + json.dumps(
            [
                "AirgrabRouter",
                {
                    "router": "AirgrabRouter",
                    "action": "airgrab",
                    "payload": {"account": account},
                },
            ]
        )
    )
    ws.close()


if __name__ == "__main__":
    accounts = getAccounts()
    # x = checkBalance(accounts, "eoseventoken", "SVN")
    for account in accounts:
        # if not checkBalance(account, "eoseventoken", "SVN"):
        run(account)
