# INSERT
import mysql.connector
import time
try:
    mydb = mysql.connector.connect(
      host="localhost",
      user="kevindaniel",
      password="123456789"
    )
    mycursor = mydb.cursor()
    #mycursor.execute("CREATE DATABASE mydatabase")
    mydb = mysql.connector.connect(
      host="localhost",
      user="kevindaniel",
      password="123456789",
      database="mydatabase"
    )
    mycursor = mydb.cursor()
    query = "INSERT INTO trial_illicit (Hundred) VALUES ('2NG911115')"
    query_str = str(query)
    mycursor.execute(query_str)
    mydb.commit()
    print("record inserted, ID:", mycursor.lastrowid)
except:
    print("ERROR")
else:
    print("Table Data Insertion Success")
time.sleep(5)