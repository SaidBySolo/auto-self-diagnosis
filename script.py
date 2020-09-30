import datetime
import json
import os
import re
import sys
import time

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.select import Select

now = datetime.datetime.now()
nowtime = now.strftime("%Y-%m-%d_%H-%M-%S")

print("설정파일을 읽습니다.\n")
with open("./info.json", "r", encoding="utf-8") as r:
    info = json.load(r)
print("로드완료!\n")

options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("window-size=1920x1080")
options.add_argument("disable-gpu")

if getattr(sys, "frozen", False):
    chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
    driver = webdriver.Chrome(chromedriver_path, options=options)
else:
    driver = webdriver.Chrome("./chromedriver.exe", options=options)

print("자가진단 홈페이지에 접속합니다.\n")
driver.get("https://hcs.eduro.go.kr/#/loginHome")
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="btnConfirm2"]').click()
print("성공적으로 접속됐습니다.\n")

print("기본 학교 정보를 제출합니다.\n")
time.sleep(0.5)
driver.find_element_by_xpath(
    '//*[@id="WriteInfoForm"]/table/tbody/tr[2]/td/button'
).click()
time.sleep(0.5)
Select(
    driver.find_element_by_xpath(
        '//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[1]/td/select'
    )
).select_by_visible_text(info["C/P"])
time.sleep(0.5)
Select(
    driver.find_element_by_xpath(
        '//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[2]/td/select'
    )
).select_by_visible_text(info["SL"])
time.sleep(0.5)
driver.find_element_by_xpath(
    '//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[1]/input'
).send_keys(info["SN"])
time.sleep(0.5)
driver.find_element_by_xpath(
    '//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button'
).click()
time.sleep(2)
driver.find_element_by_css_selector(
    "#softBoardListLayer > div.layerContentsWrap > div.layerSchoolSelectWrap > ul"
).click()
time.sleep(0.5)
driver.find_element_by_xpath(
    '//*[@id="softBoardListLayer"]/div[2]/div[2]/input'
).click()
print("제출완료\n")

print("이름 및 생년월일을 제출합니다.\n")
time.sleep(0.5)
driver.find_element_by_xpath(
    '//*[@id="WriteInfoForm"]/table/tbody/tr[3]/td/input'
).send_keys(info["NM"])
time.sleep(0.5)
driver.find_element_by_xpath(
    '//*[@id="WriteInfoForm"]/table/tbody/tr[4]/td/input'
).send_keys(info["BH"])
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
print("제출완료\n")

print("비밀번호를 제출합니다.\n")
time.sleep(0.5)
driver.find_element_by_xpath(
    '//*[@id="WriteInfoForm"]/table/tbody/tr/td/input'
).send_keys(info["PD"])
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
print("제출완료\n")

print("사용자를 선택합니다.\n")
time.sleep(2)
driver.find_element_by_css_selector(
    "#container > div:nth-child(1) > section.memberWrap > div:nth-child(2) > ul > li > a > button"
).click()

try:
    alert = driver.switch_to.alert
    message = alert.text
    left_time = re.findall(r"약(\d)분", message)[0]
    print(f"알림이 감지되었습니다. {left_time}분 후에 다시 시도합니다.\n")
    alert.accept()
except NoAlertPresentException:
    print("알림이 발견되지 않았습니다. 계속 진행합니다.\n")
else:
    time.sleep(int(left_time) * 60)
    driver.find_element_by_css_selector(
        "#container > div:nth-child(1) > section.memberWrap > div:nth-child(2) > ul > li > a > button"
    ).click()


print("선택완료\n")

print("항목을 체크합니다.\n")
time.sleep(2)

for i in range(1, 6):
    time.sleep(0.5)
    driver.find_element_by_css_selector(
        f"#container > div.subpage > div > div:nth-child(2) > div.survey_question > dl:nth-child({i}) > dd > ul > li:nth-child(1) > label"
    ).click()

driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
print("체크 완료\n")

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
