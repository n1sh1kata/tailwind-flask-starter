from flask import Flask, render_template, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
from flask_socketio import SocketIO, emit  # <-- Add this import
import os

# Load .env variables
load_dotenv()

# Flask app setup
app = Flask(__name__)
socketio = SocketIO(app)

MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_DB = os.getenv("MONGODB_DB")
MONGODB_COLLECTION = os.getenv("MONGODB_COLLECTION")

# Setup MongoDB client and collection using env variables
client = MongoClient(MONGODB_URI)
db = client[MONGODB_DB]
collection = db[MONGODB_COLLECTION]

# Your routes
@app.route("/")
@app.route("/home")
def index():
	return render_template("pages/home.html")

@app.route("/dashboard")
def dashboard():
    return render_template("pages/dashboard.html")

@app.route("/data")
def visualize():
    return render_template("pages/visualize.html")

@app.route("/accordion")
def accordion():
	return render_template("accordion.html")

@app.route("/carousel")
def carousel():
	return render_template("carousel.html")

@app.route("/modal")
def modal():
	return render_template("modal.html")

@app.route("/collapse")
def collapse():
	return render_template("collapse.html")

@app.route("/dial")
def dial():
	return render_template("dial.html")

@app.route("/dismiss")
def dismiss():
	return render_template("dismiss.html")

@app.route("/drawer")
def drawer():
	return render_template("drawer.html")

@app.route("/dropdown")
def dropdown():
	return render_template("dropdown.html")

@app.route("/popover")
def popover():
	return render_template("popover.html")

@app.route("/tabs")
def tabs():
	return render_template("tabs.html")

@app.route("/tooltip")
def tooltip():
	return render_template("tooltip.html")

@app.route("/input-counter")
def input_counter():
	return render_template("input-counter.html")

@app.route("/datepicker")
def datepicker():
	return render_template("datepicker.html")


# WebSocket event to get data from MongoDB Atlas
@socketio.on('get_data')
def handle_get_data():
    data = list(collection.find({}, {"_id": 0}))  # exclude MongoDB _id field
    emit('data_response', data)  # Send data back to client

if __name__ == '__main__':
    socketio.run(app, debug=True)  
