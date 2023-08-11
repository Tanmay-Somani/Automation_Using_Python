import mysql.connector 
from mysql.connector import Error
from pprint import pprint
import pandas as pd
from sqlalchemy import create_engine

try:
    engine=create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format('root','davv','root','root'))
    connect=mysql.connector.connect(host='localhost',database='davv',user='root',password='root')
    cursor=connect.cursor()
    query="""select * from chapri;"""
    cursor.execute(query)
    myresult=cursor.fetchall()
    data=pd.DataFrame(myresult,columns=["name","age","type","no."])
    print(data)
    # print(data.head())
    # ordering_=data.groupby('age').count().resest_index
    # pprint(ordering_)
except Error as e:
    print("Error while connecting",e)
finally:
    if connect.is_connected():
        cursor.close()
        connect.close()
        print("MySQl connection is closed")