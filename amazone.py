import requests
from bs4 import BeautifulSoup
import smtplib
import time
URL = "https://www.amazon.com/dp/B07HH1QSLB/ref=twister_B07HH6X34D?_encoding=UTF8&psc=1"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0"
}

def checkprice():    
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = price[0:5]

    if(converted_price < 1.700):
        send_mail()
    print(converted_price)
    print(title.strip())

    if(converted_price > 1.700):
        send_mail()


def send_mail():
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("enter gmail","enter password")
    subject = "Price fell down!"
    body = "check the amazone link https://www.amazon.com/dp/B07HH1QSLB/ref=twister_B07HH6X34D?_encoding=UTF8&psc=1"

    msg = "subject: {}\n\n{}".format(subject, body)

    server.sendmail(
        "gmail",
        "gmail",
        msg
    )

    print("Hey Email Has Been Sent!")
    server.quit()
while True:
    checkprice()
    time.sleep(60 * 60)

