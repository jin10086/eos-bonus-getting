import os
import json
from log import loggingSetting
from ut import pushaction, unlock
import pickle

logger = loggingSetting("draw")


def getAccounts():
    "获取所有的账号"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    accountFile = os.path.join(current_dir, "eosaccount.json")
    with open(accountFile) as f:
        account_names = json.loads(f.read())["account_names"]
        return account_names


def main(password):
    x = getAccounts()
    unlock(password)
    for i in x:
        print(pushaction("betdicelucky", "draw", [i], i))
        # print(pushaction("betdicetoken", "signup", [i, "1000.0000 DICE"], i)) # 1000dice


if __name__ == "__main__":
    password = ""
    main(password)
