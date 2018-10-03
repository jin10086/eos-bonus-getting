import pickle

from log import loggingSetting
from ut import pushaction

logger = loggingSetting("transferBalance")
with open("tmpaccount.pkl", "rb") as f:
    accounts = pickle.load(f)


def transferEos(f, to):
    return pushaction("eosio.token", "transfer", [f, to, "0.1000 EOS", ""], f)


for i in accounts:
    print(i)
    t = transferEos("gy2dgmztgqge", i)
    logger.info(t)
