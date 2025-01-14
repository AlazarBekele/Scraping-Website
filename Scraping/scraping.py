import requests
from bs4 import BeautifulSoup

from telegram import Bot

def scrap_data (url):

    try:
        respose = requests.get(url)
        if respose.status_code == 200:

            soup = BeautifulSoup(respose.content, 'body.html')
            data = soup.find('title').text
            return data
        
        else:

            return "Failed to fetch data: Invalid status code"
        
    except Exception as e:
        
        return f"Error: {str(e)}"