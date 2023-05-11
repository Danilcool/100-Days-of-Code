from bs4 import BeautifulSoup


with open('website.html',encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents,'html.parser')

#print(soup.a)

for item in soup.find_all(name="a"):
    #print(item.getText)
    print(item.get('href'))

heading = soup.find(name='h1', id='name')
print(heading.string)

heading_three = soup.find(name='h3',class_='heading')
print(heading_three.string)

company_udl = soup.select_one(selector='#name')
print(company_udl)

list = soup.select('#name')
print(list)
