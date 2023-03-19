from urllib import request

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():

    users =...

    return jsonify(users)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()



    return '', 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()



    return '', 204

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):

    return '', 204

if __name__ == '__main__':
    app.run()
import sqlite3
import csv

conn = sqlite3.connect('mydatabase.db')

with open('users.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader: "python.csv"
