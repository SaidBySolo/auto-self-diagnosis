from selenium import webdriver
import json
import time
import datetime
import os
import sys
print('설정파일을 엽니다!\n')
with open('./info.json', 'r', encoding='utf-8') as r:
    info = json.load(r)
print('로딩 완료!\n')
options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("window-size=1920x1080")
options.add_argument("Chrome/85.0.4183.83")
options.add_argument("disable-gpu")
if getattr(sys, 'frozen', False):
    chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
    driver = webdriver.Chrome(chromedriver_path, options=options)
else:
    driver = webdriver.Chrome('./chromedriver.exe', options=options)
print('자가진단 사이트에 접속합니다\n')
driver.get('https://hcs.eduro.go.kr/#/loginHome')
print('접속 완료!\n')
print('정보를 제출합니다.\n')
region = {
    "서울특별시": "1",
    "부산광역시": "2",
    "대구광역시": "3",
    "인천광역시": "4",
    "광주광역시": "5",
    "대전광역시": "6",
    "울산광역시": "7",
    "세종특별자치시": "8",
    "경기도": "10",
    "강원도": "11",
    "충청북도": "12",
    "충정남도": "13",
    "전라북도": "14",
    "전라남도": "15",
    "경상북도": "16",
    "경상남도": "17",
    "경상남도": "18",
}
level = {
    "유치원": "1",
    "초등학교": "2",
    "중학교": "3",
    "고등학교": "4",
    "특수학교": "5"
}
try:
    region = region.get(info['region'])
    if region == None:
        driver.quit()
        raise Exception("지역 잘못기재로인한 종료")
    level = region.get(info['region'])
    if region == None:
        driver.quit()
        raise Exception("학교 소속 잘못기재로인한 종료")
    driver.find_element_by_xpath('//*[@id="btnConfirm2"]').click()
    driver.find_element_by_xpath(
        '//*[@id="WriteInfoForm"]/table/tbody/tr[1]/td/button').click()
    driver.find_element_by_xpath(
        '//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[1]/td/select/option[6]').click()
    driver.find_element_by_xpath(
        '//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[2]/td/select/option[4]').click()
    driver.find_element_by_xpath(
        '//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[1]/input').send_keys(info['schoolname'])
    driver.find_element_by_xpath(
        '//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button').click()
    time.sleep(0.5)
    action = webdriver.ActionChains(driver)
    school = driver.find_element_by_class_name('layerSchoolArea')
    action.move_to_element(school)
    school.click()
    driver.find_element_by_xpath(
        '//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()
    driver.find_element_by_xpath(
        '//*[@id="WriteInfoForm"]/table/tbody/tr[2]/td/input').send_keys(info['name'])
    driver.find_element_by_xpath(
        '//*[@id="WriteInfoForm"]/table/tbody/tr[3]/td/input').send_keys(info['birth'])
    driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
except Exception as e:
    print('학교이름, 본인실명, 생년월일을 제출하던 도중 오류가 발생하였습니다! 아래의 내용을 이슈에 넣어주세요!\n')
    print(f'{e}\n')
    driver.quit()
    raise Exception("오류로인한 종료")
print('제출 완료!\n')
print('비밀번호를 제출합니다\n')
try:
    time.sleep(1)
    password = driver.find_element_by_class_name('input_text_common')
    password.send_keys(info['passwd'])
    driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
except Exception as e:
    print('비밀번호를 제출하던 도중 오류가 발생하였습니다! 아래의 내용을 이슈에 넣어주세요!\n')
    print(f'{e}\n')
    driver.quit()
    raise Exception("오류로인한 종료")
print('제출 완료!\n')
print('자가진단을 제출하겠습니다\n')
try:
    time.sleep(1.5)
    action = webdriver.ActionChains(driver)
    user = driver.find_element_by_xpath(
        '//*[@id="container"]/div[2]/section[2]/div[2]/ul/li/a/button')
    action.move_to_element(user)
    user.click()
    time.sleep(2)
    xpath = [
        '//*[@id="container"]/div[2]/div/div[2]/div[2]/dl[1]/dd/ul/li[1]/label',
        '//*[@id="container"]/div[2]/div/div[2]/div[2]/dl[2]/dd/ul/li[1]/label',
        '//*[@id="container"]/div[2]/div/div[2]/div[2]/dl[3]/dd/ul/li[1]/label',
        '//*[@id="container"]/div[2]/div/div[2]/div[2]/dl[4]/dd/ul/li[1]/label',
        '//*[@id="container"]/div[2]/div/div[2]/div[2]/dl[5]/dd/ul/li[1]/label',
        '//*[@id="btnConfirm"]'
    ]
    for i in xpath:
        driver.find_element_by_xpath(i).click()
        time.sleep(0.5)
except Exception as e:
    print('자가진단을 제출하던 도중 오류가 발생하였습니다! 아래의 내용을 이슈에 넣어주세요!\n')
    print(f'{e}\n')
    driver.quit()
    raise Exception("오류로인한 종료")
print('제출 완료!')
if info['screen'] == True:
    print("스크린샷을 준비할게요!\n")
    if not os.path.exists("./screenshot"):
        print("스크린샷 폴더가없는거같아요. 생성할게요!\n")
        os.mkdir("./screenshot")
    print("스크린샷을 찍을게요!\n")
    now = datetime.datetime.now()
    nowtime = now.strftime('%Y-%m-%d_%H-%M-%S')
    driver.save_screenshot(f"./screenshot/{nowtime}_screenshot.png")
print("자가진단이 완료되었습니다!\n")
driver.quit()
