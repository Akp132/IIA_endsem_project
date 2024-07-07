import requests
import json
import os

api_key = '9553aa68c5e549efb9598358924f6fdb'  # Using an environment variable to store the API key

def news():
    main_url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={api_key}"
    news = requests.get(main_url).json()
    
    #integrating the data to a global source to fetch queries from it later.
    

    with open('newsapi_data.json', 'a') as file:  # Open the file in append mode
        json.dump(news, file)  # Write the JSON data to the file
        file.write('\n')  # Write a newline character to the file, so that each API call's data is on a new line

news()
