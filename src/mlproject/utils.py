import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymongo
from pymongo import MongoClient

import pickle
import numpy as np

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
    

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)