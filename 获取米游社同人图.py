import requests
import json
from lxml import etree
from selenium import webdriver
from time import sleep
#import seleniumrun 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
# headers = {
#     
# }

img_urls=[]
img_names=[]
driver_path = './msedgedriver.exe'
driver = webdriver.Edge(executable_path=driver_path)
driver.get('https://www.miyoushe.com/sr/home/56?type=1')
sleep(6)
for i in range(7):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    sleep(4)
page_text = driver.page_source
tree=etree.HTML(page_text)
div_lists=tree.xpath('//div[@class="mhy-img-article-card"]')
for div_list in div_lists:
    imgsrc=div_list.xpath('.//div[@class="mhy-img-article-card__img"]/img/@src')[0]
    imgname=div_list.xpath('.//div[@class="mhy-img-article-card__img"]/img/@alt')[0]
    img_urls.append(imgsrc)
    img_names.append(imgname)
for i in range(0,len(img_urls)):
    response=requests.get(url=img_urls[i]).content
    # for j in range(0,len(img_names[i])):
    #     if '/' in img_names[i]:
    #         img_names[i].replace('/','')
    #     if '\\' in img_names[i]:
    #         img_names[i].replace('\\','')
    #     if '|' in img_names[i]:
    #         img_names[i].replace('|','')
    #     if '//' in img_names[i]:
    #         img_names[i].replace('//','')
    with open("./米游社同人图/"+img_names[i]+'.jpg','wb') as fp:
        fp.write(response)
        print(str(i)+'   is going on!!!')

    