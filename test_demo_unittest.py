# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: test_demo_pytest.py
@time: 2021/10/4 21:18
"""

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from unittest import TestCase


class TestDemo(TestCase):
    def setUp(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "fxwl"
        caps["app"] = "E:\\文件\\Appiumtest\\dailyTrucker-1.5.55-117-debug.apk"
        caps["autoGrantPermissions"] = True
        caps["ensureWebviewsHavePages"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 增加隐式等待
        self.driver.implicitly_wait(10)

    def test_demo(self):
        # 协议弹窗点击同意
        el1 = self.driver.find_element_by_id("com.kachexiongdi.trucker:id/btn_dialog_confirm")
        el1.click()
        # 启动图滑动2次
        TouchAction(self.driver).press(x=1058, y=1079).move_to(x=154, y=1066).release().perform()
        TouchAction(self.driver).press(x=1028, y=1058).move_to(x=176, y=1058).release().perform()
        # 点击立即体验按钮
        # TouchAction(self.driver).tap(x=630, y=1822).perform()
        el2 = self.driver.find_element_by_id("com.kachexiongdi.trucker:id/b_enter")
        el2.click()
        # 增加隐式等待
        self.driver.implicitly_wait(10)
        # 点击“我的”
        el3 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                                ".widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                                ".LinearLayout/android.widget.RelativeLayout/android.widget"
                                                ".FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout"
                                                "/android.widget.RelativeLayout["
                                                "3]/android.widget.LinearLayout/android.view.View")
        el3.click()
        # 点击“登录/注册”按钮
        el4 = self.driver.find_element_by_id("com.kachexiongdi.trucker:id/user_center_enter")
        el4.click()

    def tearDown(self):
        self.driver.quit()