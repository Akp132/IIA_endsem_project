import requests
import json
import os


def fetch_latest_news():
    url = "https://google-news13.p.rapidapi.com/world"
    querystring = {"lr": "en-US"}
    headers = {
        "X-RapidAPI-Key": "5e99b9f592msh3af2b4b80a35946p1e6aa4jsn4717ae405e0e",
        "X-RapidAPI-Host": "google-news13.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    news_data = response.json()

    # Integrating the data to a global source to fetch queries from it later.
    with open('googlenews_data.json', 'w') as file:
        json.dump(news_data, file)
        file.write('\n')

fetch_latest_news()
