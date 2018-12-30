import page
from base.base_action import BaseAction
import allure
"""
负责 设置页面相关逻辑
"""


class SettingPage(BaseAction):

    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    @allure.step('退出账号')
    # 退出当前登录的账号
    def logout_account(self):
        # 1.滑动页面低端 才会看见退出按钮 才能找到元素 drag
        allure.attach('退出账号', '向上滑动')
        self.swipe_screen(1)
        # 2.点击退出按钮
        allure.attach('退出账号', '点击退出按钮')
        self.click_element(page.setting_center_login_out_btn)
        # 3.点击弹出对话框确定按钮
        allure.attach('退出账号', '点击确认按钮')
        self.click_element(page.setting_center_login_dialog_confirm_btn)



