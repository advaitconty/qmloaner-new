import pandas as pd
from pymongo import MongoClient
import secret as secrets
import certifi

def send_data():
    mongo_url = secrets.mongo_host_connection("admin", "admin", default=True)
    database_name = "inventory"
    collection_name = "inventory"
    csv_file_path = "inventory.csv"

    # Pass certifi certificate for SSL verification
    client = MongoClient(mongo_url, ssl=True, tlsCAFile=certifi.where())  # Add SSL and certificate params
    db = client[database_name]
    collection = db[collection_name]
    df = pd.read_csv(csv_file_path)

    data = df.to_dict(orient='records')

    for item in range(len(data)):
        for key, value in data[item].items():
            if key == "S/N":
                data[item]["S/N"] = int(value)


    collection.insert_many(data)
    print("Data sent successfully!")


def ping():
    client = MongoClient(secrets.mongo_host_connection("admin", "admin"), ssl=True, tlsCAFile=certifi.where())
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    send_data()
