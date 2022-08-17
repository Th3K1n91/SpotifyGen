import threading
import concurrent.futures
import time

import requests
import json
import random
import string
from itertools import repeat


class creator:
    def __init__(self, email, passw):
        self.email = email
        self.passw = passw
        self.create()

    def create(self):
        header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br"
        }
        sourcs = requests.get("https://www.spotify.com/de/signup", headers=header).text
        i_id = sourcs.split('spT":"')[1].split('"')[0]
        api_key = sourcs.split('"signupServiceAppKey":"')[1].split('"')[0]

        payload = {
            "account_details": {
                "birthdate": "2000-09-12",
                "consent_flags": {
                    "eula_agreed": "true",
                    "send_email": "false",
                    "third_party_email": "false"
                },
                "display_name": str(self.email).split("@")[0],
                "email_and_password_identifier": {
                    "email": self.email,
                    "password": self.passw
                },
                "gender": 1
            },
            "callback_uri": "https://www.spotify.com/signup/challenge",
            "client_info": {
                "api_key": api_key,
                "app_version": "v2",
                "capabilities": [
                    1
                ],
                "installation_id": i_id,
                "platform": "www"
            },
            "tracking": {
                "creation_flow": "",
                "creation_point": "https://www.spotify.com/de/",
                "referrer": ""
            }
        }
        for i in range(2):
            creat = requests.post("https://spclient.wg.spotify.com/signup/public/v2/account/create", data=json.dumps(payload), headers=header)
            if creat.status_code == 200:
                with threading.Lock():
                    print(f"{self.email}\tSUCCESS")
                    open("Accounts.txt", "a").write(f'{self.email}:{self.passw}\n')
                break
            else:
                print(f"{self.email}\tERROR\t{creat.status_code}")
                time.sleep(5)


if __name__ == "__main__":
    print("\n// Best Results with VPN\n// Email inbox is https://xitroo.de/#[In here the email]\n")
    acc = int(input("How many accounts should be generated: "))
    passw = str(input("Password for all accounts: "))
    thr = int(input("Threads: "))
    accs = list()
    for i in range(acc):
        accs.append("".join(random.choice(string.ascii_letters) for a in range(random.randrange(6, 12, 1))) + "@xitroo.de")
    with concurrent.futures.ProcessPoolExecutor(max_workers=int(thr)) as executor:
        results = executor.map(creator, accs, repeat(passw))