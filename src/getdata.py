import json

import redis
import requests


class Data:

    def __init__(self, account_name, r=None):
        self.url = "https://proxy.eosnode.tools/v1/{}"
        # self.url = "https://api-kylin.eosasia.one/v1/{}"
        self.s = requests.Session()
        self.s.headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
        }
        self.account_name = account_name
        if r:
            self.r = r
            print("use set redis ")
        else:
            self.r = redis.Redis(db=1)

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
            self.data.extend(_data)
            _lastPos = _data[-1]["account_action_seq"] + 1
            if _lastPos < lastPos + offset:  # lastPos是上一次的，_lastPos是拿到数据最后的一条
                d = {"data": self.data, "lastPos": _lastPos}
                self.pickleData("{}_alldata".format(self.account_name), d)
                return
            else:
                d = {"data": self.data, "lastPos": _lastPos}
                self.pickleData("{}_alldata".format(self.account_name), d)
                lastPos = _lastPos

    def postData(self, url, data):
        return self.s.post(url, json=data).json()

    def pickleData(self, kname, data):
        self.r.set(kname, json.dumps(data))

    def run(self, dbclean=False):
        kname = "{}_alldata".format(self.account_name)
        if dbclean:
            self.r.delete(kname)
        d = self.r.get(kname)
        if d:
            data = json.loads(d)
            self.data = data["data"]
            self.getdata(lastPos=data["lastPos"])
        else:
            self.data = []
            self.getdata()


if __name__ == "__main__":
    c = Data("betdicelucky")
    c.run()
