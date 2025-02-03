# Who is the greatest player from the era, 2007-2016?


import sqlite3
import pandas as pd

db = "SoccerAnalyticsDatabase/european_soccer_database.sqlite"
connect = sqlite3.connect(db)
cursor = connect.cursor()

cursor.execute("DROP TABLE IF EXISTS GreatestPlayers;")
connect.commit()

top_players_table = """
CREATE TABLE IF NOT EXISTS GreatestPlayers AS
SELECT 
    p.id,
    p.player_name,
    p.birthday,
    MAX(pa.overall_rating) AS best_overall,
    MAX(pa.potential) AS highest_potential,
    pa.date
FROM Player AS p
JOIN Player_Attributes AS pa ON p.player_api_id = pa.player_api_id
JOIN Match AS m ON pa.date = m.date
JOIN League AS l ON m.country_id = l.country_id
WHERE pa.overall_rating IS NOT NULL
GROUP BY p.player_name
ORDER BY best_overall DESC, highest_potential DESC
LIMIT 25;
"""

cursor.execute(top_players_table)
connect.commit()

df_verification = pd.read_sql_query("SELECT * FROM GreatestPlayers LIMIT 25;", connect)
print(df_verification)

connect.close()