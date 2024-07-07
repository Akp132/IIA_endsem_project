import requests
import json
import os

def climateapi_news():
    url = "https://climate-news-feed.p.rapidapi.com/page/1"
    querystring = {"limit":"10"}
    
    headers = {
	"X-RapidAPI-Key": "5e99b9f592msh3af2b4b80a35946p1e6aa4jsn4717ae405e0e",
	"X-RapidAPI-Host": "climate-news-feed.p.rapidapi.com"
}
    #integrating the data to a global source.
    response = requests.get(url, headers=headers)
    with open('climateapi_data.json', 'a') as file:  
        json.dump(response.json(), file)  
        file.write('\n')  

climateapi_news()