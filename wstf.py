#import library
import gspread
#Service client credential from oauth2client
from oauth2client.service_account import ServiceAccountCredentials as SAC


#Create scope
scope = ['https://www.googleapis.com/auth/drive']

#create some credential using that scope and content of startup_funding.json
creds = SAC.from_json_keyfile_name('wstf.json',scope)

#create gspread authorize using that credential
client = gspread.authorize(creds)

#Now will can access our google sheets we call client.open on StartupName
sheet = client.open('wstf').sheet1

#Access all of the record inside that
everything = sheet.get_all_records()


def LongLat():
    longlat = []
# loop through all the records to get longitudes and latitudes
    for i in everything:
        location = i.get('GPS_location').split(' ')
        del location[2:len(location)]
        loc = location[::-1]
        longlat.append([float(i) for i in loc])
    return longlat
# print(LongLat())
def project():
    projo = []
    for i in everything:
        projo.append(i.get('project'))
    return projo
# print(project())

    
# print(len(lng))
# print(len(lat))