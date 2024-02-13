# Tohle je moje tréninkové SQL, nebylo použito v hodině

import sqlite3
import os
# os.remove("my.db")

connector = sqlite3.connect("my.db")

cursor = connector.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS filmy (
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
               JMENO TEXT,
    rok INTEGER,
    reziser NVARCHAR(100)
    )""")


result = cursor.execute("SELECT * from filmy")

for x in result:
    print(x)
print("a")

cursor.execute("""INSERT INTO FILMY (JMENO, ROK, REZISER)
  VALUES ('Star Wars IV', 1977, 'George Lucas')""")
connector.commit()

cursor.execute("""INSERT INTO FILMY (JMENO, ROK, REZISER)
  VALUES ('Star Wars II', 2002, 'George Lucas')
               """)
connector.commit()

cursor.execute("""delete from filmy where rok = 2002; delete from filmy where rok = 1997;""")

result = cursor.execute("SELECT * from filmy")

for x in result:
    print(x)



# connector.close()