import json
import pyodbc
from django.http import HttpResponse
# from restframework.decorators import api_view
# @api_view(['POST'])

def test(request):
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=46.34.161.23,13433;DATABASE=dbTest;UID=sa;PWD=111@a')
    cursor = connection.cursor()

    cursor.execute("select * from PriceHistory")

    rows=cursor.fetchall()

    list=[]
    for row in rows:
        obj=priceHistory(row[1],row[2])
        list.append(obj.__dict__)
    return HttpResponse(json.dumps(list), content_type='application/json')


class priceHistory():
    def __init__(self,Pdate,Price):
        self.Pdate=Pdate
        self.Price=Price

def test2(request):
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=46.34.161.23,13433;DATABASE=dbTest;UID=sa;PWD=111@a')
    cursor = connection.cursor()

    cursor.execute("select * from PriceHistory")

    rows=cursor.fetchall()

    list=[]
    for row in rows:
        list.append([row[1],row[2]])
    return HttpResponse(json.dumps(list), content_type='application/json')




