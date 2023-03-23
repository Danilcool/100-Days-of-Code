import requests
import datetime

time = datetime.datetime.now()
pixela_end_point = "https://pixe.la/v1/users"
secret_token = '282828282828'

user_name = "danilcool"
user_param = {"token":secret_token,
              "username":"danilcool",
              "agreeTermsOfService":"yes",
              "notMinor":"yes"}

#
# response = requests.post(url=pixela_end_point,json=user_param)
# print(response.text)

graphs = {"id":"graph1",
          "name":"Running",
          "unit":"Day",
          "type":"int",
          "color":"ajisai"
                  ""}

graph_endpoint = f'{pixela_end_point}/{user_name}/graphs1'

headers = {
    "X-USER-TOKEN":secret_token
}
# data = requests.post(url=graph_endpoint,json=graphs,headers=headers)
#
# print(data.text)

#adding pixel data to out graph

dates= {"date":f"{time.year}{time.month}{time.day}",
        "quantity":"2"}





graphs = {"id":"graph1",
          "name":"Running",
          "unit":"Day",
          "type":"int",
          "color":"ajisai"}

pixela_creating_point= f'{pixela_end_point}/{user_name}/graphs/graph1'

response = requests.post(url=pixela_creating_point,json=dates,headers=headers)
print(response.text)


