import requests
from bs4 import BeautifulSoup
import sqlite3
import random
import time


conn = sqlite3.connect("moneyData.db")
courses = ["usd", "eur", "pln"]
cursor = conn.cursor()
url = "https://minfin.com.ua/ua/currency/"
def getMoney(course):
    req = requests.get(url+course)
    soup = BeautifulSoup(req.text, "html_parser")
    elements = soup.find_all("span", class_="nfn-posr")
    money = []
    for k in elements:
        summa = str(k).split('<span class ="nfn-posr">')[1].split("\n"[0])
        money.append(float(summa))
        print(money)
    cursor.execute(" insert into money values (?,?,?,?,?,?,?,?)",(random.randint(-100000, 1000000), course, money, time.ctime()))
    conn.commit()
    print(f"{course}os updated")

for k in courses:
    getMoney(courses[0])
