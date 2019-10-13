#import library
import gspread
#Service client credential from oauth2client
from oauth2client.service_account import ServiceAccountCredentials as SAC

# Print nicely
import pprint
#Create scope
scope = ['https://www.googleapis.com/auth/drive']
#create some credential using that scope and content of startup_funding.json
creds = SAC.from_json_keyfile_name('wstf.json',scope)
#create gspread authorize using that credential
client = gspread.authorize(creds)
#Now will can access our google sheets we call client.open on StartupName
sheet = client.open('wstf').sheet1
# pp = pprint.PrettyPrinter()
#Access all of the record inside that
everything = sheet.get_all_records()

lng = []
lat = []
for i in everything:
    lng.append(i.get('_GPS_location_longitude'))
    lat.append(i.get('_GPS_location_latitude'))
# print(len(lng))
# print(len(lat))