from bs4 import BeautifulSoup 
import requests 
website ='https://subslikescript.com/movie/The_Breach-14229154'
results = requests.get(website)
content = results.text
soup = BeautifulSoup(content,"lxml")
box = soup.find("div",class_ ="p-body-header")
print(box)
title = box.find("div",class_='p-title').get_text()
titlee=title.find('h1',class_='p-title-value')
print(titlee)
date = box.find("div",class_ ='p-description').get_text()
print(date)
time = date.find("a",class_='u-concealed').get_text()
with open(f"('title').txt",'w') as file:
    file.write(title)
    file.write(time)



