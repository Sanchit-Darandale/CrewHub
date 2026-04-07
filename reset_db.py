from pymongo import MongoClient
from config import Config

def reset_database():
    """
    Clears all collections from the MongoDB database
    Collections: users, workers, appointments, reviews, reports
    """
    try:
        print(f"Connecting to MongoDB URI...")
        client = MongoClient(Config.MONGO_URI)
        db = client[Config.MONGO_DB_NAME]
        
        # List of collections to clear
        collections = ['users', 'workers', 'appointments', 'reviews', 'reports']
        
        print(f"Database: {Config.MONGO_DB_NAME}")
        print("-" * 30)
        
        for coll_name in collections:
            count = db[coll_name].count_documents({})
            print(f"Dropping {coll_name} ({count} documents)...")
            db[coll_name].drop()
            
        print("-" * 30)
        print("Success! All data has been deleted from the database.")
        client.close()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("! WARNING: This will permanently delete ALL users, workers, appointments, and reviews !")
    confirm = input("Confirm database reset? (y/n): ")
    if confirm.lower() == 'y':
        reset_database()
    else:
        print("Operation cancelled.")
