from selenium import webdriver
import json
import time
import os, sys

if getattr(sys, 'frozen', False): 
    chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
    driver = webdriver.Chrome(chromedriver_path)
else:
    driver = webdriver.Chrome('./chromedriver.exe')

with open('./info.json', 'r', encoding='utf-8') as r:
    info = json.load(r)

driver.get('https://eduro.ice.go.kr/hcheck/index.jsp')
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="container"]/div/div/div/div[2]/div/a[2]/div').click()
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="btnSrchSchul"]').click()
time.sleep(0.5)
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_xpath('//*[@id="schulNm"]').send_keys(info['schoolname'])
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="infoForm"]/div[1]/p/span[3]/button').click()
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
time.sleep(0.5)
driver.switch_to.window(driver.window_handles[0])
driver.find_element_by_xpath('//*[@id="pName"]').send_keys(info['name'])
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="frnoRidno"]').send_keys(info['birth'])
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="rspns011"]').click()
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="rspns02"]').click()
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="rspns070"]').click()
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="rspns080"]').click()
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="rspns090"]').click()
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()