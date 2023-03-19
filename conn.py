import sqlite3
import csv
conn = sqlite3.connect('mydatabase.db')

with open('users.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader: "users.csv"
