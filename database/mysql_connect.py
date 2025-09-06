'''This module connects to a MySQL database'''
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="tejas", passwd="1234", database= "telusko")

mycursor = mydb.cursor()

mycursor.execute("select * from student")

# result = mycursor.fetchall()
result = mycursor.fetchone()

for i in result:
    print(i)