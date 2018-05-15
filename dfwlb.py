# dfwlb
import time
import requests

login = "" # credentials

def dfwlb():
    r = requests.post("https://172.16.48.1", data={"x509policy": "", "x509subject": "", "x509issuer": "", "x509altname": "", "user": login, "password": login, "origin": "Login"}, verify=False)
    

while True:
    dfwlb()
    time.sleep(21600) # 6 hours
