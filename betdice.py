import json
import subprocess

import requests
from log import loggingSetting
from time import sleep
import arrow

s = requests.Session()

rules = [10000, 30000, 90000]

logger = loggingSetting("betdice")


def sendTx(account, action, data, f):
    cmd = [
        # "docker",
        # "exec",
        # "hungry_cori",
        "cleos",
        "-u",
        "http://api.eosbeijing.one",
        "push",
        "action",
        account,
        action,
        json.dumps(data),
        "-p",
        f,
    ]
    a = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return a.stdout


def play(myaccount, password):
    logger.info("#" * 60)
    logger.info("开始玩...")
    account = "betdicetoken"
    action = "transfer"
    count = 0
    while True:
        while True:
            for _amount in rules:
                if count > 6:
                    logger.info("连续输了6吧了...等待60s再继续...")
                    sleep(60)
                amout = "%.4f DICE" % _amount
                memo = (
                    "action:bet,seed:p9PlfQYTo0p1B3O1wO,rollUnder:50,ref:bbheasxtlatd"
                )
                logger.info("投入的金额为:{}".format(_amount))
                data = [myaccount, "betdiceadmin", amout, memo]

                t = sendTx(account, action, data, myaccount)
                send_t = arrow.utcnow()
                sleep(1)
                if b"Locked" in t:
                    logger.info("cleos 没有解锁,正在解锁")
                    unlock(password)
                    break  # 重头循环开始玩.
                elif b"transaction:" in t:
                    logger.info("请求发送成功,正在获取游戏结果.")
                    isWin = getData(myaccount, "betdiceadmin", send_t)
                    if isWin:  # 我赢了
                        logger.info("赢了.")
                        count = 0
                        break  # 重头循环开始玩.
                    else:
                        logger.info("输了.")

                elif b"has one game not yet" in t:
                    logger.info("玩的太快了，上一次玩的还没有出结果")
                    sleep(10)
                    break
                else:
                    logger.info("发送请求失败,报错为:{}".format(t))
                    sleep(10)
                    break
                # 每次玩等待2s
                count += 1
                sleep(2)


def getData(account, contractAccount, t):
    url = "https://proxy.eosnode.tools/v1/{}"

    data = {"pos": -1, "account_name": account, "json": True}
    z = s.post(url.format("history/get_actions"), json=data)
    if not z.json().get("actions"):
        sleep(2)
        return getData(account, contractAccount, t)
    _data = list(filter(lambda k: arrow.get(k["block_time"]) > t, z.json()["actions"]))
    if _data:
        for i in reversed(_data):
            if i["action_trace"]["act"]["account"] == contractAccount:
                gamedata = i["action_trace"]["act"]["data"]
                rollUnder = gamedata["rollUnder"]
                diceNumber = gamedata["diceNumber"]
                logger.info("投注数字为{}, dice为{}".format(rollUnder, diceNumber))
                if rollUnder > diceNumber:
                    return True
                else:
                    return False
    sleep(2)
    return getData(account, contractAccount, t)


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
    a = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(a.stderr)


if __name__ == "__main__":
    myaccount = "gy2dgmztgqge"
    password = ""
    play(myaccount, password)
