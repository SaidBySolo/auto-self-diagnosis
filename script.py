from selenium import webdriver
import json
import time
import datetime
import os
import sys
from discord.ext.commands import Bot as Bot
from utils.module import Module
from os import listdir
from os.path import isfile, join
import discord

module = Module()
settings = module.open('settings.json')
token = settings['token']
bot = Bot(command_prefix='Сове́тский Сою́з')
async def channelsend(content=None, File=None):
    channelid = 745844596176715806
    await bot.get_channel(channelid).send(content, file=File)

@bot.event
async def on_ready():
    await channelsend(f'{bot.user}에 로그인하였습니다!')
    await channelsend("설정파일을 읽습니다.\n")
    with open('./info.json', 'r', encoding='utf-8') as r:
        info = json.load(r)
    for info in info:
        try:
            now = datetime.datetime.now()
            nowtime = now.strftime('%Y-%m-%d_%H-%M-%S')
            await channelsend("로드완료! \n")
            options = webdriver.ChromeOptions()
            options.add_argument('window-size=1920x1080')
            options.add_argument(
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/83.0.4103.116 "
                    "Safari/537.36"
                    )
            if getattr(sys, 'frozen', False): 
                chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
                driver = webdriver.Chrome(chromedriver_path, options=options)
            else:
                driver = webdriver.Chrome('./chromedriver.exe', options=options)
            await channelsend("자가진단 홈페이지에 접속합니다.\n")
            driver.get(info['link'])
            await channelsend("성공적으로 접속됐습니다.\n")
            driver.find_element_by_xpath('//*[@id="container"]/div/div/div/div[2]/div/a[2]/div').click()
            time.sleep(0.5)
            driver.find_element_by_xpath('//*[@id="btnSrchSchul"]').click()
            time.sleep(0.5)
            driver.switch_to.window(driver.window_handles[-1])
            await channelsend("학교이름을 제출합니다.")
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
            await channelsend("제출완료!\n")
            driver.switch_to.window(driver.window_handles[0])
            await channelsend("생년월일과 이름을 제출합니다.\n")
            driver.find_element_by_xpath('//*[@id="pName"]').send_keys(info['name'])
            time.sleep(0.5)
            driver.find_element_by_xpath('//*[@id="frnoRidno"]').send_keys(info['birth'])
            await channelsend("완료!\n")
            time.sleep(0.5)
            await channelsend("체크중입니다.\n")
            driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
            time.sleep(0.5)
            try:
                driver.find_element_by_xpath('//*[@id="popupConfirm"]').click()
                time.sleep(1)      
            except:
                pass      
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
            await channelsend("전부 체크가 완료되고 제출되었어요!\n")
            if info['screen'] == True:
                await channelsend("스크린샷을 준비할게요!\n")
                if not os.path.exists("./screenshot"):
                    await channelsend("스크린샷 폴더가없는거같아요. 생성할게요!\n")    
                    os.mkdir("./screenshot")
                await channelsend("스크린샷을 찍을게요!\n")   
                driver.save_screenshot(f"./screenshot/{nowtime}_screenshot.png")
                if info.get('dm') == True:
                    try:
                        await bot.get_user(info['id']).send(file=discord.File(f"./screenshot/{nowtime}_screenshot.png"))
                        await channelsend("스크린샷을 DM으로 보냈어요!\n")   
                    except:
                        await channelsend(f"<@{info['id']}>, DM차단을 풀어주세요. 위 작업은 자가진단에 영향이 없습니다.")     
                else:               
                    await channelsend(File=discord.File(f"./screenshot/{nowtime}_screenshot.png"))
            await channelsend(f"<@{info['id']}>, 자가진단이 완료되었어요!\n")
            driver.quit()
            time.sleep(10)
        except Exception as e:
            await channelsend(e)
            return await bot.logout()
    await bot.logout()

bot.run(token)