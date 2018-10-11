import pickle

from log import loggingSetting
from ut import pushaction, getAccounts

logger = loggingSetting("transferBalance")


def transferEos(f, to, n, m=""):
    return pushaction("eosio.token", "transfer", [f, to, "%.4f EOS" % n, m], f)


def tranferDice(f, to, n, m=""):
    return pushaction("betdicetoken", "transfer", [f, to, "%.4f DICE" % n, m], f)


def tranferAdd(f, to, n, m=""):
    return pushaction("eosadddddddd", "transfer", [f, to, "%.4f ADD" % n, m], f)


def tranferEsa(f, to, n, m=""):
    return pushaction("shadowbanker", "transfer", [f, to, "%.4f ESA" % n, m], f)


if __name__ == "__main__":
    accounts = getAccounts()
    for i in accounts:
        print(i)
        t = tranferDice(i, "gy2dgmztgqge", 1000)
        logger.info(t)
