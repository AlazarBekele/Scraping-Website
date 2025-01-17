import requests
from bs4 import BeautifulSoup


url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"

Check = requests.get(url)

soup = BeautifulSoup(Check.text, "html")
print (soup.div) 
print (Check.status_code) # to check the web is 200