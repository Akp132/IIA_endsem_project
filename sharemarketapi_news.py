import requests
import json
import os

def sharemarketapi_news():
    url = "https://share-market-news-api-india.p.rapidapi.com/marketNews"
   
    headers = {
	"X-RapidAPI-Key": "5e99b9f592msh3af2b4b80a35946p1e6aa4jsn4717ae405e0e",
	"X-RapidAPI-Host": "share-market-news-api-india.p.rapidapi.com"
}
    #integrating the data to a global source.
    response = requests.get(url, headers=headers, )
    with open('sharemarketapi_data.json', 'a') as file:  
        json.dump(response.json(), file)  
        file.write('\n')  

sharemarketapi_news()