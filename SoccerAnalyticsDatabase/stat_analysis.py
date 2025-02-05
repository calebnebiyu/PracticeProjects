import sqlite3
import pandas as pd

db = "SoccerAnalyticsDatabase/european_soccer_database.sqlite"
connect = sqlite3.connect(db)
cursor = connect.cursor()

# cursor.execute("DROP TABLE IF EXISTS GreatestPlayers;")
# connect.commit()
# top_players_table = """
# CREATE TABLE IF NOT EXISTS Greatest_Players AS
# SELECT 
#     p.id,
#     p.player_name,
#     MAX(pa.overall_rating) AS best_overall,
#     MAX(pa.potential) AS highest_potential,
#     pa.date,
#     p.birthday,
#     pa.date,
#     (CAST(strftime('%Y', pa.date) AS INTEGER) - CAST(strftime('%Y', p.birthday) AS INTEGER)) AS age_at_prime
# FROM Player AS p
# JOIN Player_Attributes AS pa ON p.player_api_id = pa.player_api_id
# JOIN Match AS m ON pa.date = m.date
# JOIN League AS l ON m.country_id = l.country_id
# WHERE pa.overall_rating IS NOT NULL
# GROUP BY p.player_name
# ORDER BY best_overall DESC, highest_potential DESC
# LIMIT 25;
# """
# cursor.execute(top_players_table)
# connect.commit()
# df_check_top_players_table = pd.read_sql_query("SELECT * FROM Greatest_Players LIMIT 25;", connect)
# print(df_check_top_players_table)


# cursor.execute("DROP TABLE IF EXISTS Shooting_Stats;")
# connect.commit()
# shooting_stats_table = """
# CREATE TABLE Shooting_Stats AS
# SELECT 
#     p.player_name,
#     MAX(pa.finishing) AS best_finishing,
#     pa.shot_power,
#     pa.long_shots,
#     pa.curve,
#     pa.penalties
#     pa.volleys,
#     pa.free_kick_accuracy,
#     pa.heading_accuracy 
# FROM Player AS p
# JOIN Player_Attributes AS pa ON p.player_api_id = pa.player_api_id
# GROUP BY p.player_name
# ORDER BY best_finishing DESC 
# LIMIT 25;
# """
# cursor.execute(shooting_stats_table)
# connect.commit()
# df_check_shooting_stats_table = pd.read_sql_query("SELECT * FROM Shooting_Stats LIMIT 25;", connect)
# print(df_check_shooting_stats_table)


# cursor.execute("DROP TABLE IF EXISTS Passing_Stats;")
# connect.commit()
# passing_stats_table = """
# CREATE TABLE Passing_Stats AS
# SELECT 
#     p.player_name,
#     MAX(pa.short_passing) AS best_short_passing,
#     MAX(pa.long_passing) AS best_long_passing,
#     pa.vision,
#     pa.crossing,
#     pa.curve
# FROM Player AS p
# JOIN Player_Attributes AS pa ON p.player_api_id = pa.player_api_id
# GROUP BY p.player_name
# ORDER BY best_short_passing DESC, best_long_passing DESC
# LIMIT 25;
# """
# cursor.execute(passing_stats_table)
# connect.commit()
# df_check_passing_stats_table = pd.read_sql_query("SELECT * FROM Passing_Stats LIMIT 25;", connect)
# print(df_check_passing_stats_table)


# cursor.execute("DROP TABLE IF EXISTS Speed/Physicality_Stats;")
# connect.commit()
# speed_physicality_stats_table = """
# CREATE TABLE Speed/Physicality_Stats AS
# SELECT 
#     p.player_name,
#     pa.attacking_work_rate,
#     pa.defensive_work_rate,
#     MAX(pa.sprint_speed) AS fastest,
#     pa.acceleration,
#     pa.agility,
#     pa.stamina,
#     MAX(pa.strength) AS strongest,
#     pa.aggression,
#     pa.reactions,
#     pa.balance,
#     pa.jumping,
# FROM Player AS p
# JOIN Player_Attributes AS pa ON p.player_api_id = pa.player_api_id
# GROUP BY p.player_name
# ORDER BY fastest DESC, strongest DESC
# LIMIT 25;
# """
# cursor.execute(speed_physicality_stats_table)
# connect.commit()
# df_check_speed_physicality_stats_table = pd.read_sql_query("SELECT * FROM Speed/Physicality_Stats LIMIT 25;", connect)
# print(df_check_speed_physicality_stats_table)


# cursor.execute("DROP TABLE IF EXISTS Defending_Stats;")
# connect.commit()
# defending_stats_table = """
# CREATE TABLE Defending_Stats AS
# SELECT 
#     p.player_name,
#     pa.defensive_work_rate,
#     MAX(pa.standing_tackle) AS best_standing_tackle,
#     MAX(pa.sliding_tackle) AS best_sliding_tackle,
#     pa.reactions,
#     pa.jumping,
#     pa.strength,
#     pa.interceptions,
#     pa.aggression,
#     pa. positioning,
#     pa.marking
# FROM Player AS p
# JOIN Player_Attributes AS pa ON p.player_api_id = pa.player_api_id
# GROUP BY p.player_name
# ORDER BY best_standing_tackle DESC, best_sliding_tackle DESC
# LIMIT 25;
# """
# cursor.execute(defending_stats_table)
# connect.commit()
# df_check_defending_stats_table = pd.read_sql_query("SELECT * FROM Defending_Stats LIMIT 25;", connect)
# print(df_check_defending_stats_table)

# Create a table for ball handling (including dribbling, ball control, etc.)
# Then, begin creating visuals for analysis and presentation.
# Finally, store files in appropriate folders.

connect.close()