from transferBalance import transferEos
import requests
import time
from log import loggingSetting

logger = loggingSetting("farmeos")
s = requests.Session()


def getblance(account):
    url = "http://api.eosbeijing.one/v1/{}"
    z1 = s.post(
        url.format("chain/get_currency_balance"),
        json={"code": "eosio.token", "account": account, "symbol": "EOS"},
    )
    balance = float(z1.json()[0].split()[0])
    return balance


def run(account, balance):
    print(transferEos(account, "farmeosbank1", balance, "bbheasxtlatd 2 4"))


if __name__ == "__main__":
    account = "gy2dgmztgqge"
    logger.info("开始搬砖...")
    count = 0
    # run(account, 10)
    # # 代币：44928.0962
    while True:
        try:
            # balance = getblance(account)
            # if balance < 0:
            #     break
            count += 1
            # logger.info("balance === {}".format(balance))
            # logger.info("本次投注 === {}".format(balance / 100))
            logger.info("count === {}".format(count))
            run(account, 1)
            time.sleep(1)
        except:
            logger.exception("程序bug,正在重试")
            time.sleep(2)
