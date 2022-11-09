'''
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


import requests

url = "https://google.com"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

res = requests.get(url, headers = headers)
res.raise_for_status()

with open("wonGoogle.html", "w", encoding = "utf8") as f:
    f.write(res.text)


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>HTML Study</title>
</head>
<body>
    <h1>This is a H1</h1>
    <p>This is a paragraph~!</p>
    <input type = "text" vaue = "아이디를 입력하세요">
    <input type = "password">
    <input type = "button" value = "로그인">
    <a href = "http://google.com">구글로 이동하기</a> 
</body>
</html>
'''