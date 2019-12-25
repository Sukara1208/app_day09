import sys, os

sys.path.append(os.getcwd())

from base.page import Page
from util import DriverApp


class TestSetNetwork:

    def setup_class(self):
        self.driver = DriverApp.remote_driver()
        self.page = Page()

    def teardown_class(self):
        DriverApp.quit_driver()

    def test_set_network(self):
        self.page.get_setting_page().clik_more_mobile()
        self.page.get_more_mobile_page().clik_more_mobile_network()
        self.page.get_network_page().clik_mobile_network_type()
        self.page.get_network_page().click_mobile_network_2g()
        assert "2G" in self.page.get_network_page().assert_mobile_network_summary()
