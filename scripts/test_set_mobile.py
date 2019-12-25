import pytest,sys,os

sys.path.append(os.getcwd())
# print("os.getcwd()",os.getcwd())
# print("os.getcwd()",os.getcwd())
from page.searchpage import PageSearch
from util import DriverApp


class TestSet:

    def setup_class(self):
        self.driver = DriverApp.remote_driver(appPackage="com.android.settings", appActivity=".Settings")
        self.pageserach = PageSearch()
    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(autouse=True, scope="class")
    def goto_serach(self):
        self.pageserach.click_search_btn()


    @pytest.mark.parametrize("sea_data,exp_data", [("1", "休眠"), ("m", "MAC地址"), ("w", "WPS按钮")])
    def test_01(self, sea_data, exp_data):
        self.pageserach.send_search_input(sea_data)
        assert exp_data in self.pageserach.get_search_results()

if __name__ == '__main__':
    pytest.main(["test_09_lianxi_set.py"])