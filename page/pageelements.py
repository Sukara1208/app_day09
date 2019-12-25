from selenium.webdriver.common.by import By


class PageElements:
    """项目元素定位"""

    '''搜索页面元素定位'''
    # 搜索按钮
    search_btn = (By.ID, "com.android.settings:id/search")
    # 输入框
    search_input = (By.ID, "android:id/search_src_text")
    # 搜索结果
    search_result = (By.ID, "com.android.settings:id/title")

    '''设置页面'''
    # 设置页面内 - 更多
    set_more_mobile = (By.XPATH, "//*[contains(@text,'更多')]")

    '''更多页面'''
    # 更多页面 - 移动网络
    more_mobile_network = (By.XPATH, "//*[contains(@text,'移动网络')]")

    '''移动网络页面'''
    # 移动网络页面 - 网络类型
    mobile_network_type = (By.XPATH, "//*[contains(@text,'首选网络类型')]")
    # 移动网络页面 - 网络类型 - 选择2G
    mobile_network_2g = (By.XPATH, "//*[contains(@text,'2G')]")
    # 移动网络页面 - 灰色字
    mobile_network_summary = (By.ID, "android:id/summary")

    '''信息页面'''
    # 信息页面  --  右下角新建信息
    mms_new = (By.ID, "com.android.mms:id/action_compose_new")

    '''新信息页面'''
    # 新信息页面 --  接收者
    new_mms_accepter = (By.ID, "com.android.mms:id/recipients_editor")
    # 新信息页面 --  键入信息
    new_mms_write = (By.ID, "com.android.mms:id/embedded_text_editor")
    # 新信息页面 --  发送按钮
    new_mms_send = (By.ID, "com.android.mms:id/send_button_sms")
    # 新信息页面 --  页面发送消息内容
    new_mms_content = (By.ID, "com.android.mms:id/text_view")
