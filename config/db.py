import os
from pymongo import MongoClient

MONGODB_URL= os.environ["MONGODB_URL"]

conn = MongoClient(MONGODB_URL).wpl