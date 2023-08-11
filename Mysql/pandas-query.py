import mysql.connector 
from mysql.connector import Error
from pprint import pprint
import pandas as pd
try:
    connect=mysql.connector.connect(host='localhost',database='davv',user='root',password='root')
    cursor=connect.cursor()
    query="""select * from chapri;"""
    cursor.execute(query)
    myresult=cursor.fetchall()
    data=pd.DataFrame(myresult,columns=["name","age","type","no."])
    print(data)
    # print(data.head())
    ordering_=data.groupby('age').count()
    pprint(ordering_)
except Error as e:
    print("Error while connecting",e)
finally:
    if connect.is_connected():
        cursor.close()
        connect.close()
        print("MySQl connection is closed")