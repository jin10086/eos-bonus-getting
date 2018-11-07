import requests
import time

url = "https://wj.qq.com/sur/collect_answer"


def step1():
    s = requests.Session()


def run(account):
    data = {
        "survey_id": "2866323",
        "answer_survey": {
            "id": "2866323",
            "survey_type": 0,
            "jsonLoadTime": 41,
            "ldw": "CD60C279-456B-48A2-AF3A-BDBBB9C24890",
            "time": int(time.time()),
            "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
            "openid": "",
            "pages": [
                {
                    "id": "1",
                    "questions": [
                        {
                            "id": "q-1-1DMP",
                            "type": "text",
                            "text": f"{account}",
                            "options": [],
                            "blanks": [],
                        }
                    ],
                }
            ],
            "referrer": "",
        },
    }
    z = requests.post(
        "https://wj.qq.com/sur/collect_answer",
        json=data,
        headers={
            "referer": "https://wj.qq.com/s/2866323/16df/?from=groupmessage&isappinstalled=0",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
        },
    )
    print(z.json())


if __name__ == "__main__":
    from ut import getAccounts, runPool

    accounts = getAccounts()
    runPool(run, accounts)
