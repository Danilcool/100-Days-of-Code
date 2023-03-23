travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country,number,citys):

    travel_log.append({"county": country, 'visits': number, "cities" : citys})





#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

cities_visited = {}
list_county = []

for country in travel_log:

  for city in country['cities']:
    list_county.append(city)

  cities_visited["cities"] = list_county
print(cities_visited)