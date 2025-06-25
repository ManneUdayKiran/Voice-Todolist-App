from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

# Connect to MongoDB Atlas
client = MongoClient(os.getenv("MONGO_URI"))
db = client["todo_db"]
tasks_col = db["tasks"]

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = list(tasks_col.find({}, {"_id": 0}))
    return jsonify(tasks), 200

@app.route("/tasks", methods=["POST"])
def save_tasks():
    tasks = request.json.get("tasks", [])
    tasks_col.delete_many({})
    if tasks:
        tasks_col.insert_many(tasks)
    return jsonify({"message": "Tasks saved"}), 200

if __name__ == "__main__":
    app.run(debug=True)
