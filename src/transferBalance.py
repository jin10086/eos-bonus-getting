import pickle

from log import loggingSetting
from ut import pushaction

logger = loggingSetting("transferBalance")
with open("tmp.pkl", "rb") as f:
    accounts = pickle.load(f)


def transferEos(f, to):
    return pushaction("eosio.token", "transfer", [f, to, "0.2000 EOS", ""], f)


if __name__ == "__main__":
    for i in accounts:
        print(i)
        t = transferEos("gy2dgmztgqge", i)
        logger.info(t)
