from page.home_page import HomePage
from page.login_page import LoginPage
from page.person_center_page import PersonCenterPage
from page.setting_page import SettingPage
from page.sign_in_page import SignInPage
"""
负责 获取home_page, login_page, person_center_page ,setting_page,sign_page的实例
"""
class NavigationPage:
    # 初始化的时候 谁调用我 谁给我一个driver
    def __init__(self,driver):
        self.driver = driver
    #获取home_page的实例
    def get_home_page_obj(self):
        return HomePage(self.driver)

    # 获取login_page的实例
    def get_login_page_obj(self):
        return LoginPage(self.driver)

    # 获取person_center_page的实例
    def get_person_center_page_obj(self):
        return PersonCenterPage(self.driver)

    # 获取setting_center_page的实例
    def get_setting_page_obj(self):
        return SettingPage(self.driver)

    # 获取sign_in_page的实例
    def get_sign_in_page_obj(self):
        return SignInPage(self.driver)

