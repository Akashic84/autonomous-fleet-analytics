import pandas as pd
from db import get_engine

#returns the database connection to fleet.db
engine = get_engine()

#load csv file with trip data to data frame
df = pd.read_csv("data/sample_trips.csv")

df.to_sql(
    "trips",             #table name
    engine,              #database connection
    if_exists="replace", #delete existing table and create a new one
    index=False          #trip_id column will be the index
)

print("Trips imported successfully")