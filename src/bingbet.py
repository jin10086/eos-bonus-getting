from ut import getAccounts, runPool

from transactions import push_transaction


def run(account):
    actions = [
        [
            "eosio.token",
            "transfer",
            {
                "from": account,
                "to": "bingobetgame",
                "quantity": "0.1000 EOS",
                "memo": "",
            },
            account,
        ],
        [
            "bingobetgame",
            "playdice",
            {"player": account, "player_salt": "6328764201341931", "roll_under": 96},
            account,
        ],
    ]
    print(push_transaction(actions))


if __name__ == "__main__":
    accounts = getAccounts()
    runPool(run, accounts)
