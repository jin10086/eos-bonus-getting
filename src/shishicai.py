from ut import pushaction
from ut import getAccounts
from log import loggingSetting

logger = loggingSetting("shishicai")


def run(ref):
    """https://lottery.eosplay.co/link"""
    accounts = getAccounts()
    for i in range(0, len(accounts)):
        account = accounts[i]
        if i % 2 == 0:  # lottery:o,lottery:e 一个是猜单，一个是猜双，这段代码的目的是 55开，这样可以保证2次肯定有一次赢.
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
        else:
            print("{} 操作成".format(account))


if __name__ == "__main__":
    run("gy2dgmztgqge")
