import sqlite3
import pandas

# Connect to SQL database
db = "database.sqlite"
connect = sqlite3.connect(db)

# Extract and clean all match (columns)
data = """SELECT * Match"""
df_data = pandas.read_sql_query(data, connect)

# Save to csv
cleaned_data_csv = "cleaned_match_data.csv"
df_data.to_csv(cleaned_data_csv, index = False)

connect.close()