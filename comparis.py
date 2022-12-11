import pandas as pd
import json
import time
from csv import writer
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
from webdriver_manager.chrome import ChromeDriverManager
from seleniumwire import webdriver
import numpy as np
# from fake_useragent import UserAgent
import undetected_chromedriver as uc


# ua = UserAgent()

options={
    'proxy':{
        "http": "http://arpkmgvp-rotate:jh3269dn5f@p.webshare.io:80/",
        "https": "http://arpkmgvp-rotate:jh3269dn5f@p.webshare.io:80/",
        "no_proxy": 'localhost,127.0.0.1'

    }
}

today = date.today()

# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sabdbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_option = uc.ChromeOptions()
# driver = webdriver.Chrome(executable_path='./chromedriver.exe', seleniumwire_options=options)
# driver.maximize_window()
base_url="https://www.comparis.ch/carfinder/marktplatz?page={}"
# /html/body/zfx-root/main/zfx-entity/zfx-firm/div/div[2]/a[1]
external_url = []
n = 0
total_page=3
main_url = []

#bypass function
def seleniumUndetected():
    driver = uc.Chrome(version_main=108)
    driver.maximize_window()
    for page_num in range(total_page):
        driver.get(base_url.format(page_num))
        time.sleep(10)
        for x in range(15):
            try:
                ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/main/div/div[4]/div[1]/div[2]/div[{}]/a'.format(x+1))))
            except:
                ele= ''
            if(ele != ''):
                print(ele.get_attribute('href'))
        print("next page")

if __name__=="__main__":
    print('start')
    seleniumUndetected()

# for x in range(total_page):
    
#     driver.get(base_url.format(x+1))
    # print('a')
    # time.sleep(10)
    # external_url.append(driver.find_element(By.XPATH, '/html/body/zfx-/main/zfx-entity/zfx-firm/div/div[2]/a[1]').get_attribute('href'))
    # main_url.append()
    # item = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'css-a0dqn4 ehesakb1')))
    # item = driver.find_elements(By.CLASS_NAME, "ehesakb1")
    # print(item, '1')
    # if item:

    #     a_element = item.get_attribute("href")
    #     main_url.append(a_element)
    #     print(main_url)
#     n = n + 1
#     for i in item_length:
#         # item = driver.find_elements(By.XPTH, ("//div[@class= 'shabPub')")[2])
#         items = i.find_elements(By.TAG_NAME, "td")
#         print(n)
#         row = ['zefix', data[n-1], today.strftime("%d/%m/%Y")]
#         for item in items:

#             row.append(item.text)
#         with open('result.csv', 'a', encoding='utf-8', newline='') as f_object:

#             product_row = writer(f_object)
#             product_row.writerow(row)
#             f_object.close()

# # second_row = ['hra', today.strftime("%d/%m/%Y")]
# # with open('event3.csv', 'a', encoding='utf-8', newline='') as f_object:
# #     product_row = writer(f_object)
# #     product_row.writerow(second_row)   
# m=0
# for y in external_url:
#     driver.get(y)
#     table_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "personen")))
#     tr_element = table_element.find_elements(By.TAG_NAME, "tr")
#     n=0
#     # with open('event3.csv', 'a', encoding='utf-8', newline='') as f_object:

#     #     product_row = writer(f_object)
#     #     product_row.writerow([y])
#     m = m + 1
#     for x in tr_element:
#         row = ['hra',data[m-1], today.strftime("%d/%m/%Y")]
#         if(x.text):
#             n=n+1
#             tds = x.find_elements(By.TAG_NAME, "td")
#             for y in tds:
#                 td = y.text
#                 print(td)
#                 row.append(td)
                
#             with open('result.csv', 'a', encoding='utf-8', newline='') as f_object:

#                 product_row = writer(f_object)
#                 product_row.writerow(row)
#                 f_object.close()

    