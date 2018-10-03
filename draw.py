import os
import json
from log import loggingSetting
from ut import pushaction, unlock

logger = loggingSetting("draw")


def getAccounts():
    "获取所有的账号"
    accountFile = os.path.join(".", "eosaccount.json")
    with open(accountFile) as f:
        account_names = json.loads(f.read())["account_names"]
        return account_names


def main(password):
    x = getAccounts()
    unlock(password)
    for i in x:
        print(pushaction("betdicelucky", "draw", [i], i))


if __name__ == "__main__":
    password = ""
    main(password)
