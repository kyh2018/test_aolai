import page
from base.base_action import BaseAction
import allure
"""
负责 个人中心页面逻辑
"""

class PersonCenterPage(BaseAction):

    def __init__(self,driver):
        BaseAction.__init__(self,driver)
    #点击个人中心的设置按钮
    @allure.step('进入个人中心设置页面')
    def click_person_center_setting(self):
        self.click_element(page.person_center_setting_btn)
    #判断一下是否登录成功 如果登录成功返回true 登录失败返回false
    @allure.step('判断是否登录成功')
    def is_login_sucess(self):
        try:
            self.find_element(page.person_center_all_order)
            return True
        except:
            return False
