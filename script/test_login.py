import os,sys
import pytest
sys.path.append(os.getcwd())
from base.read_yaml_data import read_yaml_data

from page.navigation_page import NavigationPage
from base.base_driver import init_driver
import time

def get_data():
    data_list = []
    data = read_yaml_data("login_data.yaml")
    for i in data.keys():
        data2 = data.get(i)
        name = data2.get("username")
        passwd = data2.get("password")
        tag = data2.get("tag")
        except_msg = data2.get("except_msg")
        get_toast_msg = data2.get("get_toast_msg")
        data_list.append((name,passwd,tag,get_toast_msg,except_msg))
    return data_list


class TestLogin:
    #初始化导航类
    def setup_class(self):
        #1.初始化driver对象
        self.driver = init_driver('com.yunmall.lc','com.yunmall.ymctoc.ui.activity.MainActivity')
        #2.初始化导航对象
        self.navigation_page = NavigationPage(self.driver)
    def teardown_class(self):
        time.sleep(5)
        self.driver.quit()
    #测试登录业务
    @pytest.mark.parametrize("username,password",get_data())
    def test_login(self,username,password):
        #1.点击我的
        self.navigation_page.get_home_page_obj().click_my_button()
        #2.点击已有账号去登录
        self.navigation_page.get_sign_in_page_obj().click_exist_accout()
        #3.输入用户名 密码  点击登录
        self.navigation_page.get_login_page_obj().login_in(username,password)
        #4.点击个人中心设置按钮
        self.navigation_page.get_person_center_page_obj().click_person_center_setting()
        #5.点击退出
        self.navigation_page.get_setting_page_obj().logout_account()

    #测试登录错误逻辑
    @pytest.mark.parametrize("username,password,tag,get_toast_msg,except_msg", get_data())
    def test_login2(self,username,password,tag,get_toast_msg,except_msg):
        #1.点击我的
        self.navigation_page.get_home_page_obj().click_my_button()
        #2.点击已有账号去登录
        self.navigation_page.get_sign_in_page_obj().click_exist_accout()
        #3.输入用户名 密码  点击登录
        self.navigation_page.get_login_page_obj().login_in(username,password)
        #4.获取真正弹出吐司的消息
        toast_msg = self.navigation_page.get_setting_page_obj().get_toast_message(get_toast_msg)
        print(toast_msg)
        assert toast_msg == except_msg
        #5.关闭当前登录页面
        self.navigation_page.get_login_page_obj().close_login_page()


