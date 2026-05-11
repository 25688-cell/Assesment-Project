
import sqlite3
db = sqlite3.connect('Medals.db')
cursor = db.cursor()
cursor.execute(
    "SELECT * FROM Country "
    "INNER JOIN Medals "
    "ON Country.country_code = Medals.country_code;"
)
result = cursor.fetchall()
print(f"{'Code':<5}{'Country':<23}{'Gold':<6}{'Silver':<7}{'Bronze':<6}")
for row in result:
    print(f"{row[0]:<5}{row[1]:<23}{row[3]:<6}{row[4]:<7}{row[5]:<6}")
db.close()
