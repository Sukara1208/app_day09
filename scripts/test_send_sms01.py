import sys, os
import time

sys.path.append(os.getcwd())

from util import DriverApp

import pytest

from base.page import Page


class TestMmsSend:

    def setup_class(self):
        self.driver = DriverApp.remote_driver("com.android.mms", ".ui.ConversationList")
        self.page = Page()

    def teardown_class(self):
        DriverApp.quit_driver()

    @pytest.fixture(scope="class", autouse=True)
    def goto_new_mms(self):
        self.page.mms_page().click_mms_new_page()
        self.page.new_mms_page().click_accepter("13012345677")

    @pytest.mark.parametrize("mss", ["hello", "python", "appium"])
    def test_send_mms(self, mss):
        self.page.new_mms_page().send_new_mms(mss)
        time.sleep(2)
        assert mss in self.page.new_mms_page().assert_new_mms_content()
