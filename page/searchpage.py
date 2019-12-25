from selenium.webdriver.common.by import By

from base.base import Base
from page.pageelements import PageElements


class PageSearch(Base):

    def __init__(self):
        super().__init__()
        
    def click_search_btn(self):
        '''点击搜索按钮'''
        self.click_ele(PageElements.search_btn)

    def send_search_input(self, text):
        self.send_ele(PageElements.search_input, text)

    def get_search_results(self):
        results = self.find_elements(PageElements.search_result)
        return [i.text for i in results]
