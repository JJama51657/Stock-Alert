import requests
import datetime
from twilio import rest
import os
from load_dotenv import load_env
# Init
Accountid = os.getenv("a")
Accounttoken = os.getenv("b")
newsapikey = os.getenv("c")
newsurl = "https://newsapi.org/v2/everything?"
pars = {
    "QInTitle": "Tesla",
    "apikey": newsapikey
}
response = requests.get(newsurl, params=pars)
newsarts = response.json()
articles = newsarts["articles"]
Na = articles[:3]


paras = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": "04ZXW1DFBARACB67"
}
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?'
r = requests.get(url, params=paras)
data = r.json()
b = datetime.datetime.now()
a = "2025-01-"
dayc = 30
record1 = float(data["Time Series (Daily)"][f"{a}{dayc}"]["4. close"])
record2 = float(data["Time Series (Daily)"][f"{a}{dayc - 1}"]["4. close"])
percent = round(((record1 - record2) / record2) * 100, 2)
print(record1, record2, percent)
if percent > 1:
    client = rest.Client(username=Accountid, password=Accounttoken)
    for article in Na:
        RdsArticles = f"Headline: {article['title']}.\nBrief: {article['description']}"
        print(RdsArticles)
        client.messages.create(from_="+18312082568",
                               to="+447481100168",  body=RdsArticles)
    print(client.account_sid)
