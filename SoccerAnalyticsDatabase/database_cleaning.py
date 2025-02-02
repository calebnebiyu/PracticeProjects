import sqlite3
import pandas

db = "database.sqlite"
connect = sqlite3.connect(db)

query = "SELECT name FROM sqlite_master WHERE type = 'table'"
df = pandas.read_sql_query(query, connect)
table_names = df['name'].tolist()

merged_data = []

for table in table_names:
    df = pandas.read_sql_query(f"SELECT * FROM {table}", connect)
    df["table_name"] = table
    merged_data.append(df)

final_df = pandas.concat(merged_data, ignore_index = True)

cleaned_data_csv = "leaned_soccer_data.csv"
final_df.to_csv(cleaned_data_csv, index = False)

connect.close()

cleaned_data_csv