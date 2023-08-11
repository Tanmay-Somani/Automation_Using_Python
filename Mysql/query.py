import mysql.connector 
from mysql.connector import Error
from pprint import pprint
try:
    connect=mysql.connector.connect(host='localhost',database='davv',user='root',password='root')
    cursor=connect.cursor()
    query="""select * from chapri;"""
    cursor.execute(query)
    myresult=cursor.fetchall()
    pprint(myresult)
except Error as e:
    print("Error while connecting",e)
finally:
    if connect.is_connected():
        cursor.close()
        connect.close()
        print("MySQl connection is closed")