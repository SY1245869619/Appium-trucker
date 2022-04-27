# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: GetIntoApp.py
@time: 2022/4/26 17:36
"""

from PublicAction import ActionPublic


# 初始进入App的操作集合
def GetIntoApp(self):
    self.driver.implicitly_wait(5)
    try:
        assert len(self.driver.find_elements_by_id("com.android.systemui:id/notification_allow")) == 1
        self.driver.find_element_by_id("com.android.systemui:id/notification_allow").click()  # 协议弹窗点击同意
        print("\n存在权限弹窗，点击允许\n")
    except AssertionError:
        print("不存在权限弹窗\n")
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/btn_dialog_confirm").click()
    # 启动图滑动2次
    ActionPublic.swipe_left(self.driver)
    ActionPublic.swipe_left(self.driver)
    # TouchAction(self.driver).press(x=1058, y=1079).move_to(x=154, y=1066).release().perform()
    # TouchAction(self.driver).press(x=1028, y=1058).move_to(x=176, y=1058).release().perform()
    try:
        assert len(self.driver.find_elements_by_id("com.kachexiongdi.trucker:id/b_enter")) == 1
        print("存在立即体验按钮，测试通过\n")
    except AssertionError:
        print("测试不通过\n")
    # 点击立即体验按钮
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/b_enter").click()
    # 点击“我的”
    # 真机
    self.driver.find_element_by_xpath("//*[@index='2' and contains(@class, "
                                      "'android.widget.RelativeLayout')]").click()
    # 模拟器
    # self.driver.find_element_by_xpath("//*[@text='我的' and contains(@resource-id, "
    #                                   "'com.kachexiongdi.trucker:id/tv_tab_name')]").click()
