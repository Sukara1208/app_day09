from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from util import DriverApp


class Base:
    def __init__(self,appPackage="com.android.settings", appActivity=".Settings"):
        self.driver = DriverApp.remote_driver(appPackage,appActivity)

    def find_element(self, loc, timeout=5, poll_frequency=0.5):
        '''
        定位单个元素
        :param loc:元祖（定位方式，定位依据）
        :param timeout:显示等待 - 搜索元素超时时间
        :param poll_frequency:定位间隔时间
        :return:元素对象
        '''
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def find_elements(self, loc, timeout=5, poll_frequency=0.5):
        '''
        定位一组元素，列表形式
        :param loc:元祖（定位方式，定位依据）
        :param timeout:显示等待 - 搜索元素超时时间
        :param poll_frequency:定位间隔时间
        :return:元素对象
        '''
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_ele(self, loc, timeout=5, poll_frequency=0.5):
        self.find_element(loc, timeout, poll_frequency).click()


    def send_ele(self, loc, text, timeout=5, poll_frequency=0.5):
        my_ele = self.find_element(loc, timeout, poll_frequency)
        my_ele.clear()
        my_ele.send_keys(text)


if __name__ == '__main__':
    driver = DriverApp.remote_driver(appPackage="com.android.contacts",appActivity=".activities.PeopleActivity")
    base = Base()
    base.click_ele((By.XPATH,'//*[contains(@text,"pan")]'))