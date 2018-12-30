from appium import webdriver


def init_driver(s, s1):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'  # 平台名称
    desired_caps['platformVersion'] = '5.1'  # 平台版本
    desired_caps['deviceName'] = '192.168.56.101:5555'  # 设备号
    # 支持Toast
    desired_caps['automationName'] = 'Uiautomator2'
    desired_caps['appPackage'] = 'com.yunmall.lc'  # 应用的包名
    desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'  # 代表启动的activity
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 声明driver对象