import subprocess
import json
import os
from multiprocessing import Pool
import string
import random


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


def buyram(f, t, ram):
    cmd = [
        # "docker",
        # "exec",
        # "hungry_cori",
        "cleos",
        "-u",
        "http://api.eosbeijing.one",
        "system",
        "buyram",
        f,
        t,
        f"{ram}",
        "--kbytes",
        "-p",
        f,
    ]
    return runcleos(cmd)


def delegatebw(f, t, net, cpu):
    """
    抵押 cpu ，内存
    f>t,谁抵押给谁，如果是抵押给自己的话，则, f,t都是自己
    """

    cmd = [
        # "docker",
        # "exec",
        # "hungry_cori",
        "cleos",
        "-u",
        "http://api.eosbeijing.one",
        "system",
        "delegatebw",
        f,
        t,
        "%.4f EOS" % net,
        "%.4f EOS" % cpu,
        "-p",
        f,
    ]
    return runcleos(cmd)


def pushaction(contract, action, data, f, node="eos"):
    """
    contract :要玩的合约地址
    action: 玩的方法
    data : 详细信息
    f :账号
    """
    if node == "eos":
        apiurl = "http://api.eosbeijing.one"
    elif node == "bos":
        apiurl = "https://api.boscore.io"
    cmd = [
        "cleos",
        "-u",
        apiurl,
        "push",
        "action",
        contract,
        action,
        json.dumps(data),
        "-p",
        f,
    ]
    return runcleos(cmd)


def runPool(f, accounts):
    with Pool() as pool:
        pool.map(f, accounts)


def gettable(code, scope, table, node="eos"):
    if node == "eos":
        apiurl = "http://api.eosbeijing.one"
    elif node == "bos":
        apiurl = "https://api.boscore.io"
    return json.loads(
        runcleos(["cleos", "-u", apiurl, "get", "table", code, scope, table])
    )


def genrateRandomN(k=12):
    return "".join(random.choices(string.ascii_lowercase, k=k))
