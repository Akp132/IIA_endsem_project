import requests
import json
import os

def cryptoapi_news():
    url = "https://crypto-news34.p.rapidapi.com/news/cryptonews"
    querystring = {"lang":"en"}
    headers = {
	"X-RapidAPI-Key": "5e99b9f592msh3af2b4b80a35946p1e6aa4jsn4717ae405e0e",
	"X-RapidAPI-Host": "crypto-news34.p.rapidapi.com"
}
    #integrating the data to a global source.
    response = requests.get(url, headers=headers, params=querystring)
    with open('cryptoapi_data.json', 'a') as file:  
        json.dump(response.json(), file)  
        file.write('\n')  

cryptoapi_news()