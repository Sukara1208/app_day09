from base.base import Base
from page.pageelements import PageElements


class MmsNewPage(Base):

    def __init__(self):
        super().__init__()

    def click_mms_new_page(self):
        self.click_ele(PageElements.mms_new)

  