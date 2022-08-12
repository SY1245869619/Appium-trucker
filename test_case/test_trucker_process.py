# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: test_trucker_process.py
@time: 2021/10/6 22:02
"""
import pytest
from time import sleep
from appium import webdriver
from PublicAction import Appium_Start, ActionPublic
from AppAction import GetIntoApp, AppSignIn, AppNews, AppSourceList, AppSourceDetails, AppWaybill, AppMyPage


class TestDemo:
    Appium_Start.appium_start('0.0.0.0', 4723)

    def setup_class(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "fxwl"
        caps["app"] = "../app/trucker-daily5.1.6.apk"
        caps["autoGrantPermissions"] = True
        # caps["noReset"] = True
        # caps["ensureWebviewsHavePages"] = True
        # 连接远程地址
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 增加隐式等待
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        self.driver.quit()

    # 初始进入app的操作集测试用例
    def test_GetIntoApp(self):
        GetIntoApp.GetIntoApp(self)

    # App登录功能的操作集测试用例
    def test_AppSignIn(self):
        AppSignIn.AppSignIn(self)

    # App消息功能的操作集测试用例
    def test_AppNews(self):
        AppNews.AppNews(self)

    # App货源列表的操作集测试用例
    def test_AppSourceList(self):
        AppSourceList.AppSourceList(self)

    # App货源详情页操作集测试用例
    def test_AppSourceDetails(self):
        AppSourceDetails.AppSourceDetails(self)

    # App运单页操作集测试用例
    def test_AppWaybill(self):
        AppWaybill.AppWaybill(self)

    # App我的页操作集测试用例
    def test_AppMyPage(self):
        AppMyPage.AppMyPage(self)

    def test_demo1(self):
        # 点击注册/登录按钮
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/ll_user_center_auth_status").click()
        # 切换为密码登录
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/tv_password_login").click()
        # 点击手机号输入框
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/et_phone").click()
        # 输入手机号
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/et_phone").send_keys("13171521557")
        # 点击密码输入框
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/et_verify_code").click()
        # 输入密码
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/et_verify_code").send_keys("cs123456")
        # 点击登录按钮
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/btn_login").click()
        sleep(5)
