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
from selenium.webdriver.support import expected_conditions as EC
number = [4533, 108978, 224594, 393159]
driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.maximize_window()
base_url="https://www.zefix.admin.ch/fr/search/entity/list/firm/{}"
# /html/body/zfx-root/main/zfx-entity/zfx-firm/div/div[2]/a[1]
external_url = []
n = 0
for x in number:
    main_url=base_url.format(x)
    driver.get(main_url)
    # external_url.append(driver.find_element(By.XPATH, '/html/body/zfx-/main/zfx-entity/zfx-firm/div/div[2]/a[1]').get_attribute('href'))

    companyAction_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'companyActions')))
    if companyAction_element:

        a_element = companyAction_element.find_element(By.TAG_NAME, "a").get_attribute("href")
        external_url.append(a_element)

    item_length = driver.find_elements(By.CLASS_NAME, "shabPub")
    for i in item_length:
        # item = driver.find_elements(By.XPTH, ("//div[@class= 'shabPub')")[2])
        n = n + 1
        items = i.find_elements(By.TAG_NAME, "td")

        row = []
        for item in items:

            row.append(item.text)
        with open('event3.csv', 'a', encoding='utf-8', newline='') as f_object:

            product_row = writer(f_object)
            product_row.writerow(row)
            f_object.close()
        
for y in external_url:
    driver.get(y)
    table_element = driver.find_element(By.CLASS_NAME, "personen")
    tr_element = table_element.find_element(By.TAG_NAME, "tr").text
    print(tr_element)
    # row_element = table_element.
    