import requests
from bs4 import BeautifulSoup


url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

print(soup.title)
print(soup.title.get_text())

print(soup.a)
print(soup.a.attrs)
print(soup.a["href"])

print(soup.find("a", attrs={"class": "Nbtn_upload"}))
print(soup.find(attrs={"class":"Nbth_upload"}))

rank1 = soup.find("li", attrs={"class":"rank01"})
print("rank 1: {}".format(rank1.a.get_text()))

otherRanks = rank1.find_next_siblings("li")
i = 1 
for otherRank in otherRanks:
    i = i+1
    print("rank {}: {}".format(i, otherRank.a.get_text()))