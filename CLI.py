from ast import Dict
from sys import api_version
from typing import Any
import requests
import json
import os
import mysql.connector

from APIs.rapidAPI import rapidapi_news
from mapped_googleapi import transform_googlenews_article

global_schema_template = {
    "Title": "",
    "Source": "",
    "URL": "",
}

def search_specific_news():
    user_query = input("Enter your search query: ")
    rapidapi_news(user_query)
    insert_data_into_db2('rapidapi_data.json', 'rapidapi')
    export_data_to_user_output2('rapidapi_data.json', 'rapidapi')



# Updated function to add Google News data to final JSON file
def add_googlenews_data_to_final_json(googlenews_file: str, final_data_file: str) -> None:
    """
    Transforms Google News articles from the provided JSON file and adds them to the final JSON file.
    
    :param googlenews_file: Path to the JSON file containing Google News articles.
    :param final_data_file: Path to the final JSON file to which the transformed articles will be added.
    """
    # Load Google News data
    with open(googlenews_file, 'r') as f:
        googlenews_data = json.load(f)
    
    # Access the articles directly
    googlenews_articles = googlenews_data.get("items", [])

    # Transform articles
    transformed_articles = []
    for article in googlenews_articles:
        transformed_article = transform_googlenews_article(article)
        transformed_articles.append(transformed_article)

    # # Load existing data from the final JSON file
    # try:
    #     with open(final_data_file, 'r') as f:
    #         final_data = json.load(f)
    # except FileNotFoundError:
    #     final_data = []
    # except json.JSONDecodeError:
    #     final_data = []
    final_data=[]

    # Add transformed articles to the final data
    final_data.extend(transformed_articles)

    # Write the updated data back to the final JSON file
    with open(final_data_file, 'w') as f:
        json.dump(final_data, f)


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

def fetch_news(category):
    print("--kbcbedbcjkbjbcvbv")
    url = f"https://google-news13.p.rapidapi.com/{category}"
    querystring = {"lr": "en-US"}
    headers = {
        "X-RapidAPI-Key": "a1a99df58dmsh928c352854a2c35p124101jsn83d26898ebb2",
        "X-RapidAPI-Host": "google-news13.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    news_data = response.json()

    # Write data to JSON file
    with open('googlenews_data.json', 'w') as file:
        json.dump(news_data, file, indent=4)

    # Call function to insert data into MySQL database
    insert_data_into_db('googlenews_data.json')

    print(f"News in the category '{category}' has been fetched and stored.")

def insert_data_into_db(json_file_path):
    # # MySQL database credentials
    # db_config = {
    #     "host": "localhost",
    #     "user": "root",
    #     "password": "Akshay132",
    #     "database": "IIA"
    # }

    # # Load JSON data
    # with open(json_file_path, 'r') as file:
    #     json_data = json.load(file)

    # # Establish a database connection
    # conn = mysql.connector.connect(**db_config)
    # cursor = conn.cursor()

    # # Create table (if not exists)
    # cursor.execute("CREATE TABLE IF NOT EXISTS googlenews (id INT AUTO_INCREMENT PRIMARY KEY, data JSON)")

    # # Insert data into table
    # insert_query = "INSERT INTO googlenews (data) VALUES (%s)"
    # cursor.execute(insert_query, (json.dumps(json_data),))

    # # Commit the transaction
    # conn.commit()

    # # Close the connection
    # cursor.close()
    # conn.close()


    # File paths
    googlenews_file =  r'/Users/akshay/Desktop/IIA/googlenews_data.json'
    final_data_file = r'/Users/akshay/Desktop/IIA/finaldata.json'

    # Run the function to add Google News data to final JSON file
    add_googlenews_data_to_final_json(googlenews_file, final_data_file)

    # Export data from MySQL table to a user output file
    export_data_to_user_output(final_data_file)

def export_data_to_user_output(json_file_path):
    # # MySQL database credentials
    # db_config = {
    #     "host": "localhost",
    #     "user": "root",
    #     "password": "Akshay132",
    #     "database": "IIA"
    # }

    # # Establish a database connection
    # conn = mysql.connector.connect(**db_config)
    # cursor = conn.cursor()

    # # Select data from table
    # cursor.execute("SELECT data FROM googlenews")
    # rows = cursor.fetchall()

    # # Write data to user output file
    # with open('user_output.json', 'w') as file:
    #     for row in rows:
    #         json.dump(row[0], file, indent=4)

    # # Close the connection
    # cursor.close()
    # conn.close()


    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "Akshay132",
        "database": "IIA"
    }

    # Load JSON data
    file_path = '/Users/akshay/Desktop/IIA/finaldata.json'
    with open(file_path, 'r') as file:
            json_data = json.load(file)

    # Establish a database connection
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Create table (if not exists)
    create_table_query = """
    CREATE TABLE IF NOT EXISTS goooglenews (
        
        title VARCHAR(255),
        source VARCHAR(100),
        url VARCHAR(255) 
    );
    """
    cursor.execute(create_table_query)

    # Insert data into the table
    insert_query = """
    INSERT INTO goooglenews (title, source, url)
    VALUES (%s, %s, %s)
    """
    for item in json_data:
        cursor.execute(insert_query, (item['Title'], item['Source'], item['URL']))

    # Commit the transaction
    conn.commit()

    # Close the connection
    cursor.close()
    conn.close()

    print("Data has been inserted successfully!")


