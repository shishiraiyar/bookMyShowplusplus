from flask import Flask,render_template, request
from database import Database
from mongo import MongoDatabase

app = Flask(__name__)
RDB = Database("data.db")
NRDB = MongoDatabase()
print("Lamao")

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/admin")
def adminLogin():
    theatres = RDB.getAllTheatres()
    movies = RDB.getMoviesList()
    screens=RDB.getScreens()
    return render_template('adminPage.html',theatres=theatres,movies=movies,screens=screens)

@app.route("/addMovie", methods=["POST"])
def addMovie():
    name = request.form.get("name")
    description = request.form.get("description") 
    cast = request.form.get("cast") 
    rating = float(request.form.get("rating")) 
    duration = int(request.form.get("duration") )
    print(name+" "+description+" "+cast)
    print(rating)
    print(duration)
    RDB.insertMovie(name,description,cast,rating,duration)
    return ('',204)

@app.route("/addScreen", methods=["POST"])
def addScreen():
    rows = request.form.get("rows")
    cols = request.form.get("cols") 
    t_id = int(request.form.get("theatre")) 
    print(rows+" "+cols)
    print(t_id)
    RDB.insertScreen(rows,cols,t_id)
    
    return ('',204)

@app.route("/addMovieShow", methods=["POST"])
def addMovieShow():
    startTime = request.form.get("startTime")
    endTime = request.form.get("endTime") 
    date = request.form.get("date") 
    movie = int(request.form.get("movie")) 
    screen = int(request.form.get("screen") )
    print(startTime+" "+endTime+" "+date)
    print(movie)
    print(screen)
    RDB.insertMovieShow(startTime,endTime,date,movie,screen)
    
    return ('',204)

@app.route("/addTheatre", methods=["POST"])
def addTheatre():
    name = request.form.get("name")
    operatingSince = request.form.get("operatingSince") 
    latitude = request.form.get("latitude") 
    longitude = request.form.get("longitude")
    address = request.form.get("address") 
    print(name+" "+operatingSince+" "+latitude+" "+longitude+" "+address)
    RDB.insertTheatre(name,operatingSince,latitude,longitude,address)
    return ('',204)

@app.route("/validateUser", methods=["POST"])
def validateUser():
    #send to db
    email = request.form.get("email")
    password = request.form.get("pwd") 
    print(email)
    print(password)
    result = NRDB.validate(email,password)
    if(result==True):
        return homepage()
    else:
        return ('',204)

@app.route("/signUp", methods=["POST"])
def signUp():
    #send to db
    email = request.form.get("email")
    username= request.form.get("username")
    password = request.form.get("pwd") 
    print(email+" "+username+" "+password)
    NRDB.addUser(email,username,password)
    return ('',204)

@app.route("/home")
def homepage():
    movies =RDB.getMoviesList() #list of dictionary ; each dictionary is a movie
    # print(movies)
    return render_template('homepage.html', movies=movies)

@app.route("/map/<movie_ID>")
def mapPage(movie_ID):
    theatres=RDB.getTheatres(movie_ID)
    return render_template('map.html', theatres=theatres)

@app.route("/shows") #/shows?theatre=3231&movie=8348
def showPage():
    movie_id = request.args.get('movie')
    theatre_id = request.args.get('theatre')
    # print(movie_id)
    # print(theatre_id)
    show_data=RDB.getMovieShows(movie_id,theatre_id)
    return render_template('shows.html',show_data=show_data)

@app.route("/seats/<show_ID>")
def showSeats(show_ID):
    info=NRDB.getSeats(int(show_ID))
    seatMatrix = info["seatMatrix"]
    row=len(seatMatrix)
    col=len(seatMatrix[0])
    return render_template('seats.html',seatMatrix=seatMatrix,row=row,col=col)

@app.route("/bookTicket/<seatNo>", methods=['POST'])
def bookTicket():
    data = request.json
    print(data)
    # data contains showid, row, col, userid
    # add an entry to tickets table 
    # mark the seat as booked in mongo
    # return success popup or something

app.run(host="0.0.0.0", port=5000, debug=True)