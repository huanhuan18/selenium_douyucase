# -*- coding: utf-8 -*-

from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains   # 鼠标
import datetime
import random
import threading
import multiprocessing

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from time import sleep
import traceback
import time, sys

options = Options()    # 实例化一个启动参数对象
# options.add_argument('--headless')       #设置无界面模式运行浏览器
options.add_argument('--start-maximized')      #设置启动浏览器时窗口最大化运行
options.add_argument('--incognito')            #设置无痕模式
options.add_argument('--disable-infobars')     #设置禁用浏览器正在被自动化程序控制的提示
# options.add_argument('--window-size=1928,1080')       #设置浏览器分辨率窗口大小
options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(options=options)

# driver.execute_script('''
#     window._showModalDialog = window.showModalDialog;
#     window.showModalDialog = window.open;
# ''')


def login():
    driver.implicitly_wait(10)  # 10s内只要找到元素就执行

    driver.get('https://www.douyu.com/')


    driver.find_element_by_xpath("//header//span[@class='UnLogin-icon']").click()

    # WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it('login-passport-frame'))
    driver.switch_to.frame("login-passport-frame")
    driver.find_element_by_xpath("//div[@class='scancode-link clearfix']/span[@data-type]").click()
    driver.find_element_by_xpath("//a[@class='fl third-icon third-icon-qq']").click()
    allhandle = driver.window_handles
    # sleep(3)
    driver.switch_to.window(allhandle[1])
    driver.switch_to.frame("ptlogin_iframe")
    driver.find_element_by_id("img_out_848368042").click()

    # 鼠标悬浮在分类上
    Webelement = driver.find_element_by_xpath("//div[@class='public-DropMenu Category ']//span")
    ActionChains(driver).move_to_element(Webelement).perform()
    driver.find_element_by_link_text("英雄联盟").click()

    # 滚动条到视频位置
    driver.switch_to.window(driver.window_handles[2])
    sleep(2)
    target = driver.find_element_by_xpath("//ul[@class='layout-Cover-list' ]/li[3]")
    driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)

    # 找到第三个视频点关注并获取视频标题
    Webelement = driver.find_element_by_xpath("//ul[@class='layout-Cover-list' ]/li[3]")
    ActionChains(driver).move_to_element(Webelement).perform()
    titlename = driver.find_element_by_xpath("//ul[@class='layout-Cover-list' ]/li[3]//h3").text
    try:
        my_love = "//ul[@class='layout-Cover-list' ]/li[3]//div[@class='DyListCover-btn ']"
        driver.find_element_by_xpath(my_love).click()
    except:
        pass
    sleep(2)

    # 进入我的关注通过标题进入直播间
    driver.find_element_by_xpath("//header//div[@class='Header-right']/div[3]/div[1]").click()
    driver.find_element_by_xpath("//h2[text()='{}']".format(titlename)).click()

    # 进入直播间计时并发送弹幕
    starttime = datetime.datetime.now()
    sleep(3)
    allhandle = driver.window_handles
    driver.switch_to.window(allhandle[3])
    # wait = ui.WebDriverWait(driver,10)
    # wait.until(lambda driver: driver.find_element_by_xpath("//span[@class='SuperFansGuideTips-close']").click())
    try:
        driver.find_element_by_xpath("//span[@class='SuperFansGuideTips-close']").click()
        driver.find_element_by_xpath("//i[@class='PcDiversion-close']").click()
    except:
        pass

    # 伪节点::before   ::after 用css定位
    sendword = driver.find_element_by_css_selector("div.ChatSend>textarea")
    driver.execute_script("arguments[0].scrollIntoView();", sendword)
    # sendword.click()
    sendword.send_keys("666")
    sleep(1)
    sendbtn = driver.find_element_by_css_selector("div.ChatSend-button ")
    driver.execute_script("arguments[0].click();", sendbtn)
    waittime = random.randint(5, 10)
    sleep(waittime)
    driver.close()
    endtime = datetime.datetime.now()
    interval = (endtime - starttime).seconds
    print("您在{}直播间观看了{}s".format(titlename, interval))
    driver.quit()


def unlogin():
    # driver.implicitly_wait(10)  # 10s内只要找到元素就执行

    driver.get('https://www.douyu.com/')

    driver.find_element_by_xpath("//div[@class='public-DropMenu Category ']//span").click()
    sleep(3)

    # 选择颜值 > 跳舞
    target = driver.find_element_by_link_text("颜值")
    driver.execute_script("arguments[0].scrollIntoView();", target)
    target.click()
    sleep(3)
    dance = driver.find_element_by_xpath("//span[text()='跳舞']")
    driver.execute_script("arguments[0].scrollIntoView();", dance)
    dance.click()
    sleep(2)

    # 进入第一个直播间
    driver.find_element_by_xpath("//section[@id='listAll']/div[2]/ul[1]/li[1]/div").click()
    sleep(4)
    allhand = driver.window_handles
    driver.switch_to.window(allhand[1])
    sleep(2)
    try:
        driver.find_element_by_xpath("//span[@class='SuperFansGuideTips-close']").click()
        driver.find_element_by_xpath("//i[@class='PcDiversion-close']").click()
        driver.find_element_by_xpath("//div[@class='ActPayDialog-close']").click()
    except:
        pass
    sleep(10)
    driver.close()

    # 进入第二个直播间
    driver.switch_to.window(allhand[0])
    driver.find_element_by_xpath("//section[@id='listAll']/div[2]/ul[1]/li[2]/div").click()
    sleep(4)
    allhand = driver.window_handles
    driver.switch_to.window(allhand[1])
    sleep(2)
    try:
        driver.find_element_by_xpath("//span[@class='SuperFansGuideTips-close']").click()
        driver.find_element_by_xpath("//i[@class='PcDiversion-close']").click()
        driver.find_element_by_xpath("//div[@class='ActPayDialog-close']").click()
    except:
        pass
    sleep(8)
    driver.quit()


if __name__ == "__main__":
    threads = []
    t1 = threading.Thread(target=unlogin())
    threads.append(t1)
    t2 = threading.Thread(target=login())
    threads.append(t2)
    for t in threads:
        t.start()
        t.join()



