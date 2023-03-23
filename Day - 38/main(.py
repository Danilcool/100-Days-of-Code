import openai
import pandas
import datetime


import gspread
from oauth2client.service_account import ServiceAccountCredentials


time_now = datetime.datetime.now()
API_KEY= "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"
openai.api_key = API_KEY



scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]


# user_input = input('What did you do today:')
#
#
#
# response = openai.Completion.create(
#   model="text-davinci-002",
#   prompt=f"Decide texts workout time: time and workout: type out them in python dictionary type\n\nTexts: \"{user_input}\"\n",
#   temperature=0,
#   max_tokens=60,
#   top_p=1,
#   frequency_penalty=0.5,
#   presence_penalty=0
# )
#
#
#
#
# text_response = response['choices'][0]['text']
# print(text_response)
#
# data = text_response.split('\n')
#
# data_activity = data[1][14:]
# data_time = data[3][14:]
# print(data_activity,data_time)
#
#
day_count = 1

def main():
  user_input = input('What did you do today:')
  response = open_ai_response(user_input)
  add_to_csv(response, user_input)
  save_to_drive_sheets()



def open_ai_response(user_input):

  response = openai.Completion.create(
    model="text-davinci-002",
    prompt=f"Decide texts workout time: time and workout: type out them in python dictionary type\n\nTexts: \"{user_input}\"\n",
    temperature=0,
    max_tokens=60,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0
  )
  text_response = response['choices'][0]['text']
  data = text_response.split('\n')

  data_activity = data[1][14:]
  data_duration = data[3][14:]
  return [data_activity,data_duration]

def add_to_csv(response,user_input):
    data_activity = response[0]
    data_duration = response[1]


    try:

      raw_data = {
                  "Date": [time_now.strftime("%m/%d/%Y")],
                  'Day': [time_now.strftime("%A")],
                  'Workout Type': [data_activity],
                  'Duration': [data_duration],
                  'Input': [user_input]}

      date = pandas.DataFrame(raw_data)

      date.to_csv('Final Data.csv', mode='a', header=False)
    except:

      raw_data = {
        "Date": [time_now.strftime("%m/%d/%Y")],
        'Day': [time_now.strftime("%A")],
        'Workout Type': [data_activity],
        'Duration': [data_duration],
        'Input': [user_input]}

      date = pandas.DataFrame(raw_data)

      date.to_csv('Final Data.csv')

def save_to_drive_sheets():

    credentials = ServiceAccountCredentials.from_json_keyfile_name('python-366113-83514fe625f9.json', scope)
    client = gspread.authorize(credentials)

    sheet = client.open('Workout Data').sheet1
    df = pandas.read_csv("Final Data.csv")
    sheet.update([df.columns.values.tolist()] + df.values.tolist())

main()