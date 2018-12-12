import requests
from transferBalance import transferPraEos, transferEos
from ut import pushaction
import time

s = requests.Session()

blacklist = ["gy2dgmztgqge", "hazdgnryhage"]


def gettable():
    url = "https://proxy.eosnode.tools/v1/{}"

    jsdata = {
        "scope": "bid.game",
        "code": "bid.game",
        "table": "tname",
        "json": True,
        "lower_bound": "",
        "upper_bound": "",
        "limit": 1000,
    }

    z = s.post(url.format("chain/get_table_rows"), json=jsdata)
    t = int(time.time())
    return filter(
        lambda k: k["bidder"] not in blacklist
        and float(k["current_price"].split(" ")[0]) < 5
        and k["length"] <= 5,
        # and k["status"] not in [3, 5],
        z.json()["rows"],
    )


def withdraw():
    print(pushaction("bid.game", "withdraw", ["gy2dgmztgqge"], "gy2dgmztgqge"))


if __name__ == "__main__":

    while True:
        withdraw()
        for i in gettable():
            bidname, bid_count, current_price = (
                i["bidname"],
                i["bid_count"],
                i["current_price"],
            )
            current_price = float(current_price.split(" ")[0])
            if i["length"] == 5:
                if current_price < 0.5:
                    memo = f"bid,{bidname},{bid_count},bbheasxtlatd"
                    print(transferEos("gy2dgmztgqge", "bid.game", current_price, memo))
            elif i["length"] == 4:
                if current_price < 2:
                    memo = f"bid,{bidname},{bid_count},bbheasxtlatd"
                    print(transferEos("gy2dgmztgqge", "bid.game", current_price, memo))
            else:
                if current_price < 5:
                    memo = f"bid,{bidname},{bid_count},bbheasxtlatd"
                    print(transferEos("gy2dgmztgqge", "bid.game", current_price, memo))

        # time.sleep(2)
