import sqlite3

# db = sqlite3.connect("data.db")

# def deleteDB(db: sqlite3.Connection)



class Database:
    def __init__(self, filename):
        self.db = sqlite3.connect(filename,check_same_thread=False)
    
    def createTables(self):
        cur = self.db.cursor()
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
                        phoneNumber TEXT, 
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
        self.db.commit()
        cur.close()
        return

    def getTableNames(self):
        cur = self.db.cursor()
        res = cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        names = [row[0] for row in res]
        # if 'sqlite_sequence' in names:
        #     names.remove('sqlite_sequence')
        
        cur.close()
        return names

    def showTableInfo(self):
        cur = self.db.cursor()
        tables = self.getTableNames()
        for table in tables:
            print(table)
            info = cur.execute(f"PRAGMA table_info({table})")
            for col in info.fetchall():
                print(col[1])
            print("***************************************")
        cur.close()
        return
        
    def genericDisplayTable(self, tableName):
        cur = self.db.cursor()
        res = cur.execute(f"PRAGMA table_info({tableName})")
        attributes = [col[1] for col in res.fetchall()]
        print(attributes)

        res = cur.execute(f"SELECT * FROM {tableName}")
        for row in res.fetchall():
            print(row)
        return

    def displayDatabase(self):
        for table in self.getTableNames():
            print(table)
            databej.genericDisplayTable(table)
            print("********************************************\n\n")

    def insertMovie(self, title, description, cast, rating, duration):
        cur = self.db.cursor()
        cur.execute(f"""INSERT INTO MOVIE (title, description, cast, rating, duration) 
                        VALUES ('{title}', '{description}', '{cast}', '{rating}', '{duration}')""")
        self.db.commit()
        cur.close()

    def insertUser(self, userID, fName, lName, pNo, dob):
        cur = self.db.cursor()
        cur.execute(f"""INSERT INTO USER (ID, firstName, lastName, phoneNumber, DOB)
                        VALUES ('{userID}', '{fName}', '{lName}', '{pNo}', '{dob}')""")
        self.db.commit()
        cur.close()

    def insertTheatre(self, name, operatingSince, lat, lng, addr):
        cur = self.db.cursor()
        cur.execute(f"""INSERT INTO THEATRE (name, operatingSince, latitude, longitude, address)
                        VALUES ('{name}', '{operatingSince}', '{lat}', '{lng}', '{addr}')""")
        self.db.commit()
        cur.close()
    
    def insertScreen(self, rows, cols, t_id):
        cur = self.db.cursor()
        cur.execute(f"""INSERT INTO SCREEN (rows, columns, theatre_ID)
                        VALUES ('{rows}', '{cols}', '{t_id}')""")
        self.db.commit()
        cur.close()
    
    def insertMovieShow(self, startTime, duration, movieID, screenID):
        cur = self.db.cursor()
        cur.execute(f"""INSERT INTO MOVIESHOW (startTime, duration, movie_ID, screen_ID)
                        VALUES ('{startTime}', '{duration}', '{movieID}', '{screenID}')""")
        self.db.commit()
        cur.close()

    def insertTicket(self, showID, userID, row, col, ticketClass):
        cur = self.db.cursor()
        cur.execute(f"""INSERT INTO TICKET (show_ID, user_ID, row, column, ticketClass)
                        VALUES ('{showID}', '{userID}', '{row}', '{col}', '{ticketClass}')""")
        self.db.commit()
        cur.close()
    
    def getMoviesList(self):
        cur = self.db.cursor()
        cur.execute("""SELECT * FROM MOVIE""")
        rows = cur.fetchall()
        movies=[]
        for row in rows:
            movie = {
                'ID': row[0],
                'title': row[1],
                'description':row[2],
                'cast':row[3],
                'rating':row[4],
                'duration':row[5]
            }
            movies.append(movie)

        cur.close()
        return movies
        
    def populateDummyData(self):
        self.insertMovie("3 idiots", "Engineering", "Amir Khan", 9.3, 120)
        self.insertMovie("4 idiots", "More idiots more better", "Srk", 9.4, 180)
        self.insertMovie("Oppenheimer", "bomb", "Robert Oppenheimer", 9.5, 190)
        self.insertMovie("Barbie", "pink", "girl", 9.45, 130)

        self.insertTheatre("PVR", "Yesterday", 12.97, 77.59,  "R R Nagar")
        self.insertTheatre("Inox", "Tomorrow", 12.98, 77.60,  "Rajaji Nagar")

        self.insertScreen(rows=10, cols=10, t_id=1)
        self.insertScreen(rows=7, cols=6, t_id=1)
        self.insertScreen(rows=9, cols=9, t_id=2)
        self.insertScreen(rows=6, cols=6, t_id=2)

        self.insertUser(154, "Library", "Table", "1234567890", "12/12/2012")
        self.insertUser(178, "Wiggly", "Bunny", "3003003003", "11/11/2011")

        self.insertMovieShow(startTime=1706868822, duration=300, movieID=2, screenID=1)
        self.insertMovieShow(startTime=1706878822, duration=300, movieID=3, screenID=2)
        self.insertMovieShow(startTime=1706978822, duration=250, movieID=4, screenID=2)
        self.insertMovieShow(startTime=1706978822, duration=200, movieID=4, screenID=1)

        self.insertTicket(showID=1, userID=154, row=1, col=1, ticketClass='vip')
        self.insertTicket(showID=3, userID=178, row=3, col=2, ticketClass='vip')
        

if __name__ == "__main__":

    databej = Database("data.db")
    # databej.createTables()
    
    # databej.populateDummyData()

    databej.displayDatabase()

    movies=databej.getMoviesList()
    print(movies)
