
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
    Name VARCHAR(50) NOT NULL,
    Year INTEGER,
    DirectorName VARCHAR(100)
    )"""

create_table(connection, create_table_query)

def insert_into_table(conn, data):
    query = """
            INSERT INTO filmy (Name, Year, DirectorName)
            VALUES (?, ?, ?);
            """
    cursor = conn.cursor()  
    cursor.execute(query, data)
    conn.commit()  


sample_query = """
INSERT INTO filmy (Name, Year, DirectorName)
  VALUES ('Star Wars IV', 1977, 'George Lucas')
"""

insert_into_table(connection, ('Star Wars IV', 1977, 'George Lucas'))

insert_into_table(connection, ('Star Wars V', 1980, 'Irvin Kershner'))

insert_into_table(connection, ('Star Wars VI', 1983, 'Richard Marquand'))
insert_into_table(connection, ('Žluťoučký kůň', 2024, 'studenti z IT Stepu'))

def run_select_query(conn, query):
    cursor = conn.cursor()  
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)


query = "SELECT MovieId, Name, DirectorName FROM filmy WHERE DirectorName = 'George Lucas';"
    
run_select_query(connection, query)


connection.close() 