def insert_data_into_db2(json_file_path, category):
    # MySQL database credentials
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "Akshay132",
        "database": "IIA"
    }

    # Load JSON data
    with open(json_file_path, 'r') as file:
        json_data = json.load(file)

    # Establish a database connection
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Create a separate table for each category
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {category}news (id INT AUTO_INCREMENT PRIMARY KEY, data JSON)")

    # Insert data into table
    insert_query = f"INSERT INTO {category}news (data) VALUES (%s)"
    cursor.execute(insert_query, (json.dumps(json_data),))

    # Commit the transaction
    conn.commit()

    # Close the connection
    cursor.close()
    conn.close()

def export_data_to_user_output2(json_file_path, category):
    # MySQL database credentials
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "Akshay132",
        "database": "IIA"
    }

    # Establish a database connection
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Select data from table
    cursor.execute(f"SELECT data FROM {category}news")
    rows = cursor.fetchall()

    # Write data to user output file
    with open('user_output.json', 'w') as file:
        for row in rows:
            json.dump(row[0], file, indent=4)

    # Close the connection
    cursor.close()
    conn.close()




def specific_news():
    while True:
        print("\\nSpecific News Categories:")
        print("1. Crypto News")
        print("2. Sharemarket News")
        print("3. Climate News")
        print("4. Back to Main Menu")

        choice = input("Enter your choice (number): ")
        if choice == '4':
            return  # Return to main menu

        category_map = {
            "1": "crypto",
            "2": "sharemarket",
            "3": "climate"
        }

        chosen_category = category_map.get(choice)
        if chosen_category:
            fetch_and_store_specific_news(chosen_category)
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def fetch_and_store_specific_news(category):
    if category == 'crypto':
        cryptoapi_news()
    elif category == 'sharemarket':
        sharemarketapi_news()
    elif category == 'climate':
        climateapi_news()

    # Insert data into specific table in MySQL database
    insert_data_into_db2(f'{category}api_data.json', category)

    # Export data from MySQL table to a user output file
    export_data_to_user_output2(f'{category}api_data.json', category)


def trending_news():
    while True:
        print("\\nTrending News Categories:")
        print("1. Latest")
        print("2. World")
        print("3. Business")
        print("4. Entertainment")
        print("5. Health")
        print("6. Science")
        print("7. Sport")
        print("8. Technology")
        print("9. Back to Main Menu")

        choice = input("Enter your choice (number): ")
        if choice == '9':
            return  # Return to main menu

        category_map = {
            "1": "latest",
            "2": "world",
            "3": "business",
            "4": "entertainment",
            "5": "health",
            "6": "science",
            "7": "sport",
            "8": "technology"
        }

        chosen_category = category_map.get(choice)
        if chosen_category:
            fetch_news(chosen_category)
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

def main_menu():
    while True:
        print("\\nWelcome to NEWSNET")
        print("Choose an option:")
        print("1. Trending News")
        print("2. Specific News on Climate , Crypto and ShareMarket(Coming Soon)")
        print("3. Search Specific News (Coming Soon)")
        print("4. Exit")

        choice = input("Enter your choice (number): ")
        if choice == '1':
            trending_news()
        elif choice == '2':
            specific_news()
        if choice == '3':
            search_specific_news()
        elif choice == '4':
            print("Exiting NEWSNET. Goodbye!")
            break
        else:
            print("This feature is not available yet. Please choose another option.")

if __name__ == "__main__":
    main_menu()
