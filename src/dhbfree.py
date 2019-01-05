from ut import getAccounts, pushaction, runPool


def run(account):
    print(pushaction("dhboneplay11", "getfree", [account], account))


if __name__ == "__main__":
    accounts = getAccounts()
    runPool(run, accounts)
