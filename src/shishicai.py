from ut import pushaction
from draw import getAccounts
from log import loggingSetting

logger = loggingSetting("shishicai")


def run(ref):
    """https://lottery.eosplay.co/link"""
    accounts = getAccounts()
    for i in range(5, len(accounts) - 5):
        account = accounts[i]
        if i % 2 == 0:
            memo = "lottery:o@{}".format(ref)
        else:
            memo = "lottery:e@{}".format(ref)
        t = pushaction(
            "eosio.token",
            "transfer",
            [account, "eosplaybrand", "0.1000 EOS", memo],
            account,
        )
        if b"transaction" not in t:
            logger.info("转账失败:{}".format(account))
            logger.info("原因为:{}".format(t))


run("gy2dgmztgqge")
