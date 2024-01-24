from flask import Flask,render_template, request
# import database

app = Flask(__name__)
@app.route("/")
def login():
    return render_template('login.html')

@app.route("/home")
def homepage():
    #QUery
    movies = [{"name": "omg", "rating": 4, "id": 2}, {"name": "lol", "rating": 3, "id": 3}]
    return render_template('homepage.html', movies=movies)

@app.route("/map/<movie_ID>")
def mapPage(movie_ID):
    #server queries for locations that play this movie, and store in location_data
    # jinja
    return render_template('mapPage.html', location_data) 

@app.route("/shows") #/shows?theatre=3231&movie=8348
def showPage():
    #request.getparams??
    #query for list of shows in the given theatre for the given movie
    #jinja
    return render_template('showPage.html',show_data)

@app.route("/seats/<show_ID>")
def showSeats(show_ID):
    #query from mongoDB
    #display?
    #jinja
    return render_template('seats.html',seatMatrix)

@app.route("/bookTicket", methods=['POST'])
def bookTicket():
    data = request.json
    print(data)
    # data contains showid, row, col, userid
    # add an entry to tickets table 
    # mark the seat as booked in mongo
    # return success

# @app.route("/getMovieInfo/<movie_ID>")
# def getMovieInfo(movie_ID):
#     print(movie_ID)
#     return {"ID":movie_ID}



app.run()
