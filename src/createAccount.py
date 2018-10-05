from ut import pushaction, runcleos, delegatebw
from log import loggingSetting
import random
import string

logger = loggingSetting("createAccount")


def genrateRandomName():
    return "".join(random.choices(string.ascii_lowercase, k=12))


def createKey():
    pass


def checkName(name):
    cmd = "cleos -u http://api.eosbeijing.one get account {}".format(name)
    a = runcleos(cmd.split(" "))
    if b"created" not in a:
        return True
    else:
        logger.info("该用户名:{},已经被注册".format(name))
        return False


def createUser(publicKey, name=None, cpu=0.1, net=0.1, ram=3):
    if not name:
        name = genrateRandomName()
    # 直到随机到一个没有注册的用户名.
    while True:
        if checkName(name):
            break
        name = genrateRandomName()

    cmd = [
        "cleos",
        "-u",
        "http://api.eosbeijing.one",
        "system",
        "newaccount",
        "gy2dgmztgqge",
        name,
        publicKey,
        publicKey,
        "--stake-net",
        "{} EOS".format(net),
        "--stake-cpu",
        "{} EOS".format(cpu),
        "--buy-ram-kbytes",
        "{}".format(ram),
    ]
    t = runcleos(cmd)
    logger.info(name)
    logger.info(t)


def createUser1(publicKey, f, _amount=0.64, name=None):
    "使用 signupeoseos 来注册匿名账号,http://signupeoseos.com/#/"
    if not name:
        name = genrateRandomName()
    # 直到随机到一个没有注册的用户名.
    amount = "%.4f EOS" % _amount
    while True:
        if checkName(name):
            break
        name = genrateRandomName()
    memo = "{}-{}".format(name, publicKey)
    t = pushaction("eosio.token", "transfer", [f, "signupeoseos", amount, memo], f)

    logger.info("account:{}".format(name))
    logger.info(t)


if __name__ == "__main__":
    logger.info("开始注册账号...")
    publicKey = ""
    f = ""
    for i in range(100):
        createUser1(publicKey, f)
