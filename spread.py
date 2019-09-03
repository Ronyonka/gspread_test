import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC

scope = ['https://www.googleapis.com/auth/drive']
creds = SAC.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('TestSheet').sheet1
everything = sheet.get_all_records()
node = '0A03F8E4'

def printer(everything, node):
    arr = []
    for i in everything:
        if i.get('NodeAddr') == node:
            return i.get('IMEI')

print(printer(everything, node))