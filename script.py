from selenium import webdriver
import json
import time
import datetime
import os
import sys

now = datetime.datetime.now()
nowtime = now.strftime('%Y-%m-%d_%H-%M-%S')

print("설정파일을 읽습니다.\n")
with open('./info.json', 'r', encoding='utf-8') as r:
    info = json.load(r)
print("로드완료!\n")

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument(
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/83.0.4103.116 "
        "Safari/537.36"
        )
options.add_argument("disable-gpu")

if getattr(sys, 'frozen', False): 
    chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
    driver = webdriver.Chrome(chromedriver_path, options=options)
else:
    driver = webdriver.Chrome('./chromedriver.exe', options=options)

print("자가진단 홈페이지에 접속합니다.\n")
driver.get(info['link'])
print("성공적으로 접속됬습니다.\n")

driver.find_element_by_xpath('//*[@id="container"]/div/div/div/div[2]/div/a[2]/div').click()
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="btnSrchSchul"]').click()
time.sleep(0.5)
driver.switch_to.window(driver.window_handles[-1])
print("학교이름을 제출합니다.")
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="schulNm"]').send_keys(info['schoolname'])
time.sleep(0.5)
if info['preschool'] is True:
    driver.find_element_by_xpath('//*[@id="infoForm"]/div[1]/p/span[3]/button').click()
    driver.find_element_by_xpath('//*[@id="infoForm"]/div[2]/table/tbody/tr[2]/td[1]/a').click()
else:
    driver.find_element_by_xpath('//*[@id="infoForm"]/div[1]/p/span[3]/button').click()
    driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
time.sleep(0.5)
print("제출완료!\n")
driver.switch_to.window(driver.window_handles[0])
print("생년월일과 이름을 제출합니다.\n")
driver.find_element_by_xpath('//*[@id="pName"]').send_keys(info['name'])
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="frnoRidno"]').send_keys(info['birth'])
print("완료!\n")
time.sleep(0.5)
print("체크중입니다.\n")
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
print("전부 체크가 완료되고 제출되었어요!\n")

print("스크린샷을 준비할게요!\n")

if not os.path.exists("./screenshot"):
    print("스크린샷 폴더가없는거같아요. 생성할게요!\n")
    os.mkdir("./screenshot")
    print("스크린샷을 찍을게요!\n")
    driver.save_screenshot(f"./screenshot/{nowtime}_screenshot.png")
    print("자가진단이 완료되었어요!\n")
    driver.quit()
else:
    print("스크린샷을 찍을게요!\n")
    driver.save_screenshot(f"./screenshot/{nowtime}_screenshot.png")
    print("자가진단이 완료되었어요!\n")
    driver.quit()
