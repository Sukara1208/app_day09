import time
import pytest
from selenium.webdriver.common.by import By
from base.base import Base
from util import DriverApp


class TestSms:

    def setup_class(self):
        self.driver = DriverApp.remote_driver(appPackage="com.android.mms", appActivity=".ui.ConversationList")
        self.base = Base()

    def teardown_class(self):
        DriverApp.quit_driver()

    @pytest.fixture(autouse=True, scope="class")
    def goto_sms(self):
        self.base.click_ele((By.XPATH, "//*[contains(@resource-id,'com.android.mms:id/action_compose_new')]"))
        # self.base.click_ele((By.ID, "com.android.mms:id/action_compose_new"))
        self.base.send_ele((By.XPATH, "//*[contains(@text,'接收者')]"),"18010495003")

    @pytest.mark.parametrize("msg", ["hello", "python", "appium"])
    def test_sms(self, msg):
        '''发送短信'''
        self.base.send_ele((By.XPATH, "//*[contains(@text,'键入信息')]"), msg)
        self.base.click_ele((By.ID, "com.android.mms:id/send_button_sms"))
        slium = self.base.find_elements((By.ID, "com.android.mms:id/text_view"))[-1]
        assert msg in slium.text

if __name__ == '__main__':
    pytest.main(["test_10_send_sms.py","-s"])