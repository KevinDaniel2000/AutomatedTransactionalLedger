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
    
    # Illicit
    sql = "DROP TABLE trial_illicit"
    mycursor.execute(sql)
    
    # Legitimate 
    sql = "DROP TABLE trial"
    mycursor.execute(sql)
    
    # Transaction
    sql = "DROP TABLE Transation_log"
    mycursor.execute(sql)
except:
    print("ERROR | Table Not Exists")
else:
    print("Table Deletion Success")
time.sleep(5)