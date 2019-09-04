import psycopg2
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC


scope = ['https://www.googleapis.com/auth/drive']
creds = SAC.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('TestSheet').sheet1
everything = sheet.get_all_records()


try:
   connection = psycopg2.connect(user="ron",
                                  password="password",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="hive")
   cursor = connection.cursor()
   postgreSQL_select_Query = "SELECT * FROM washgis"
   cursor.execute(postgreSQL_select_Query)
   print("Selecting rows from washgis table using cursor.fetchall")
   data_records = cursor.fetchall() 
   
   print("Print each row and it's columns values")
   node_arr = []
   for row in data_records:
    #    print("time = ", row[0], )
    #    print("topic = ", row[1])
    #    print("message  = ", row[2], "\n")
        if row[1].replace("/telemetry/", "").isdigit():
            node_arr.append(int(row[1].replace("/telemetry/", "")))
        else:
            node_arr.append(row[1].replace("/telemetry/", ""))
except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)
finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


def printer(everything, node_arr):
    arr = []
    for i in everything:
        for node in node_arr:
            if i.get('NodeAddr') == node:
                arr.append(i.get('IMEI'))
    return arr
    # return node_arr

print(printer(everything, node_arr))