import sqlite3
import pandas as pd

db = "SoccerAnalyticsDatabase/european_soccer_database.sqlite"
connect = sqlite3.connect(db)
cursor = connect.cursor()

cursor.execute("DROP TABLE IF EXISTS Greatest_Players;")
connect.commit()

top_players_table = """
CREATE TABLE IF NOT EXISTS Greatest_Players AS
SELECT 
    p.id,
    p.player_name,
    p.birthday,
    MAX(pa.overall_rating) AS best_overall,
    MAX(pa.potential) AS highest_potential,
    pa.date,
    (CAST(strftime('%Y', pa.date) AS INTEGER) - CAST(strftime('%Y', p.birthday) AS INTEGER)) AS age_at_prime
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

df_verification = pd.read_sql_query("SELECT * FROM Greatest_WhePlayers LIMIT 25;", connect)
print(df_verification)

# Copy table and make a new one for team stat analysis.

# Then, compare the two and come up with a conclusion as to who is the best player.

# Attain each of these tables and label the last one as your final one

connect.close()