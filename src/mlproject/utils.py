import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymongo
from pymongo import MongoClient

load_dotenv()

host=os.getenv("host")
port=os.getenv("port")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv('mlproject')

def read_mongodb_data():
    logging.info("Reading Mongodb database started")
    try:
        client = MongoClient() # Connection happen OR client = MongoClient("mongodb://localhost:27017/")
        
        db = client.mlProject # Getting a database
        logging.info("Connection established", db)

        collection=db.Tables
        df=pd.DataFrame(list(collection.find()))
        print(df)

        return df


    except Exception as e:
        raise CustomException(e)