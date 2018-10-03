from ut import pushaction
from draw import getAccounts
from log import loggingSetting

logger = loggingSetting("shishicai")


def run():
    """https://lottery.eosplay.co/link"""
    accounts = getAccounts()
    for i in range(5, len(accounts) - 5):
        account = accounts[i]
        if (
            account != "gy2dgmztgqge"
            or account != "acvnbzkffrsl"
            or account != "bbheasxtlatd"
        ):
            if i % 2 == 0:
                memo = "lottery:o@gy2dgmztgqge"
            else:
                memo = "lottery:e@gy2dgmztgqge"
            t = pushaction(
                "eosio.token",
                "transfer",
                [account, "eosplaybrand", "0.1000 EOS", memo],
                account,
            )
            if b"transaction" not in t:
                logger.info("转账失败:{}".format(account))
                logger.info("原因为:{}".format(t))


run()
