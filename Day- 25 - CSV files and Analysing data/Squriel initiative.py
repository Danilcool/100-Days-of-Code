import pandas


data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')


grey_data = len(data["Primary Fur Color"] == 'Grey')

black_data = len(data["Primary Fur Color"] == 'Black')

white_data = len(data["Primary Fur Color"] == 'White')

Cinnamon_data = len(data["Primary Fur Color"] == 'Cinnamon')

data_dict = {
    'Fur Colour' : ['Grey','Cinnamon','Black','white'],
    'Count':[grey_data,Cinnamon_data, black_data,white_data]

}

finished_data = pandas.DataFrame(data_dict)
finished_data.to_csv("Finished data.csv")
