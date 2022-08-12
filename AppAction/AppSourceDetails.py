# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: AppSourceDetails.py
@time: 2022/4/27 17:35
"""
import os
import time
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from PublicAction import ActionPublic

# 截图
img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '//ScreenShots//'
Time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
screen_save_path = img_folder + Time


# App货源详情页操作集合
def AppSourceDetails(self):
    sleep(1)
    # 向上滑动
    ActionPublic.swipe_up(self.driver)
    # 勾选货物运输协议
    self.driver.find_element("xpath", "//*[@index='24' and contains(@class, "
                                      "'android.widget.ImageView')]").click()
    sleep(2)
    # 点击抢单按钮
    self.driver.find_element("xpath", "//android.view.View[@content-desc='抢单']").click()
    sleep(1)
    # 判断是否存在轨迹和司机定位提醒弹窗
    try:
        assert len(
            self.driver.find_elements("id", "com.kachexiongdi.trucker:id/btn_know")) == 1
        # 截图
        self.driver.get_screenshot_as_file(screen_save_path + '轨迹和司机定位提醒弹窗.png')
        self.driver.find_element("id",
                                 "com.kachexiongdi.trucker:id/btn_know").click()  # 协议弹窗点击同意
        print("\n存在轨迹和司机定位提醒弹窗，点击知道了\n")
    except AssertionError:
        print("不存在轨迹和司机定位提醒弹窗\n")
    sleep(3)
    # 选择车辆点击确认车辆
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/btn_confirm").click()
    # 核对订单弹窗点击取消按钮
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/btn_dialog_cancel").click()
    # 再次点击抢单按钮
    self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="抢单").screenshot(screen_save_path + '详情页抢单按钮.png')
    self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="抢单").click()
    sleep(1)
    # 判断是否存在轨迹和司机定位提醒弹窗
    try:
        assert len(
            self.driver.find_elements("id", "com.kachexiongdi.trucker:id/btn_know")) == 1
        self.driver.find_element("id",
                                 "com.kachexiongdi.trucker:id/btn_know").click()  # 协议弹窗点击同意
        print("\n存在轨迹和司机定位提醒弹窗，点击知道了\n")
    except AssertionError:
        print("不存在轨迹和司机定位提醒弹窗\n")
    sleep(3)
    # 选择车辆点击确认车辆
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/btn_confirm").click()
    # 核对弹窗勾选协议
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/checkbox").click()
    # 核对订单弹窗点击确认按钮
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/btn_dialog_confirm").click()
    # 抢单成功提醒弹窗点击我知道了
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/btn_know").click()
    sleep(1)
    # 上传磅单引导图点击任意位置
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/iv_guide").click()
    sleep(2)
    # 点击返回按钮
    # 调用系统自带返回按钮
    self.driver.back()
    # 点击返回按钮
    # 调用系统自带返回按钮
    self.driver.back()
    sleep(2)
