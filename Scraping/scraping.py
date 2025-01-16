import requests
from bs4 import BeautifulSoup


url = "https://www.ebay.com/sch/i.html?_nkw=macbook+air+m2&_sacat=0&_from=R40&_trksid=p4432023.m570.l1311"

Check = requests.get(url)

print (Check.status_code)