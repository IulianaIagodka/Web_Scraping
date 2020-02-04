import json
import requests
from bs4 import BeautifulSoup

TOKEN = "1015415531:AAGLP49ZJjWPXvPkL-Qh6ljyBnDYvWp0Ddo"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
url_news = "https://towardsdatascience.com/"


r1 = requests.get(url_news)
coverpage = r1.content
soup1 = BeautifulSoup(coverpage, "html5lib")
coverpage_news = soup1.find_all("h3", class_="u-contentSansBold u-lineHeightTightest u-xs-fontSize24 u-paddingBottom2 u-paddingTop5 u-fontSize32")
first_new = coverpage_news[0].get_text()
#print(first_new)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


text, chat = get_last_chat_id_and_text(get_updates())
#send_message(text, chat)
send_message(f"{first_new}", chat)
#print (text)