from bs4 import BeautifulSoup
import requests

user_year_input = input('What year do you want to travel into?(format of YYY-MM-DD):')

year_mont_day_list = user_year_input.split("-")

year = year_mont_day_list[0]
month = year_mont_day_list[1]
day = year_mont_day_list[2]
web_url = f"https://www.billboard.com/charts/hot-100/{year}-{month}-{day}/"

responce = requests.get(web_url)
text_info = responce.text

web_soup = BeautifulSoup(text_info,'html.parser')
# div_container = web_soup.find_all(class_="o-chart-results-list-row-container",name='div')
# for div in div_container:
#     print(div.get_text())

final_list = []
names = web_soup.find_all(name='h3',id="title-of-a-story")
for name in names:
    names_list = name.get_text().strip().split("\n")
    for name in names_list:
        if name != "Songwriter(s):":
            if name != "Producer(s):":
                if name != "Imprint/Promotion Label:":
                    final_list.append(name)

print(final_list[3:-1])