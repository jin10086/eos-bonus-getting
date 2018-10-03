import subprocess
import os
import json
from log import loggingSetting

logger = loggingSetting("draw")


def unlock(password):
    cmd = [
        # "docker",
        # "exec",
        # "hungry_cori",
        "cleos",
        "wallet",
        "unlock",
        "--password",
        password,
    ]
    print(" ".join(cmd))
    a = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def pushaction(contract, action, data, f):
    """
    contract :要玩的合约地址
    action: 玩的方法
    data : 详细信息
    f :账号
    """

    cmd = [
        # "docker",
        # "exec",
        # "hungry_cori",
        "cleos",
        "-u",
        "http://api.eosbeijing.one",
        "push",
        "action",
        contract,
        action,
        json.dumps(data),
        "-p",
        f,
    ]
    a = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return a.stdout


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
