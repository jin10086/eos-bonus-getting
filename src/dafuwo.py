from ut import pushaction, runcleos
from transferBalance import transferEos, tranferRich
import json
import time

RICHCONTRACT = "richrich2222"


def auction(account, q):  # 拍卖
    return transferRICH(account, RICHCONTRACT, q, m="auction")


def playdice(account):  # 投掷骰子
    return pushaction(RICHCONTRACT, "playdice", [account, "2010"], account)


def buyland(account):  # 买地
    return transferEos(account, RICHCONTRACT, 10, m="buyland2010")


def buytoken(account, q):  # 购买token
    return transferEos(account, RICHCONTRACT, q, m="buytoken")


def buyhostel(account, count):  # 建旅馆
    return transferEos(account, RICHCONTRACT, 2 * count, m=f"buyhostel2010|{count}")


def gettable(code, scope, table):
    cmd = [
        "cleos",
        "-u",
        "https://api.eosbeijing.one:443",
        "get",
        "table",
        "-l",
        "200",
        code,
        scope,
        table,
    ]
    x = runcleos(cmd)
    return json.loads(x)


def getusers(account):  # 查询用户的位置,用户的押金，当前位置，以及能干嘛.
    a = gettable(RICHCONTRACT, account, "users")
    return a


def payrent(account):  # 支付押金
    return pushaction(RICHCONTRACT, "payrent", [account], account)


def run():
    print(playdice("gy2dgmztgqge"))
    # print(buyland("gaojin.game"))


if __name__ == "__main__":

    # tranferRich("gy2dgmztgqge", "richrich2222", 2100, "save")
    # print(payrent("gaojin.game"))
    a = getusers("gy2dgmztgqge")
    print(a)
    while True:
        run()
        a = getusers("gy2dgmztgqge")
        print(a)

        if a["rows"][0]["location"] == "16":
            break
        time.sleep(1)
