from base.base import Base
from page.pageelements import PageElements


class MoreMobilePage(Base):
    def __init__(self):
        super().__init__()

    def clik_more_mobile_network(self):
        self.click_ele(PageElements.more_mobile_network)