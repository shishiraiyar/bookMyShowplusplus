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
    #server queries for locations, and theatre id that play this movie, and store in location_data. also add movie id to each object
    # jinja
    location_data=[{"lat":124, "long":567,"t_id":1,"t_name":"shishu theatres"}]
    return render_template('map.html', location_data=location_data)

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
