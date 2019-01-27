from transactions import push_transaction

from ut import runPool


def sell(q):
    qq = "%.4f MEV" % q
    actions = [
        [
            "eosvegascoin",
            "transfer",
            ["gy2dgmztgqge", "findexfindex", qq, ""],
            "gy2dgmztgqge",
        ],
        [
            "findexfindex",
            "sellorder",
            {
                "r_sell_order": {
                    "seller": "gy2dgmztgqge",
                    "pair_id": "89",
                    "quote_quantity": qq,
                    "minimum_price": "1000000",
                    "remark": "bitpie4users",
                }
            },
            "gy2dgmztgqge",
        ],
    ]
    print(push_transaction(actions))


def buy(q, q1):
    qq = "%.8f EUSD" % q
    qq1 = "%.4f MEV" % q1
    actions = [
        [
            "bitpietokens",
            "transfer",
            ["gy2dgmztgqge", "findexfindex", qq, ""],
            "gy2dgmztgqge",
        ],
        [
            "findexfindex",
            "buyorder",
            {
                "r_buy_order": {
                    "buyer": "gy2dgmztgqge",
                    "pair_id": "89",
                    "quote_quantity": qq1,
                    "maximum_price": "1000000",
                    "remark": "bitpie4users",
                }
            },
            "gy2dgmztgqge",
        ],
    ]
    print(push_transaction(actions))


def run(a):
    sell(101)
    buy(1.01, 101)


if __name__ == "__main__":
    while True:
        runPool(run, [0 for i in range(1000)])
    # while True:
    # sell(101)
    # buy(1.01, 101)
