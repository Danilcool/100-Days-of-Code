from bs4 import BeautifulSoup
import requests
website = "https://news.ycombinator.com/news"

responce = requests.get(website)
text_file = responce.text

soup = BeautifulSoup(text_file,'html.parser')
#
# print(soup.title)
#
# list = soup.find_all(class_='titleline')
#
# for title in list:
#     print(title.find('a').string)
#
# print('a')
articles_list_raw = soup.find_all(class_='titleline')
score_list_raw = soup.find_all(class_='score')

block_of_code = soup.find(class_='titleline')
articles_text = block_of_code.get_text('a')
upvotes_block = soup.find(class_="score")
article_upvote = upvotes_block.get_text()

print(articles_list_raw)
print(score_list_raw)

articles_list = []
score_list= []

for i in range(0, len(articles_list_raw) - 1):
    articles_list.append(articles_list_raw[i].get_text('a'))
    score_list.append(int(score_list_raw[i].getText('span').replace(" points","")))

top_score = max(score_list)
top_score_index = score_list.index(top_score)

print(f'Todays top story is {articles_list[top_score_index]} with {top_score} likes')

print(articles_list)
print(score_list)


