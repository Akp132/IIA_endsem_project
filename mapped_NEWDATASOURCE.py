import json
from typing import List, Dict, Any, Callable

# Global schema template
global_schema_template = {
    "Title": "",
    "Source": "",
    "URL": "",
    "PublishedAt": "",
    "Image": "",
}

# Function to transform article data to match the global schema
def transform_article(article: Dict[str, Any], source_transformer: Callable[[Dict[str, Any]], Dict[str, str]]) -> Dict[str, str]:
    return source_transformer(article)

# Sample transformation function for a new data source
def transform_new_source(article: Dict[str, Any]) -> Dict[str, str]:
    transformed_article = global_schema_template.copy()
    # Add transformation logic here based on the structure of the data from the new source
    # For example:
    transformed_article["Title"] = article.get("titleField", "unknown")
    transformed_article["Source"] = "NewSource"  # or retrieve from the article if available
    transformed_article["URL"] = article.get("urlField", "unknown")
    transformed_article["PublishedAt"] = article.get("dateField", "unknown")
    transformed_article["Image"] = article.get("imageField", "unknown")
    return transformed_article

# Function to add data from a new source to the final JSON file
def add_data_from_new_source(json_file: str, final_data_file: str, source_transformer: Callable[[Dict[str, Any]], Dict[str, str]]) -> None:
    # Load data from the new source
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Extract articles and transform them to match the global schema
    articles = data.get("articles", [])  # Adjust the key as needed based on the structure of the new source's data
    transformed_articles = [transform_article(article, source_transformer) for article in articles]
    
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

# Function to remove data from a specific source from the final JSON file
def remove_data_from_source(final_data_file: str, source_name: str) -> None:
    # Load existing data from the final JSON file
    try:
        with open(final_data_file, 'r') as f:
            final_data = json.load(f)
    except FileNotFoundError:
        final_data = []
    except json.JSONDecodeError:
        final_data = []

    # Remove articles from the specified source
    final_data = [article for article in final_data if article.get("Source") != source_name]

    # Write the updated data back to the final JSON file
    with open(final_data_file, 'w') as f:
        json.dump(final_data, f)

# Example usage
add_data_from_new_source('path_to_new_source_data.json', 'finaldata.json', transform_new_source)
remove_data_from_source('finaldata.json', 'NewSource')
