from ut import runPool
from transferBalance import transferEos, tranferKar, tranferEUSD
import random
import string


def genrateRandomName():
    return "".join(random.choices(string.ascii_lowercase, k=12))


def run(a):
    memo = f"action:bet,seed:{genrateRandomName()},rollUnder:96,ref:bbheasxtlatd"
    f = "gy2dgmztgqge"
    t = "betdiceadmin"
    print(tranferEUSD(f, t, 10, memo))


if __name__ == "__main__":
    x = range(10000)
    runPool(run, x)
