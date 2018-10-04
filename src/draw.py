import os
import json
from log import loggingSetting
from ut import pushaction, unlock, getAccounts
import pickle

logger = loggingSetting("draw")


def main(password):
    x = getAccounts()
    unlock(password)
    for i in x:
        print(pushaction("betdicelucky", "draw", [i], i))


if __name__ == "__main__":
    password = "1"
    main(password)
