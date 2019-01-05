import pickle

from log import loggingSetting
from ut import pushaction
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


def tranferRich(f, to, n, m=""):
    return pushaction("richrich1111", "transfer", [f, to, "%.4f RICH" % n, m], f)


def tranferEUSD(f, to, n, m=""):
    return pushaction("bitpietokens", "transfer", [f, to, "%.8f EUSD" % n, m], f)


def tranferEETH(f, to, n, m=""):
    return pushaction("bitpietokens", "transfer", [f, to, "%.8f EETH" % n, m], f)


def tranferEBTC(f, to, n, m=""):
    return pushaction("bitpietokens", "transfer", [f, to, "%.8f EBTC" % n, m], f)


def tranferJKS(f, to, n, m=""):
    return pushaction("eosbocai1111", "transfer", [f, to, "%.4f JACKS" % n, m], f)


def tranferZks(f, to, n, m=""):
    return pushaction("zkstokensr4u", "transfer", [f, to, "%.4f ZKS" % n, m], f)


def tranferRoy(f, to, n, m=""):
    return pushaction("eosroyaleroy", "transfer", [f, to, "%.4f ROY" % n, m], f)


def tranferBase(code, action, symbol, f, to, n, m="", decimal=4):
    return pushaction(code, action, [f, to, f"%.{decimal}f {symbol}" % n, m], f)


if __name__ == "__main__":
    accounts = getAccounts()
