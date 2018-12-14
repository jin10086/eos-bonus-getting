from ut import runcleos
import json


def _push_transaction(d):
    cmd = [
        "cleos",
        "-u",
        "https://api.eosbeijing.one",
        "push",
        "transaction",
        json.dumps(d),
    ]
    return runcleos(cmd)


def getaction(contract, action, data, f, p=False):
    """
    contract :要玩的合约地址
    action: 玩的方法
    data : 详细信息
    f :账号
    """
    cmd = [
        "cleos",
        "-u",
        "https://api.eosbeijing.one",
        "push",
        "action",
        contract,
        action,
        json.dumps(data),
        "-d",
        "-s",
        "-p",
        f,
    ]
    return json.loads(runcleos(cmd))


def push_transaction(actions):
    """
    actions是 由多个action组成
    每个action由 [合约账号,调用方法,调用参数,签名者] 组成
    """
    # actions = [
    #     ["eosio.token","transfer",["eosbocaira12", "redredredred", "1.0000 EOS", "save"],"eosbocaira12"],
    #     ["eosio.token","transfer",["eosbocaira12", "redredredred", "1.0000 EOS", "save"],"eosbocaira12"],
    #     ["eosio.token","transfer",["eosbocaira12", "redredredred", "1.0000 EOS", "save"],"eosbocaira12"],
    # ]
    for i in range(len(actions)):
        action = getaction(*actions[i])
        if i == 0:
            ret = action
        else:
            ret["actions"].extend(action["actions"])
    return _push_transaction(ret)


if __name__ == "__main__":
    actions = [
        [
            "eosio.token",
            "transfer",
            ["eosbocaira12", "redredredred", "1.0000 EOS", "save"],
            "eosbocaira12",
        ],
        [
            "eosio.token",
            "transfer",
            ["eosbocaira12", "redredredred", "1.0000 EOS", "save"],
            "eosbocaira12",
        ],
        [
            "eosio.token",
            "transfer",
            ["eosbocaira12", "redredredred", "1.0000 EOS", "save"],
            "eosbocaira12",
        ],
    ]
    print(push_transaction(actions))
