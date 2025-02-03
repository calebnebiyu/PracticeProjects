import sqlite3
import pandas

db_path = "SoccerAnalyticsDatabase\european_soccer_database.sqlite"
connect = sqlite3.connect(db_path)

tables_query = "SELECT name FROM sqlite_master WHERE type='table';"
tables_df = pandas.read_sql_query(tables_query, connect)
table_names = tables_df['name'].tolist()
print("Tables in database:", table_names)

for table in table_names:
    query = f"PRAGMA table_info({table});"
    df = pandas.read_sql_query(query, connect)
    print(f"Columns in {table}:\n", df['name'])

connect.close()