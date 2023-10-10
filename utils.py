from pymongo import MongoClient

def get_db_handle(db_name, host, port, username, password):

    client = MongoClient(host="raymann", port=int("27017"), username="geoffrey", password="Raymann@2050")

    db_handle = client['tennis']
    return db_handle, client