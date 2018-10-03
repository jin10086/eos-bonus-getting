import subprocess
import json
import os


def getAccounts():
    "获取所有的账号"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    accountFile = os.path.join(current_dir, "eosaccount.json")
    with open(accountFile) as f:
        account_names = json.loads(f.read())["account_names"]
        return account_names


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


def runcleos(cmd):
    a = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return a.stdout


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
