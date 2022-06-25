import csv
import psycopg2
import os
import pandas as pd

conn = psycopg2.connect(host = '127.0.0.1', 
database='postgres',
user='postgres',
password='dy1011')

cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS diabetes;")
cur.execute("""CREATE TABLE diabetes (
Pregnancies INTEGER PRIMARY KEY NOT NULL,
Glucose INTEGER NOT NULL,
Bloodpressure INTEGER NOT NULL,
Skinthickness VARCHAR,
Insulin INTEGER NOT NULL,
BMI VARCHAR(16) NOT NULL,
DiabetesPedigreeFunction VARCHAR(16) NOT NULL,
Age INTEGER NOT NULL,
Outcome INTEGER NOT NULL);""")

read_list = []
read_list_col = []
with open('diabetes.csv', 'r') as f:
    file_read = csv.reader(f, delimiter=',')
    line_count = 0
    for line in file_read:
        if line_count == 0:
            read_list_col.append(line)
        else:    
            read_list.append(line)
        line_count += 1            

for i in range(len(read_list)):
    read_list[i].insert(0,i)   

for row in read_list:
    cur.execute("""
    INSERT INTO Diabetes (Pregnancies, Glucose,
Bloodpressure,
Skinthickness,
Insulin,
BMI,
DiabetesPedigreeFunction,
Age,
Outcome)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);""",row)

conn.commit()