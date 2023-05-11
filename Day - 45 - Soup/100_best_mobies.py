from bs4 import BeautifulSoup
import requests
import random
Web = "https://au.rollingstone.com/100-greatest-movies-of-all-time/page/1/moulin-rouge/"

responce = requests.get(Web)
text_info = responce.text

soup = BeautifulSoup(text_info,'html.parser')

titles_list_raw = soup.find_all(class_="c-list__title t-bold")
titles_list = []

for title in titles_list_raw:
    titles_list.append(title.get_text('h3'))

def main():
    print('100 Best Movies in The world')
    print(titles_list)
    while titles_list != 0:
        random_number = return_random_number(titles_list)
        print(f'Total you should watch {titles_list[random_number]}')
        user_input = input('Did you watch this movie yes or no:').lower()
        if user_input == 'yes':
            titles_list.pop(random_number)

def return_random_number(titles_list):
    print(len(titles_list))
    random_number = random.randint(0,len(titles_list)-1)
    print(random_number)
    return random_number

with open('Topmovies','a') as file:
    for title in titles_list:
        file.write(f"{title}\n")


