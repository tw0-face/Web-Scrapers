from selenium import webdriver
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import sys,time


DRIVER_PATH='E:\egy-best\egybest-dl-master\egybest-dl\chromedriver.exe'
name = sys.argv[1]
episode = sys.argv[2]
quality = sys.argv[3] 
if quality==480:
    quality=0
else:
    quality=1
    
lody_url ='https://lodynet.ink/%D8%A7%D9%84%D9%85%D8%B3%D9%84%D8%B3%D9%84-%D8%A7%D9%84%D9%83%D9%88%D8%B1%D9%8A-'+str(name.replace(' ', '-').lower())+'-%D9%85%D8%AA%D8%B1%D8%AC%D9%85-%D8%A7%D9%84%D8%AD%D9%84%D9%82%D8%A9-'+ str(episode)
req = Request(
url = lody_url
    ,headers={'User-Agent': 'Mozilla/5.0'}
)
list = []
url = urlopen(req).read()
soup = BeautifulSoup(url,features="lxml")

for line in soup.find_all('a'):
    if str(line.get('href')).startswith("http://uplo.top/"):
        list.append(line.get('href'))

print('[+]lody url :' + lody_url)
print('[+]uplo url :' + list[quality])

option = webdriver.ChromeOptions()
option.add_argument('headless')

driver = webdriver.Chrome(DRIVER_PATH, options = option)
page_url = str(list[quality])
driver.get(page_url)
all_matches_button = driver.find_element_by_xpath('//button[@id="downloadbtn"]')
time.sleep(4)
all_matches_button.click()
print("The current url is:"+str(driver.current_url))
