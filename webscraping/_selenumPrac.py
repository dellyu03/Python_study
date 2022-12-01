from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser=webdriver.Chrome()

browser.get("http://naver.com")

elem=browser.find_element("id", "query")

que="삼성전자"
elem.send_keys(que)

elem.send_keys(Keys.ENTER)

browser.find_element("xpath", "//*[@id='main_pack']/section[4]/div/div[3]/a").click()

browser.find_element("xpath","//*[@id='main_pack']/div[2]/div/div/a[1]").click()

url="https://search.naver.com/search.naver?where=news&sm=tab_pge&query={} &sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=148&mynews=0&office_type=0&office_section_code  =0&news_office_checked=&nso=so:r,p:all,a:all&start=".format(que)

f=open("naver_samsung_news_title.txt","w",encoding="utf8")

for i in range(1,992,10):
    browser.get(url+str(i))
    elems=browser.find_element("class name", "list_news").find_elements("class name", "news_tit")

    for elem in elems:
        print(i, ":", elem.text)
        with open("naver_samsung_news_title.txt", "a", encoding="utf8") as f:
            f.write(elem.text)
        i+=1

browser.close()