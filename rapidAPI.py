import requests
import json
import os

def rapidapi_news(search_query):
    url = "https://news67.p.rapidapi.com/v2/topic-search"
    querystring = {"languages": "en", "search": search_query, "batchSize": "10", "skip": "6"}
    headers = {
        "X-RapidAPI-Key": "5e99b9f592msh3af2b4b80a35946p1e6aa4jsn4717ae405e0e",
        "X-RapidAPI-Host": "news67.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    with open('rapidapi_data.json', 'w') as file:
        json.dump(response.json(), file)
