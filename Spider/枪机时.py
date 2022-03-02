from splinter.browser import Browser
from time import sleep
import traceback

class Rob_Machine(object):
    def __init__(self, username, passwd, start_time, end_time):
        self.username = username
        self.passwd = passwd
        self.start_time = start_time
        self.end_time = end_time
        self.login_url = 'http://cem.ylab.cn/login.action'
        self.initMy_url = 'http://cem.ylab.cn/user/home.action'
        self.rob_old_F20_url = 'http://cem.ylab.cn/user/listReserve.action?instrumentId=28ad18ae3ebb4f91b1d52553019ca381'
        self.rob_new_F20_url = 'http://cem.ylab.cn/user/listReserve.action?instrumentId=563e690aae7b41dfb6da1880f291e65b'
        self.driver_name = 'chrome'
        self.executable_path = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'

    def login(self):
        self.driver.visit(self.login_url)
        self.driver.fill('username', self.username)
        sleep(1)

        self.driver.fill('password', self.passwd)
        sleep(1)

    def start_rob(self):
        self.driver = Browser(driver_name=self.driver_name, executable_path=self.executable_path)

        self.driver.driver.set_window_size(700,500)
        self.login()
        self.driver.visit(self.rob_old_F20_url)
        try:
            print('开始抢机时...')
            self.driver.find_by_class('sess resttime').click()
            sleep(1)
            self.driver.find_by_id('resv-start-time', self.start_time).click()
            sleep(1)
            self.driver.find_by_id('resv-end-time', self.end_time).click()
            sleep(1)
            self.driver.find_by_id('submitBtn').click()
            sleep(1)
            self.driver.find_by_text('确认').click()
            print('Rob Meachine Sucessfully!')
        except Exception as e:
            print(e)

if __name__ == '__main__':
    username = 'TEMWizard'
    password = 'szsxh0352xx'
    start_time = '0:00'
    end_time = '0:30'

    Rob_Machine(username, password, start_time, end_time)
