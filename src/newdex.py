from ut import pushaction
from transferBalance import tranferBase

to = "newdexpocket"


def run(count, price, account):
    amount = count * price
    memo = {
        "type": "sell-limit",
        "symbol": "fishjoytoken-fish-eos",
        "price": f"{price}",
        "count": f"{count}",
        "amount": f"{amount}",
        "channel": "web",
        "ref": "Scatter",
    }
    data = {
        "from": account,
        "to": to,
        "quantity": "%.4f FISH" % count,
        "memo": f"{memo}",
    }
    print(data)
    print(pushaction("fishjoytoken", "transfer", data, account))


def shijia(count, account):
    memo = {
        "type": "sell-market",
        "symbol": "eosroyaleroy-roy-eos",
        "price": "0.0000000",
        "count": count,
        "amount": 0,
        "channel": "web",
        "ref": "Scatter",
    }
    data = {
        "from": account,
        "to": to,
        "quantity": "%.4f ROY" % count,
        "memo": f"{memo}",
    }
    print(pushaction("eosroyaleroy", "transfer", data, account))


if __name__ == "__main__":
    account = "rrjsgwridops"
    shijia(10000, account)
