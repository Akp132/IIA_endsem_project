import mysql.connector
import json

# MySQL database credentials
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
CREATE TABLE IF NOT EXISTS articles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    source VARCHAR(100),
    url VARCHAR(255),
    published_at VARCHAR(20),
    image_url VARCHAR(255)
);
"""
cursor.execute(create_table_query)

# Insert data into the table
insert_query = """
INSERT INTO articles (title, source, url, published_at, image_url)
VALUES (%s, %s, %s, %s, %s)
"""
for item in json_data:
    cursor.execute(insert_query, (item['Title'], item['Source'], item['URL'], item['PublishedAt'], item['Image']))

# Commit the transaction
conn.commit()

# Close the connection
cursor.close()
conn.close()

print("Data has been inserted successfully!")
