from sqlalchemy import create_engine

#url for fleed.db database file is the current folder
DB_URL = "sqlite:///fleet.db"

#create the database and establish connection
engine = create_engine(DB_URL)

#encapsulation to not expose the variable
def get_engine():
    return engine