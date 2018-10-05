import json
import os
import pickle
from time import sleep

import requests

from log import loggingSetting
from ut import getAccounts, pushaction, unlock

s = requests.Session()
logger = loggingSetting("draw")


def main(password):
    x = getAccounts()
    for i in x:
        t = getdraw(i)
        if b"wrong identity" in t:
            sleep(1)
            print("*" * 60)
            getdraw(i)
        print(t)


def getdraw(account):
    b, c = randomN()
    return pushaction("betdicelucky", "draw", [account, b, c], account)


def randomN():
    # js代码如下。。。
    """                           for (n = t.sent,
                                            e = n.last_irreversible_block_num,
                                            o = 1,
                                            a = 0; a < 5651; a++)
                                            o *= e,
                                            o %= 8633;
                                        return t.next = 12,
                                            this.contract_login.draw({
                                                from: this.$store.state.account.name,
                                                b: e,
                                                c: o
                                            }, {
                                                authorization: this.$store.state.account.name + "@" + this.$store.state.account.authority
                                            });"""
    e = int(getinfo())
    o = 1
    for i in range(5651):
        o *= e
        o %= 8633
    return e, o


def getinfo():
    url = "https://api.eosbeijing.one/v1/{}"
    z1 = s.post(url.format("chain/get_info"))
    return z1.json()["last_irreversible_block_num"]


if __name__ == "__main__":
    password = "1"
    main(password)
