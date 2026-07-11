import sqlite3

conn = sqlite3.connect("database/disaster.db")

cursor = conn.cursor()

cursor.execute("SELECT * FROM reports")

rows = cursor.fetchall()

print("\n------ REPORTS TABLE ------\n")

for row in rows:
    print(row)

conn.close()