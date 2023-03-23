import pandas
data = pandas.read_csv("50_states.csv")


answer = 'Alabama'
data[data.state == answer]
state_info = data[data.state == answer]

for state in data.state:
    if state == answer:
        print('hello')