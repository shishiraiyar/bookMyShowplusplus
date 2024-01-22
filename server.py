from flask import Flask,render_template, request

app = Flask(__name__)
@app.route("/")
def login():
    return render_template('login.html')

@app.route("/homepage")
def homepage():
    return render_template('homepage.html')

@app.route("/getMovieInfo/<movie_ID>")
def getMovieInfo(movie_ID):
    print(movie_ID)
    return {"ID":movie_ID}

@app.route("/bookTicket", methods=['POST'])
def bookTicket():
    data = request.json
    print(data)

app.run()
