from urllib.request import urlopen
from bs4 import BeautifulSoup
import lxml

url = "http://www.hubertiming.com/results/2017GPTR10K"
html = urlopen(url)

soup = BeautifulSoup(html, 'lxml')

# Get the title
title = soup.title
print(title)

# Print out the text
text = soup.get_text()
#print(soup.text)