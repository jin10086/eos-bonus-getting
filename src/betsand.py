from ut import runPool

from transferBalance import transferEos
import random
import string
import time


def run():
    f = "gaojin.game"
    t = "betsandrou11"

    memo = "jB5|jA5,cd4c87e232a7ae0b0aa9697b13efb021c6ba9020,167a81a76e1,gy2dgmztgqge"
    print(transferEos(f, t, 1, memo))


def genrateRandomName():
    return "".join(random.choices(string.ascii_lowercase, k=12))


if __name__ == "__main__":
    while True:
        time.sleep(0.511)
        run()
