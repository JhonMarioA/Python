import requests
import os
from dotenv import load_dotenv

load_dotenv()

#import the API_KEY saved in the env
API_KEY = os.getenv("NEWS_API_KEY")
url = "https://newsapi.org/v2/top-headlines"



def search_by_category(category):
    params = { 
       "country": "us",
       "from": "2025-9-25",
       "category": f"{category}",
       "apiKey": API_KEY,
       "pageSize": 2
       }
       
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, params=params, headers=headers)
    return response

def search_by_keyword(key_word):
    params = {
        "country": "us",
        "q": key_word,
        "from": "2025-9-25",
        "apiKey": API_KEY,
        "pageSize": 2
       }
    
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, params=params, headers=headers)
    return response

    
