import requests
from bs4 import BeautifulSoup


url = "https://comic.naver.com/webtoon/list?titleId=790713&weekday=fri"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("td", attrs = {"class" : "title"} )

for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com" + cartoon.a["href"]
    print(title, link)

'''
print(soup.title)
print(soup.title.get_text())

print(soup.a)
print(soup.a.attrs)
print(soup.a["href"])
'''

'''
print(soup.find("a", attrs={"class": "Nbtn_upload"}))
print(soup.find(attrs={"class":"Nbth_upload"}))

rank1 = soup.find("li", attrs={"class":"rank01"})
print("rank 1: {}".format(rank1.a.get_text()))

otherRanks = rank1.find_next_siblings("li")
i = 1 
for otherRank in otherRanks:
    i = i+1
    print("rank {}: {}".format(i, otherRank.a.get_text()))
'''

'''
cartoons = soup.find_all("a", attrs = {"class" : "title"})
print('만화 수 : ', len(cartoons))

for i, cartoon in enumerate(cartoons):
    if i == 15:
        break
    print(cartoon.get_text())
'''
