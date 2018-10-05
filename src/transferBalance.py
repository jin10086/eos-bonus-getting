import pickle

from log import loggingSetting
from ut import pushaction, getAccounts

logger = loggingSetting("transferBalance")


def transferEos(f, to, n):
    return pushaction("eosio.token", "transfer", [f, to, "%.4f EOS" % n, ""], f)


def tranferDice(f, to, n):
    return pushaction("betdicetoken", "transfer", [f, to, "%.4f DICE" % n, ""], f)


if __name__ == "__main__":
    accounts = getAccounts()
    for i in accounts:
        print(i)
        t = tranferDice(i, "gy2dgmztgqge", 1000)
        logger.info(t)
