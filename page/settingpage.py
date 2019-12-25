from base.base import Base
from page.pageelements import PageElements


class SettingPage(Base):
    def __init__(self):
        super().__init__()

    def clik_more_mobile(self):
        self.click_ele(PageElements.set_more_mobile)