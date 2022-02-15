from pymongo import MongoClient
from pprint import pprint

MONGO_USER = "root"
MONGO_PASSWORD = "example"
MONGO_ENDPOINT = "172.17.0.1:27017"
mongo_client = MongoClient(f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_ENDPOINT}/")
pprint(f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_ENDPOINT}/")
db = mongo_client["db"]
collection = db["project"]
# Issue the serverStatus command and print the results

res = list(collection.find({}))
pprint(res)
