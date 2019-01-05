import json

import redis
import requests
from pymongo import MongoClient
import pymongo


class Data:

    def __init__(self, account_name):
        self.url = "https://proxy.eosnode.tools/v1/{}"
        # self.url = "https://api-kylin.eosasia.one/v1/{}"
        self.s = requests.Session()
        self.s.headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
        }
        self.account_name = account_name
        self.m = db = MongoClient()["jacks"]

    def getAction(self, pos=0, offset=500):
        print("get ", pos)
        data = self.postData(
            self.url.format("history/get_actions"),
            data={"pos": pos, "offset": offset, "account_name": self.account_name},
        )
        if data.get("actions"):
            return data
        return {"actions": []}

    def getdata(self, lastPos=0, offset=100):
        while True:
            _data = self.getAction(pos=lastPos, offset=offset)["actions"]
            if not _data:
                return
            _lastPos = _data[-1]["account_action_seq"] + 1
            if _lastPos < lastPos + offset:  # lastPos是上一次的，_lastPos是拿到数据最后的一条
                self.mongoclient.insert_many(_data)
                return
            else:
                self.mongoclient.insert_many(_data)
                lastPos = _lastPos

    def postData(self, url, data):
        return self.s.post(url, json=data).json()

    def pickleData(self, kname, data):
        self.r.set(kname, json.dumps(data))

    def run(self, dbclean=False, offset=100, lastpos=0):
        kname = "{}_alldata".format(self.account_name)
        d = self.m[kname]
        self.mongoclient = d
        a = (
            self.mongoclient.find({}, {"account_action_seq": 1})
            .sort("account_action_seq", pymongo.DESCENDING)
            .limit(1)
        )
        if a.count():
            lastpos = a[0]["account_action_seq"]
        else:
            lastpos = 0

        self.getdata(offset=offset, lastPos=lastpos)


import os, sys, time


def main():
    print("AutoRes is starting")
    c = Data("gaojin.game")
    c.run(offset=500)

    executable = sys.executable
    args = sys.argv[:]
    print(args)
    args.insert(0, sys.executable)

    time.sleep(1)
    print("Respawning")
    os.execvp(executable, args)


if __name__ == "__main__":
    #
    main()
