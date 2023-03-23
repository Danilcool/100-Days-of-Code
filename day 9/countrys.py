travel_log = [{
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

cities_visited = {}
list_county = []
for country in travel_log:

  for city in country['cities']:
    list_county.append(city)

  cities_visited["cities"] = list_county


print(cities_visited)

{
  "country": "Germany",
  "visits": 5,
  "cities": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "cities_amount" : 12 }
},
]