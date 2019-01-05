from ut import runPool
from transferBalance import transferEos
import string, random


def genrateRandomName():
    return "".join(random.choices(string.ascii_lowercase, k=10))


def run(a):
    print(
        transferEos(
            "gy2dgmztgqge",
            "hotbetsadmin",
            0.2,
            f"hotdice|gaojin.game|96|{genrateRandomName()}|",
        )
    )


if __name__ == "__main__":
    while True:
        runPool(run, range(1000 * 8))
