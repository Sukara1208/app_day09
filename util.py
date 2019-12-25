import time

from appium import webdriver


class DriverApp:
    driver = None
    @classmethod
    def remote_driver(cls,appPackage="com.android.settings",appActivity=".Settings",url="http://127.0.0.1",duankou=":8888"):
        if cls.driver is None:
            capabilities = {
                "platformName": "Android",  # 操作平台（Android 和iOS）,不区分大小写
                "platformVersion": "5.1",  # 系统版本号，可以不添加，但必须和设备版本号一致否则报错
                "deviceName": "1",  # 设备名称，不能省略，起标记设备名称的作用
                "appPackage": appPackage,  # 待测应用的包名
                "appActivity": appActivity  # 待测应用的启动名
            }
            cls.driver = webdriver.Remote(command_executor=f'{url}{duankou}/wd/hub',
                                           desired_capabilities=capabilities)
        return cls.driver
    @classmethod
    def quit_driver(cls):
        if cls.driver is not None:
            cls.driver.quit()
            cls.driver = None

if __name__ == '__main__':
    DriverApp.remote_driver()
    time.sleep(3)
    DriverApp.quit_driver()

