import pandas as pd
import requests
import json
from csv import writer
from lib2to3.pgen2 import driver
from urllib import response
import pandas as pd
import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from datetime import date

# proxies={
#     "http": "http://arpkmgvp-rotate:jh3269dn5f@p.webshare.io:80/",
#     "https": "http://arpkmgvp-rotate:jh3269dn5f@p.webshare.io:80/"
# }
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=%s' % proxies)
number = [4533, 108978, 224594, 393159]
today = date.today()
id = ['CHE-103.058.551','CHE-103.887.688', 'CHE-100.687.182','CHE-105.984.411']
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
# driver = webdriver.Chrome(chrome_options = chrome_options, executable_path='./chromedriver.exe')
driver.maximize_window()
base_url="https://www.zefix.admin.ch/fr/search/entity/list/firm/{}"
# /html/body/zfx-root/main/zfx-entity/zfx-firm/div/div[2]/a[1]
external_url = []
n = 0
# with open('event3.csv', 'a', encoding='utf-8', newline='') as f_object:

#     product_row = writer(f_object)
#     product_row.writerow(["zefix"])

for x in number:
    main_url=base_url.format(x)
    driver.get(main_url)
    # external_url.append(driver.find_element(By.XPATH, '/html/body/zfx-/main/zfx-entity/zfx-firm/div/div[2]/a[1]').get_attribute('href'))

    companyAction_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'companyActions')))
    if companyAction_element:

        a_element = companyAction_element.find_element(By.TAG_NAME, "a").get_attribute("href")
        external_url.append(a_element)

    item_length = driver.find_elements(By.CLASS_NAME, "shabPub")
    n = n + 1
    for i in item_length:
        # item = driver.find_elements(By.XPTH, ("//div[@class= 'shabPub')")[2])
        items = i.find_elements(By.TAG_NAME, "td")
        print(n)
        row = ['zefix', id[n-1], today.strftime("%d/%m/%Y")]
        for item in items:

            row.append(item.text)
        with open('event3.csv', 'a', encoding='utf-8', newline='') as f_object:

            product_row = writer(f_object)
            product_row.writerow(row)
            f_object.close()

# second_row = ['hra', today.strftime("%d/%m/%Y")]
# with open('event3.csv', 'a', encoding='utf-8', newline='') as f_object:
#     product_row = writer(f_object)
#     product_row.writerow(second_row)   
m=0
for y in external_url:
    driver.get(y)
    table_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "personen")))
    tr_element = table_element.find_elements(By.TAG_NAME, "tr")
    n=0
    # with open('event3.csv', 'a', encoding='utf-8', newline='') as f_object:

    #     product_row = writer(f_object)
    #     product_row.writerow([y])
    m = m + 1
    for x in tr_element:
        row = ['hra',id[m-1], today.strftime("%d/%m/%Y")]
        if(x.text):
            n=n+1
            tds = x.find_elements(By.TAG_NAME, "td")
            for y in tds:
                td = y.text
                print(td)
                row.append(td)
                
            with open('event3.csv', 'a', encoding='utf-8', newline='') as f_object:

                product_row = writer(f_object)
                product_row.writerow(row)
                f_object.close()

    