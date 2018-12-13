from ut import runPool

from transferBalance import transferEos
import random
import string
import time


def run():
    f = "gy2dgmztgqge"
    t = "betsandrou11"

    memo = "jB5|jA5,df89268a3ab52962a2b58fa4f2ab65d1c1d0a99a,167a7764ab4,gaojin.game"
    print(transferEos(f, t, 1, memo))


def genrateRandomName():
    return "".join(random.choices(string.ascii_lowercase, k=12))


if __name__ == "__main__":
    while True:
        time.sleep(0.51)
        run()
