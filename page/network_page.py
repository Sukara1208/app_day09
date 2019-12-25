from base.base import Base
from page.pageelements import PageElements


class NetWorkPage(Base):
    def __init__(self):
        super().__init__()

    def clik_mobile_network_type(self):
        self.click_ele(PageElements.mobile_network_type)

    def click_mobile_network_2g(self):
        self.click_ele(PageElements.mobile_network_2g)

    def assert_mobile_network_summary(self):
        return [i.text for i in self.find_elements(PageElements.mobile_network_summary)]
