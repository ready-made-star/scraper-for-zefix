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
import undetected_chromedriver as uc

options={
    'proxy':{
        "http": "http://arpkmgvp-rotate:jh3269dn5f@p.webshare.io:80/",
        "https": "http://arpkmgvp-rotate:jh3269dn5f@p.webshare.io:80/",
        "no_proxy": 'localhost,127.0.0.1'
    }
}

today = date.today()

base_url="https://www.comparis.ch/carfinder/marktplatz?page={}"
# /html/body/zfx-root/main/zfx-entity/zfx-firm/div/div[2]/a[1]
total_page=100
main_url = []
#bypass function
def seleniumUndetected():

    # n = 0
    driver = uc.Chrome(version_main=108)
    driver.maximize_window()
    datas = {}
    count = 0
    for page_num in range(total_page):
        car_url = []
        driver.get(base_url.format(page_num))
        time.sleep(15)
        for x in range(15):
            try:
                url_ele = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/main/div/div[4]/div[1]/div[2]/div[{}]/a'.format(x+1))))
                make_ele = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/main/div/div[4]/div[1]/div[2]/div[{}]/a/div/div[2]/div[1]/h2/span[1]'.format(x+1)))).text
                model_ele = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/main/div/div[4]/div[1]/div[2]/div[{}]/a/div/div[2]/div[1]/h2/span[3]'.format(x+1)))).text

            except:
                url_ele= ''
                make_ele = ''
                model_ele = ''

            if(url_ele != ''):
                car_url.append([url_ele.get_attribute('href'), make_ele, model_ele])

        for car, make, model in car_url:

        # if(1):
        # car = 'https://www.comparis.ch/carfinder/marktplatz/details/show/29033254'
            driver.get(car)
            print(car)
            data = {}
            item= WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'attributes-grid')))
            items = item.find_elements(By.CLASS_NAME, 'column')
            data["URLs"] = car
            try:
                data["data_posted"] = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content-section-id"]/section/div/div/div/div[2]/div[1]/div[2]/ul/li[1]'))).text.replace('Erstmals gefunden am ', '').replace('\n', '')
            except:
                data["data_posted"] = ''
            try:
                data["mileage"] = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content-section-id"]/section/div/div/div/div[2]/div[1]/div[3]/b/ul/li[3]'))).text.replace('Km-Stand: ', '').replace('km', '').strip()
            except:
                data["mileage"] = ''
            try:
                data["makename"] = make
                data["modelname"] = model
            except:
                data["makename"] = ''
                data["modelname"] = ''
            try:
                data["firstreg"] = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content-section-id"]/section/div/div/div/div[2]/div[1]/div[3]/b/ul/li[2]'))).text.replace('Erstzulassung: ', '')
            except:
                data["firstreg"] = ''
            data["DetailsSpecifications"] = {}

            for i in items:
                try:
                    title = i.find_element(By.TAG_NAME, "dt").text
                    data["DetailsSpecifications"][title] = i.find_element(By.TAG_NAME,'dd').text
                except:
                    data["DetailsSpecifications"][title] = ""

            try:
                data["price"] = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content-section-id"]/section/div/div/div/div[2]/div[2]/div[1]/div[3]/div/div[1]/div/div/strong'))).text
            except:
                data["price"] = ''
            data["dateExtracted"] = str(time.gmtime(time.time())[0]) + '-' + str(time.gmtime(time.time())[1]) + '-' + str(time.gmtime(time.time())[2])
            
            datas[count] = {}

            datas[count].update(data)
            count += 1
        with open(f"{today}.json", "w", encoding='utf-8') as file:
            json.dump(datas, file, indent=4, ensure_ascii=False)

if __name__=="__main__":
    print('start')
    seleniumUndetected()
  