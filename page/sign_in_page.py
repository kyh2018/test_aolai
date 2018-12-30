import page
from base.base_action import BaseAction
import allure

"""
注册页面
"""
class SignInPage(BaseAction):
    #初始化函数 动态把driver传入
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    @allure.step('点击已有账号')
    def click_exist_accout(self):
        self.click_element(page.sign_in_exit_account_id)



