import json
from typing import Dict, Any, List

# Global schema template
global_schema_template = {
    "Title": "",
    "Source": "",
    "URL": "",
}

def transform_googlenews_article(article: Dict[str, Any]) -> Dict[str, str]:
    """
    Transforms an article from the Google News format to the global schema format.
    """
    transformed_article = global_schema_template.copy()
    
    transformed_article["Title"] = article.get("title", "unknown")
    transformed_article["Source"] = article.get("publisher", "unknown")
    transformed_article["URL"] = article.get("newsUrl", "unknown")
    # transformed_article["PublishedAt"] = article.get("timestamp", "unknown")
    # transformed_article["Image"] = article.get("images", {}).get("thumbnail", "unknown") if isinstance(article.get("images"), dict) else "unknown"
    
    return transformed_article

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

    # Load existing data from the final JSON file
    try:
        with open(final_data_file, 'r') as f:
            final_data = json.load(f)
    except FileNotFoundError:
        final_data = []
    except json.JSONDecodeError:
        final_data = []

    # Add transformed articles to the final data
    final_data.extend(transformed_articles)

    # Write the updated data back to the final JSON file
    with open(final_data_file, 'w') as f:
        json.dump(final_data, f)

# File paths
googlenews_file =  r'/Users/akshay/Desktop/IIA/googlenews_data.json'
final_data_file = r'/Users/akshay/Desktop/IIA/finaldata.json'

# Run the function to add Google News data to final JSON file
add_googlenews_data_to_final_json(googlenews_file, final_data_file)

# Return the path to the output file
final_data_file
