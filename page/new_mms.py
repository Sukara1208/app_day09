from base.base import Base
from page.pageelements import PageElements


class NewMmsPage(Base):

    def __init__(self):
        super().__init__()

    def click_accepter(self, text_accepter):
        self.send_ele(PageElements.new_mms_accepter, text_accepter)

    def send_new_mms(self, text_write):
        self.send_ele(PageElements.new_mms_write, text_write)
        self.click_ele(PageElements.new_mms_send)

    def assert_new_mms_content(self):
        return [i.text for i in self.find_elements(PageElements.new_mms_content)]
