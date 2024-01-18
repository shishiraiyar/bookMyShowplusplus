import sqlite3

db = sqlite3.connect("data.db")

def initDB(db: sqlite3.Connection):
    cur = db.cursor()
    cur.execute("""
                CREATE TABLE MOVIE(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                    title TEXT, 
                    description TEXT, 
                    cast TEXT, 
                    rating REAL, 
                    duration INTEGER)
                """)

    cur.execute("""       
                CREATE TABLE SCREEN (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    rows INTEGER,
                    columns INTEGER,
                    theatre_ID INTEGER,
                    FOREIGN KEY (theatre_ID) REFERENCES THEATRE (ID)
                )
    """)

    cur.execute("""       
                CREATE TABLE MOVIESHOW (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    startTime INTEGER,
                    duration INTEGER,
                    movie_ID INTEGER,
                    screen_ID INTEGER,
                    FOREIGN KEY (movie_ID) REFERENCES MOVIE (ID),
                    FOREIGN KEY (screen_ID) REFERENCES SCREEN (ID)
                )
    """)

    cur.execute("""
                CREATE TABLE USER(
                    ID integer PRIMARY KEY, 
                    firstName TEXT,
                    lastName TEXT, 
                    phoneNumber INTEGER, 
                    DOB TEXT
                )
    """)


    cur.execute("""
                CREATE TABLE THEATRE(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                    name TEXT,
                    operatingSince TEXT, 
                    latitude REAL, 
                    longitude REAL, 
                    address TEXT
                )
    """)

    cur.execute("""
                CREATE TABLE TICKET(
                    show_ID INTEGER, 
                    user_ID INTEGER, 
                    row INTEGER, 
                    column INTEGER, 
                    ticketClass TEXT,
                    FOREIGN KEY(show_ID) REFERENCES MOVIESHOW(ID),
                    FOREIGN KEY (user_ID) REFERENCES USER(ID),
                    PRIMARY KEY(show_ID, row, column)
                )
    """)


def showTableInfo(db: sqlite3.Connection):
    cur = db.cursor()
    res = cur.execute("SELECT name FROM sqlite_master")
    names = [row[0] for row in res]
    print(names)
    for name in names:
        print(name)
        info = cur.execute(f"PRAGMA table_info({name})")
        for col in info.fetchall():
            print(col[1])
        print("***************************************")


initDB(db)
db.commit()


showTableInfo(db)

db.close()