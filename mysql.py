from sqlalchemy import create_engine 
import pandas as pd 
from dotenv import load_dotenv
import os  

load_dotenv()

# Get environment variables
username = os.getenv('username')
password = os.getenv('password')
host = os.getenv('hostaddress')

# Define your connection string for MySQL
database_URL = f'mysql+pymysql://{username}:{password}@{host}:3306/life'

# Create the engine
engine = create_engine(database_URL)


#Now we are going to import fake data