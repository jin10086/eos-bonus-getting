from ut import runPool, genrateRandomN
from transferBalance import transferEos


def run(a):
    print(
        transferEos(
            "gy2dgmztgqge",
            "richrich2222",
            2.5,
            f"playdice|{genrateRandomN()}-1-96-gaojin.game",
        )
    )


if __name__ == "__main__":
    while True:
        run(1)
        # runPool(run, range(8 * 1000))
