import pymongo

# Replace <password> with your actual password and adjust the URI as necessary
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Access the database (replace 'your_database_name' with your actual database name)
db = client["pyproject"]  # For example, using the 'local' database

# Example: Access a collection (replace 'your_collection_name' with the actual collection name)
collection = db["students"]  # Replace with your collection name

# Print a confirmation message
print("Connected to the database!")
