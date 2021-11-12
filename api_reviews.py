from flask import Flask, jsonify, request
import json

app = Flask(__name__)

with open('./warframe_reviews.json') as json_file:
    review_data = json.load(json_file)

@app.route('/all')
def get_all_reviews():
  return jsonify(review_data)