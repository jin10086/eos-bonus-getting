import pickle

from log import loggingSetting
from ut import pushaction

logger = loggingSetting("transferBalance")


def transferEos(f, to, n, m=""):
    return tranferBase("eosio.token", "EOS", f, to, n, m)


def transferBos(f, to, n, m=""):
    return tranferBase("eosio.token", "BOS", f, to, n, m, node="bos")


def tranferDice(f, to, n, m=""):
    return tranferBase("betdicetoken", "DICE", f, to, n, m)


def tranferRich(f, to, n, m=""):
    return tranferBase("richrich1111", "RICH", f, to, n, m)


def tranferEUSD(f, to, n, m=""):
    return tranferBase("bitpietokens", "EUSD", f, to, n, m, 8)


def tranferEETH(f, to, n, m=""):
    return tranferBase("bitpietokens", "EETH", f, to, n, m, 8)


def tranferEBTC(f, to, n, m=""):
    return tranferBase("bitpietokens", "EBTC", f, to, n, m, 8)


def tranferJKS(f, to, n, m=""):
    return tranferBase("eosbocai1111", "JACKS", f, to, n, m)


def tranferZks(f, to, n, m=""):
    return tranferBase("zkstokensr4u", "ZKS", f, to, n, m)


def tranferRoy(f, to, n, m=""):
    return tranferBase("eosroyaleroy", "ROY", f, to, n, m)


def tranferBase(contract, symbol, f, to, n, m="", decimal=4, node="eos"):
    return pushaction(
        contract, "transfer", [f, to, f"%.{decimal}f {symbol}" % n, m], f, node=node
    )


if __name__ == "__main__":
    accounts = getAccounts()
