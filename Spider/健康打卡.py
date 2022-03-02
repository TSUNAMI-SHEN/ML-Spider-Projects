import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
#预约机时
#FIRST STEP
driver = webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chromedriver.exe')
driver.get("https://healthreport.zju.edu.cn/ncov/wap/default/index")  # 地址栏里输入健康打卡的网址
driver.implicitly_wait(1)  # 设置隐式等待时间
driver.find_element_by_xpath("//*[@id='username']").send_keys("22026103") # 模拟按键输入
driver.find_element_by_xpath("//*[@id='password']").send_keys("szsxh0352xx") # 模拟按键输入
driver.find_element_by_xpath("//*[@id='dl']").click()

driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section/div[4]/ul/li[4]/div/div/div[2]/span[2]").click()
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section/div[4]/ul/li[5]/div/div/div[2]/span[2]").click()
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section/div[4]/ul/li[6]/div/div/div[2]/span[2]").click()
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section/div[4]/ul/li[7]/div/div/div[2]/span[2]").click()
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section/div[4]/ul/li[8]/div/div/div[2]/span[2]").click()
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section/div[4]/ul/li[9]/div/div/div[2]/span[2]").click()
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section/div[4]/ul/li[10]/div/div/div[2]/span[2]").click()
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section/div[4]/ul/li[11]/div/div/div[2]/span[2]").click()
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section/div[4]/ul/li[12]/div/div/div[2]/span[2]").click()
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section/div[4]/ul/li[13]/div/div/div[2]/span[2]").click()
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section/div[4]/ul/li[14]/div/div/div[2]/span[2]").click()
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section/div[4]/ul/li[15]/div/div/div[2]/span[2]").click()
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section/div[4]/ul/li[16]/div/div/div[1]/span[2]").click()
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section/div[4]/ul/li[17]/div/div/div[1]/span[2]").click()
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section/div[4]/ul/li[18]/div/div/div[2]/span[2]").click()
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section/div[4]/ul/li[19]/div/div/div[1]/span[2]").click()
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section/div[4]/ul/li[20]/div/div/div[1]/span[2]").click()

driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section/div[4]/ul/li[23]/div/input").click()

driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section/div[4]/ul/li[26]/div/div/div[2]/span[2]").click()
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section/div[4]/ul/li[38]/div/div/div/span[2]").click()
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section/div[5]/div/a").click()
driver.find_element_by_xpath("//*[@id='wapcf']/div/div[2]/div[2]").click()
driver.quit()
