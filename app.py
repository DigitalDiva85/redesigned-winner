from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime

app = Flask (__name__)
CORS(app)

#Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.clockSystem
logs_collection = db.logs

#Fetch logs for a specific month
@app.route('/logs', methods = ['Get'])
def get_logs():
    year = request.args.get('year')
    month = request.args.get('month')
    logs = list(logs_collection.find({"date" : {"$regex" : f"^{year}-{month.zfill(2)}"}}))
    
    for log in logs:
        log["_id"] =str(log["_id"]) #Convert Object to string
        return jsonify(logs)
    
    