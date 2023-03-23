import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas

scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('python-366113-83514fe625f9.json', scope)
client = gspread.authorize(credentials)

#
# sheet = client.create('Workout Data')
#
# sheet.share('dovcharenko20@gmail.com',perm_type='user',role='writer')

sheet = client.open('Workout Data').sheet1

df = pandas.read_csv("Final Data.csv")





sheet.update([df.columns.values.tolist()] + df.values.tolist())


# create a csv file on python file and then append files to it from the main after that we can suse the sheet.update https://towardsdatascience.com/turn-google-sheets-into-your-own-database-with-python-4aa0b4360ce7