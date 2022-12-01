'''
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

#daum
# import requests
# from bs4 import BeautifulSoup

# for year in range(2017, 2022):
#     url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q={}+%EC%98%81%ED%99%94+%EC%88%9C%EC%9C%84".format(year)
#     res = requests.get(url)
#     res.raise_for_status()

#     soup = BeautifulSoup(res.text, "lxml")
#     images = soup.find_all ("img", attrs={"class":"thumb_img"})

#     for idx, image in enumerate(images):
#         image_url = image["src"]
#         if image_url.startswith("//"):
#             image_url = "https:" + image_url
#         print(image_url)
#         image_res = requests.get(image_url)
#         image_res.raise_for_status()
#         with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f:
#             f.write(image_res.content)
#         if idx >= 4:
#             break

#selenium
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# browser=webdriver.Chrome()

# browser.get("http://naver.com")

# elem=browser.find_element("id", "query")

# que="삼성전자"
# elem.send_keys(que)

# elem.send_keys(Keys.ENTER)

# browser.find_element("xpath", "//*[@id='main_pack']/section[4]/div/div[3]/a").click()

# browser.find_element("xpath","//*[@id='main_pack']/div[2]/div/div/a[1]").click()

# url="https://search.naver.com/search.naver?where=news&sm=tab_pge&query={} &sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=148&mynews=0&office_type=0&office_section_code  =0&news_office_checked=&nso=so:r,p:all,a:all&start=".format(que)

# f=open("naver_samsung_news_title.txt","w",encoding="utf8")

# for i in range(1,992,10):
#     browser.get(url+str(i))
#     elems=browser.find_element("class name", "list_news").find_elements("class name", "news_tit")

#     for elem in elems:
#         print(i, ":", elem.text)
#         with open("naver_samsung_news_title.txt", "a", encoding="utf8") as f:
#             f.write(elem.text)
#         i+=1

# browser.close()

#naver
# import csv
# import requests
# from bs4 import BeautifulSoup

# url = "https://finance.naver.com/sise/sise_market_sum.naver?&page="
# filename = "시가총액1-200.csv"

# f = open(filename, 'w', encoding="utf-8-sig", newline = "")
# writer = csv.writer(f)

# title = "N 종목명 현재가 전일비 등략률 액면가 시가총액 상장주식주 외국인비율 거레량 PER ROE".split()
# writer.writerow(title)

# for page in range(1, 5):
#     res = requests.get(url + str(page))
#     res.raise_for_status()
#     soup = BeautifulSoup(res.text, "lxml")
#     data_rows = soup.find("table", attrs = {'class' : 'type_2'}).find("tbody").find_all("tr")

#     for row in data_rows:
#         columns = row.find_all("td")
#         if len(columns) <= 1:
#             continue
#         data = [column.get_text().strip() for column in columns]
#         if "-" in data[4]:
#             data[3] = '-' + data[3]
#         writer.writerow(data)