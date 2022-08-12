#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Appium-trucker
@File    ：AppWaybill.py
@IDE     ：PyCharm
@Author  ：萌新小缘
@Date    ：2022/7/20 19:46
"""
from time import sleep

from appium.webdriver.common.appiumby import AppiumBy


def AppWaybill(self):
    # 切换到运单页
    # 真机
    self.driver.find_element("xpath", "//*[@index='1' and contains(@class, "
                                      "'android.widget.RelativeLayout')]").click()
    # 进入运单详情页
    self.driver.find_element("xpath", "//*[@text='待装货' and contains(@resource-id, "
                                      "'com.kachexiongdi.trucker:id/tv_order_status')]").click()
    # 点击过磅二维码按钮
    self.driver.find_element("xpath", "//android.view.View[@content-desc='过磅二维码']").click()
    # 点击返回按钮
    # 调用系统自带返回按钮
    sleep(1)
    self.driver.back()
    # self.driver.keyevent(4)
    sleep(2)
    # 点击取消运单
    self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=" 取消运单").click()
    sleep(1)
    # 点击确定按钮
    self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="确认").click()
    # 点击企业名称输入框
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/et_content").click()
    # 输入企业名称信息
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/et_content").send_keys("北京测试")
    # 点击搜索按钮
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/tv_search").click()
    # 点击清空输入框信息按钮
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/iv_clear").click()
    # 点击运输中tab
    self.driver.find_element("xpath", "//*[@text='运输中' and contains(@class, "
                                      "'android.widget.TextView')]").click()
    # 点击结算中tab
    self.driver.find_element("xpath", "//*[@text='结算中' and contains(@class, "
                                      "'android.widget.TextView')]").click()
    # 点击已完成tab
    self.driver.find_element("xpath", "//*[@text='已完成' and contains(@class, "
                                      "'android.widget.TextView')]").click()
    # # 进入运单详情页
    # self.driver.find_element("xpath", "//*[@index='0' and contains(@class, "
    #                                   "'android.widget.LinearLayout')]").click()
    sleep(3)
    # 点击返回按钮
    # 调用系统自带返回按钮
    # self.driver.keyevent(4)
