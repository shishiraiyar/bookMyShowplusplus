from flask import Flask,render_template, request
from database import Database

app = Flask(__name__)
RDB = Database("data.db")

@app.route("/")
def login():
    return render_template('login.html')

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
    print(movie_id)
    print(theatre_id)
    #query for list of shows in the given theatre for the given movie
    #jinja
    show_data=[{"show_id":12345}]
    return render_template('shows.html',show_data=show_data)

@app.route("/seats/<show_ID>")
def showSeats(show_ID):
    #query from mongoDB
    #display?
    #jinja
    seatMatrix=[[0,2,0,0],[4,0,6,0],[7,8,0,0]]
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

app.run()