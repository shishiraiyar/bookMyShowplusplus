from flask import Flask,render_template, request,jsonify
from database import Database
from mongo import MongoDatabase
import os
import google.generativeai as genai
from flask import jsonify
from google.generativeai.types import HarmCategory, HarmBlockThreshold

app = Flask(__name__)
RDB = Database("data.db")
NRDB = MongoDatabase()
print("Lamao")

genai.configure(api_key ='AIzaSyAATqp6lsJHLLrcMZnrZveUGx7083TgG9M')
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat()

def send_to_chatbot():
    context = """
                You are a chatbot designed to give information acquired from the database below when users ask for it
                """
    
    movies = f"""
                The following movies are in the database:
                {RDB.getMoviesList()}
            """
    theatres = f"""
                The following theatres are in the database:
                {RDB.getAllTheatres()}
                """
    
    shows = """"""
    message1 = """the following movies are in the database currently: 
                Name=3 idiots, Description=In college, Farhan and Raju form a great bond with Rancho due to his refreshing outlook. Years later, a bet gives them a chance to look for their long-lost friend whose existence seems rather elusive, Cast=Amir Khan, Sharman Joshi, R.Madhavan, Kareena Kapoor, Rating=9.3, Duration= 120 minutes;
                Name=Bhool Bhulaiyaa, Description=An NRI and his wife decide to stay in his ancestral home, paying no heed to the warnings about ghosts. Soon, inexplicable occurrences cause him to call a psychiatrist to help solve the mystery, Cast=Akshay Kumar, Rajpal Yadav, Vidya Balan, Paresh Rawal, Rating=9.4, Duration=180 minutes;
                Name= Oppenheimer, Description=During World War II, Lt. Gen. Leslie Groves Jr. appoints physicist J. Robert Oppenheimer to work on the top-secret Manhattan Project. Oppenheimer and a team of scientists spend years developing and designing the atomic bomb. Their work comes to fruition on July 16, 1945, as they witness the worlds first nuclear explosion, forever changing the course of history, Cast=Cilian Murphy, Florence Pugh, Emily Blunt, Robert Downey Jr,Rating= 9.5,Duration= 190 minutes;
                Name=Barbie, Description=Barbie and Ken are having the time of their lives in the colorful and seemingly perfect world of Barbie Land. However, when they get a chance to go to the real world, they soon discover the joys and perils of living among humans, Cast=Margot Robbie, Ryan Gosling, Will Ferrel, Emma Mackey, Rating=9.45, Duration= 130 minutes
                """
    generate_content(context + movies + theatres)
    print('message sent to chatbot')


def generate_content(message):
    global chat
    config = {
        "max_output_tokens": 2048,
        "temperature": 0.5,
        "top_p": 1
    }
    safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
    }
    return chat.send_message(message, 
                             generation_config=config, 
                             safety_settings=safety_settings
                             ).candidates[0].content.parts[0].text


@app.route("/")
def login():
    return render_template('login.html')

@app.route("/chatbot")
def chatbotpage():
    send_to_chatbot()
    return render_template("chatbot.html")

@app.route("/getchatbotresponse", methods=['POST'])
def getchatbotresponse():
    message = request.json["message"]
    response = generate_content(message)
    return jsonify({"response": response})



@app.route("/adminLogin")
def adminLogin():
    return render_template('adminLogin.html')

@app.route("/admin")
def adminPage():
    theatres = RDB.getAllTheatres()
    movies = RDB.getMoviesList()
    screens=RDB.getScreens()
    return render_template('adminPage.html',theatres=theatres,movies=movies,screens=screens)

@app.route("/validateAdmin", methods=["POST"])
def validateAdmin():
    #send to db
    email = request.form.get("email")
    password = request.form.get("pwd") 
    print(email)
    print(password)
    result = NRDB.validateAdmin(email,password)
    print(result)
    if(result==True):
        return adminPage()
    else:
        return ('',204)
    # return ('',204)

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

@app.route('/book_ticket', methods=['POST'])
def book_ticket():
    data = request.json
    showID = int(data.get('showID'))
    row = int(data.get('row'))
    col = int(data.get('col'))
    print(type(showID))
    print(row)
    print(col)
    NRDB.update(showID,row,col)
    # Do something with the row and col (e.g., mark the seat as booked)
    # seatMatrix[row][col] = 1

    # You can perform additional logic here

    result = {'message': 'Ticket booked successfully'}
    return jsonify(result)



app.run(host="0.0.0.0", port=5000, debug=False)