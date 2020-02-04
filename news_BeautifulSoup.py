# importing necessary packages
import requests
from bs4 import BeautifulSoup

url = "https://towardsdatascience.com/"

r1 = requests.get(url)
coverpage = r1.content

soup1 = BeautifulSoup(coverpage, "html5lib")

coverpage_news = soup1.find_all("h3", class_="u-contentSansBold u-lineHeightTightest u-xs-fontSize24 u-paddingBottom2 u-paddingTop5 u-fontSize32")
first_new = coverpage_news[0].get_text()
print(first_new)
