from page.mms_page import MmsNewPage
from page.moremobilepage import MoreMobilePage
from page.network_page import NetWorkPage
from page.new_mms import NewMmsPage
from page.settingpage import SettingPage
from util import DriverApp


class Page:
    def __init__(self):
        self.driver = DriverApp.remote_driver()

    def get_setting_page(self):
        '''返回 -- 设置页面实例化对象'''
        return SettingPage()

    def get_more_mobile_page(self):
        '''返回 -- 更多页面实例化对象'''
        return MoreMobilePage()

    def get_network_page(self):
        '''返回 -- 移动网络页面'实例化对象'''
        return NetWorkPage()
    
    def mms_page(self):
        '''返回 -- 信息页面'实例化对象'''
        return MmsNewPage()
    
    def new_mms_page(self):
        '''返回 -- 新信息页面'实例化对象'''
        return NewMmsPage()
