import pickle

from log import loggingSetting
from ut import pushaction

logger = loggingSetting("transferBalance")
with open("tmp.pkl", "rb") as f:
    accounts = pickle.load(f)


def transferEos(f, to, n):
    return pushaction("eosio.token", "transfer", [f, to, "%.4f EOS" % n, ""], f)


def tranferDice(f, to, n):
    return pushaction("betdicetoken", "transfer", [f, to, "%.4f DICE" % n, ""], f)


if __name__ == "__main__":
    for i in accounts:
        print(i)
        t = transferEos("gy2dgmztgqge", i)
        logger.info(t)
