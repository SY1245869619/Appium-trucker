# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: AppWaybillDetails.py
@time: 2022/4/27 17:35
"""
from time import sleep

from appium.webdriver.common.touch_action import TouchAction

from PublicAction import ActionPublic

# App运单详情页操作集合
def AppWaybillDetails(self):
    sleep(2)
    # 向上滑动
    ActionPublic.swipe_up(self.driver)
    # TouchAction(self.driver).press(x=589, y=1836).move_to(x=600, y=1268).release().perform()
    # 勾选货物运输协议
    self.driver.find_element_by_xpath("//*[@index='24' and contains(@class, "
                                      "'android.widget.ImageView')]").click()
    # 点击抢单按钮
    self.driver.find_element_by_accessibility_id("抢单").click()
    sleep(6)
    # 选择车辆点击确认车辆
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/btn_confirm").click()
    # 核对订单弹窗点击取消按钮
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/btn_dialog_cancel").click()
    # 再次点击抢单按钮
    self.driver.find_element_by_accessibility_id("抢单").click()
    sleep(6)
    # 选择车辆点击确认车辆
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/btn_confirm").click()
    # 核对弹窗勾选协议
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/checkbox").click()
    # 核对订单弹窗点击确认按钮
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/btn_dialog_confirm").click()
    # 抢单成功提醒弹窗点击我知道了
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/btn_know").click()
    sleep(1)
    # 上传磅单引导图点击任意位置
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/iv_guide").click()
    sleep(2)
    # 点击返回按钮
    # 调用系统自带返回按钮
    self.driver.keyevent('4')
    # self.driver.find_element_by_xpath("//*[@text='运单详情' and contains(@class, "
    #                                   "'android.widget.TextView')]/../android.view.ViewGroup").click()
    # 点击返回按钮
    # 调用系统自带返回按钮
    self.driver.keyevent('4')
    # self.driver.find_element_by_xpath("//*[@text='货源详情' and contains(@class, "
    #                                   "'android.widget.TextView')]/../android.view.ViewGroup").click()
    sleep(2)
