# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: GetIntoApp.py
@time: 2022/4/26 17:36
"""
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from PublicAction import ActionPublic


# 初始进入App的操作集合
def GetIntoApp(self):
    try:
        self.driver.implicitly_wait(5)
        # 点击第一个协议
        # 使用Appium的定位策略
        self.driver.find_element(AppiumBy.ID, "com.kachexiongdi.trucker:id/owner_auth_rule").click()
        sleep(2)
        # 调用系统自带返回按钮
        self.driver.back()
        # self.driver.keyevent('4')
        # 点击第二个协议
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/owner_privacy_policy").click()
        sleep(2)
        # 调用系统自带返回按钮
        self.driver.back()
        # 协议弹窗点击确定按钮
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/btn_dialog_confirm").click()
        try:
            assert len(
                self.driver.find_elements("id", "com.android.permissioncontroller:id/permission_allow_button")) == 1
            self.driver.find_element("id",
                                     "com.android.permissioncontroller:id/permission_allow_button").click()  # 协议弹窗点击同意
            print("\n存在权限弹窗，点击允许\n")
        except AssertionError:
            print("不存在权限弹窗\n")
        # 启动图滑动1次
        ActionPublic.swipe_left(self.driver)
        # 点击立即体验按钮
        try:
            assert len(self.driver.find_elements("id", "com.kachexiongdi.trucker:id/b_enter")) == 1
            self.driver.find_element("id", "com.kachexiongdi.trucker:id/b_enter").click()
            print("存在立即体验按钮，可以向下\n")
        except AssertionError:
            print("无法点击立即体验按钮\n")
        sleep(1)
        try:
            assert len(self.driver.find_elements("id","com.android.permissioncontroller:id"
                                                      "/permission_allow_always_button")) == 1
            # 协议弹窗点击同意
            self.driver.find_element("id","com.android.permissioncontroller:id/permission_allow_always_button").click()
            print("\n存在权限弹窗，点击始终允许\n")
        except AssertionError:
            print("不存在权限弹窗\n")
        # 点击“我的”
        # 真机
        self.driver.find_element("xpath", "//*[@index='2' and contains(@class, "
                                          "'android.widget.RelativeLayout')]").click()
        # 模拟器
        # self.driver.find_element("xpath","//*[@text='我的' and contains(@resource-id, "
        #                                   "'com.kachexiongdi.trucker:id/tv_tab_name')]").click()
        print("初始进入App的操作正常")
    except:
        print("初始进入App的操作异常")
