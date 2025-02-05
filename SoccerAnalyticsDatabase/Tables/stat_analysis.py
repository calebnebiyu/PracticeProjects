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
df_check_top_players_table = pd.read_sql_query("SELECT * FROM Greatest_Players LIMIT 25;", connect)
print(df_check_top_players_table)


cursor.execute("DROP TABLE IF EXISTS Shooting_Stats;")
connect.commit()
shooting_stats_table = """
CREATE TABLE Shooting_Stats AS
SELECT 
    p.player_name,
    MAX(pa.finishing) AS best_finishing,
    pa.shot_power,
    pa.long_shots,
    pa.curve,
    pa.penalties
    pa.volleys,
    pa.free_kick_accuracy,
    pa.heading_accuracy 
FROM Player AS p
JOIN Player_Attributes AS pa ON p.player_api_id = pa.player_api_id
GROUP BY p.player_name
ORDER BY best_finishing DESC 
LIMIT 25;
"""
cursor.execute(shooting_stats_table)
connect.commit()
df_check_shooting_stats_table = pd.read_sql_query("SELECT * FROM Shooting_Stats LIMIT 25;", connect)
print(df_check_shooting_stats_table)

connect.close()