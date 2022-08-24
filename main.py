# 1.1.1
import threading, time, requests, json, random, string, sys, os, queue
from PyQt5 import QtWidgets, QtGui, uic

class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('gui.ui', self)
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))
        self.show()
        self.Image.setPixmap(QtGui.QPixmap("images/logo.png"))
        self.start.clicked.connect(self.st)
        self.Name.mousePressEvent = self.pr
        self.Image.mousePressEvent = self.pr
        self.Github.mousePressEvent = self.gt

    def gt(self, event):
        os.system("start https://github.com/Th3K1n91/SpotifyGen")

    def pr(self, event):
        os.system("start https://cracked.io/insuckablyat88")

    def st(self):
        if self.count.text() and self.password.text() and self.threads.text() != "":
            if len(self.password.text()) >= 8:
                print("Please Wait")
                for i in range(int(self.count.text())): q.put("".join(random.choice(string.ascii_letters) for _ in range(random.randint(8,14))) + "@xitroo.de")
                while True:
                    for i in range(int(self.threads.text())):
                        t = threading.Thread(target=creator(email=q.get(), passw=self.password.text()).create, args=())
                        threads.append(t)
                        t.start()
                    if q.empty() == True: break
                    for t in threads: t.join()

class creator:
    def __init__(self, email: str, passw: str):
        self.email = email
        self.passw = passw

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
        creat = requests.post("https://spclient.wg.spotify.com/signup/public/v2/account/create", data=json.dumps(payload), headers=header)
        if creat.status_code == 200:
            with threading.Lock():
                print(f"{self.email}\tSUCCESS")
                open("Accounts.txt", "a").write(f'{self.email}:{self.passw}\n')
        else:
            print(f"{self.email}\tERROR\t{creat.status_code}")
            time.sleep(5)


if __name__ == "__main__":
    # Vars
    q = queue.Queue()
    threads = list()
    # Start App
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()