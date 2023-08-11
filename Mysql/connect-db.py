import mysql.connector 
from mysql.connector import Error
try:
    connect=mysql.connector.connect(host='localhost',database='davv',user='root',password='root')
    if connect.is_connected():
        print("connected to MYSQL server version")
        cursor=connect.cursor()
        cursor.execute("select database();")
        record=cursor.fetchone()
        print("youre connected to database: ",record)
except Error as e:
    print("Error while connecting",e)