import pandas
import pandas as pd


data = pd.read_csv("pokemon_data.csv")

# print(data.head(4))

# print(data.iloc[2,1])

#
# for index,row in data.iterrows():
#     print(index , row['Name'])
#
# fire_data = data.loc[data['Type 1'] =='Fire' ]
# print(fire_data)
#
# data = data.describe()
# print(data)
#
# data= data.sort_values('Speed',ascending=False)
# print(data)


#
# data['Total Stats'] = data['HP'] + data['Attack'] + data['Defense'] + data['Sp. Atk']+ data['Sp. Def'] + data['Attack']
#
# print(data)

#
# data = data.loc[(data['Type 1'] == 'Grass') & (data['Type 2'] == 'Poison') & (data['HP'] > 70)]
# data = data.drop(columns="Unnamed: 0",)
# data.reset_index(drop=True, inplace=True)
# data.to_csv('Testing_pokemon_csv',index=False)
#
# print(data)
#
#
# final_data = pandas.read_csv('Testing_pokemon_csv')
# +++++++
# new_data = data.loc[~data['Name'].str.contains('Mega') == True]
# new_data = new_data.drop(columns="Unnamed: 0",)
#
# new_data.reset_index(drop=True,inplace=True)
# new_data.to_csv('Not Mega Pokemon',index=False)
#
# print(new_data)

new_data = pandas.read_csv('Not Mega Pokemon')

data = data + new_data
data.to_csv('new data.csv')
print(data)