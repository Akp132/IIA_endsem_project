import json
from typing import Dict, List

# Global schema template
global_schema_template = {
    "Title": "",
    "Source": "",
    "URL": "",
    "PublishedAt": "",
    "Image": "",
}

def transform_rapidapi_article(article: Dict) -> Dict:
    """
    Transforms an article from the Rapid API format to the global schema format.
    """
    transformed_article = global_schema_template.copy()
    
    transformed_article["Title"] = article.get("Title", "unknown")
    transformed_article["Source"] = article.get("Source", "unknown")
    transformed_article["URL"] = article.get("Url", "unknown")
    transformed_article["PublishedAt"] = article.get("PublishedOn", "unknown")
    transformed_article["Image"] = article.get("Image", "unknown")
    
    return transformed_article

def add_rapidapi_data_to_final_json(rapidapi_file: str, final_data_file: str) -> None:
    """
    Reads data from the specified Rapid API JSON file, transforms the articles based on the global schema,
    and appends the data to the final JSON file.

    :param rapidapi_file: Path to the Rapid API JSON file.
    :param final_data_file: Path to the final JSON file.
    """
    # Read data from Rapid API JSON file
    with open(rapidapi_file, 'r') as f:
        rapidapi_data = json.load(f)
    
    # Extract articles from Rapid API data
    articles = rapidapi_data.get("news", [])
    
    # Transform articles based on the global schema
    transformed_articles = [transform_rapidapi_article(article) for article in articles]
    
    # Read existing data from final JSON file
    try:
        with open(final_data_file, 'r') as f:
            final_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        final_data = []
    
    # Append new data to final JSON file
    final_data.extend(transformed_articles)
    with open(final_data_file, 'w') as f:
        json.dump(final_data, f)
# File paths
rapidapi_file =  r'C:\Users\mukes\OneDrive\Desktop\IIA_Project\rapidapi_data.json'
final_data_file = r'C:\Users\mukes\OneDrive\Desktop\IIA_Project\finaldata.json'

# Run the function to add Rapid API data to final JSON file
add_rapidapi_data_to_final_json(rapidapi_file, final_data_file)

# Return the path to the output file
final_data_file
