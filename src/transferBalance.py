import pickle

from log import loggingSetting
from ut import pushaction, getAccounts

logger = loggingSetting("transferBalance")


def transferEos(f, to, n, m=""):
    return pushaction("eosio.token", "transfer", [f, to, "%.4f EOS" % n, m], f)


def transferPraEos(f, to, n, m=""):
    return pushaction("prochaintest", "transfer", [f, to, "%.4f EOS" % n, m], f)


def tranferDice(f, to, n, m=""):
    return pushaction("betdicetoken", "transfer", [f, to, "%.4f DICE" % n, m], f)


def tranferAdd(f, to, n, m=""):
    return pushaction("eosadddddddd", "transfer", [f, to, "%.4f ADD" % n, m], f)


def tranferEsa(f, to, n, m=""):
    return pushaction("shadowbanker", "transfer", [f, to, "%.4f ESA" % n, m], f)


def tranferBocai(f, to, n, m=""):
    return pushaction("eosbocai1111", "transfer", [f, to, "%.4f BOCAI" % n, m], f)


def tranferKar(f, to, n, m=""):
    return pushaction("therealkarma", "transfer", [f, to, "%.4f KARMA" % n, m], f)


def tranferEUSD(f, to, n, m=""):
    return pushaction("bitpietokens", "transfer", [f, to, "%.8f EUSD" % n, m], f)


def tranferJKS(f, to, n, m=""):
    return pushaction("eosbocai1111", "transfer", [f, to, "%.4f JACKS" % n, m], f)


def tranferZks(f, to, n, m=""):
    return pushaction("zkstokensr4u", "transfer", [f, to, "%.4f ZKS" % n, m], f)


if __name__ == "__main__":
    accounts = getAccounts()
    for i in accounts:
        print(i)
        t = tranferDice(i, "gy2dgmztgqge", 1000)
        logger.info(t)
