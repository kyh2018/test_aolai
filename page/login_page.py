import page
from base.base_action import BaseAction
import  allure
"""
负责登录页面的逻辑
"""
class LoginPage(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    @allure.step('登录逻辑')
    def login_in(self,name,pwd):
        # 1.输入账号  账号的数据不能写死 应该是从脚本里面动态传入
        allure.attach('登录', '请输入账号')
        self.input_element_content(page.login_username_id,name)
        # 2.输入密码
        allure.attach('登录', '请输入密码')
        self.input_element_content(page.login_password_id,pwd)
        # 3.点击登录按钮
        allure.attach('登录', '点击登录按钮')
        self.click_element(page.login_login_in_btn)

    def close_login_page(self):
        self.click_element(page.login_login_out_btn)
