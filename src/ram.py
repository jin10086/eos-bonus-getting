from ut import gettable
import time


def getram():
    x = gettable("eosio", "eosio", "rammarket")
    data = x["rows"][0]
    quote = float(data["quote"]["balance"].split(" ")[0])
    base = float(data["base"]["balance"].split(" ")[0])
    return calram(quote, base)


def calram(quote, base):
    return (quote) / (1 + base / 1024)


if __name__ == "__main__":
    while True:
        time.sleep(2)
        print(getram())
