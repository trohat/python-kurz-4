
import sqlite3

def connect_to_db():
    try:
        connection = sqlite3.connect("my_db.db") # toto je hlavní práce celé funkce
        print(sqlite3.version)
        return connection   
    except sqlite3.Error as e:
        print(e)

connection = connect_to_db()

def create_table(conn, query):
    cursor = conn.cursor()  
    cursor.execute(query)
    conn.commit()  
    


create_table_query = """CREATE TABLE IF NOT EXISTS filmy (
    MovieId INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    Name NVARCHAR(200) NOT NULL,
    Year INTEGER,
    DirectorName NVARCHAR(100)
    )"""

create_table(connection, create_table_query)


connection.close() 
