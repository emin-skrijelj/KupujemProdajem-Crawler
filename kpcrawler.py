import re
import time
import smtplib
import requests

from sys import argv as arguments

headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"}

# Regular expressions
matchUrl = r'''<a href..(.+)".class="adName"''' # https://www.kupujemprodajem.com/ + match[0]

matches = []

def main():
    url = "https://www.kupujemprodajem.com/najnoviji/1"
    while True:
        message = ""
        req = requests.get(url,headers=headers).text
        matches = re.findall(matchUrl,req)
        for match in matches:
            message += match + "\n"
    # Email -> 1 Password -> 2 Reciver -> 3
        try:
            client = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            client.ehlo()
            client.login(arguments[1],arguments[2])
            client.sendmail(arguments[1],arguments[3],message)
            client.close()
            print("message sent")
        except Exception as f:
            print(f)
        time.sleep(180)

if __name__ == "__main__":
    if(len(arguments) != 4):
        print("usage\npython main.py email password reciver-email")
    else:
        main()
