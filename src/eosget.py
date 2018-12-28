import requests
from ut import getAccounts, runPool, pushaction
import re

s = requests.Session()
s.headers = {
    "origin": "https://dice.eosget.io",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
}


def getinfo():
    url = "https://api.eosbeijing.one/v1/{}"
    z1 = s.post(url.format("chain/get_info"))
    return z1.json()["last_irreversible_block_num"]


def getrandom(account):
    z = s.get(f"https://dice.eosget.io/user/random?account={account}")
    return z.json()["data"]


def run(account):
    memo = f"luckdraw|{getrandom(account)}"
    x = pushaction("eosgetadmin1", "luckdraw", [account, memo], account)
    print(x)
    if not b"eosio_assert_message" in x:
        tx = re.findall(b"executed transaction: (.*?) ", x)[0]
        tx = str(tx, encoding="utf8")
        block_num = getinfo()
        data = {"transaction_id": tx, "block_num": block_num}
        z1 = s.post("https://dice.eosget.io/eos/luckdrawReport", data=data)
        print(z1.text)


if __name__ == "__main__":
    accounts = getAccounts()
    runPool(run, accounts)
