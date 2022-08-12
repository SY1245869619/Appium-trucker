#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Appium-trucker
@File    ：AppMyPage.py
@IDE     ：PyCharm
@Author  ：萌新小缘
@Date    ：2022/7/20 20:03
"""
import os
import time
from time import sleep

from appium.webdriver.common.appiumby import AppiumBy

from PublicAction import ActionPublic

# 截图
img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '//ScreenShots//'
Time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
screen_save_path = img_folder + Time + '我的页.png'


def AppMyPage(self):
    # 点击“我的”页
    # 真机
    self.driver.find_element("xpath", "//*[@index='2' and contains(@class, "
                                      "'android.widget.RelativeLayout')]").click()
    # 模拟器
    # self.driver.find_element("xpath", "//*[@text='我的' and contains(@resource-id, "
    #                                   "'com.kachexiongdi.trucker:id/tv_tab_name')]").click()
    sleep(1)
    # 点击认证状态栏，进入认证详情页
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/tv_no_auth").click()
    # 点击返回按钮
    self.driver.back()
    # 点击钱包栏，进入钱包页
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/tv_user_center_wallet").click()
    sleep(3)
    # 点击提现栏，进入提现页
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/item_withdrawal").click()
    sleep(3)
    # 点击返回按钮
    self.driver.back()
    # 点击银行卡栏，进入我的银行卡页
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/item_bankcard").click()
    # 点击返回按钮
    self.driver.back()
    # 点击账单按钮，进入账单页
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/tb_right_tv").click()
    # 点击返回按钮
    self.driver.back()
    sleep(1)
    # 点击运费记录的第一个，进入账单详情页
    self.driver.find_element("xpath", "//*[@index='0' and contains(@resource-id, "
                                      "'com.kachexiongdi.trucker:id/rl_item')]").click()
    # 点击返回按钮
    self.driver.back()
    # self.driver.find_element("xpath", "//*[@text='账单详情' and contains(@resource-id, "
    #                                   "'com.kachexiongdi.trucker:id/tb_center_title')]/../android.widget"
    #                                   ".ImageButton").click()
    # 点击返回按钮
    self.driver.back()
    # 点击我的车辆栏，进入车辆列表
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/tv_user_center_vehicle").click()
    # 点击一辆车，进入车辆详情页
    self.driver.find_element("xpath", "//*[@index='0' and contains(@resource-id, "
                                      "'com.kachexiongdi.trucker:id/tv_plate')]").click()
    # 点击返回按钮
    self.driver.back()
    sleep(1)
    # 点击返回按钮
    self.driver.keyevent(4)
    sleep(1)
    # 点击我的车队栏，进入我的车队页
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/rl_fleet").click()
    sleep(3)
    # 点击搜索框
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/et_content").click()
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/et_content").click()
    # 搜索框输入“沈”
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/et_content").send_keys("沈")
    # 点击搜索按钮
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/tv_search").click()
    # 点击“+”
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/tb_right_icon").click()
    # 点击加入车队按钮
    self.driver.find_element("xpath", "//*[@text='加入车队' and contains(@resource-id, "
                                      "'com.kachexiongdi.trucker:id/forum_menu_item')]").click()
    # 点击返回按钮
    self.driver.back()
    sleep(1)
    # 点击返回按钮
    self.driver.back()
    # 点击运费代收按钮
    self.driver.find_element("xpath", "//*[@text='运费代收' and contains(@class, "
                                      "'android.widget.TextView')]").click()
    sleep(3)
    # 点击返回按钮
    self.driver.back()
    # 点击意见反馈按钮
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/fl_item_opinion").click()
    # 点击返回按钮
    self.driver.back()
    # 点击在线客服按钮
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/fl_contactus").click()
    # 点击取消按钮
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/btn_dialog_cancel").click()
    # 滑动屏幕至设置按钮位置
    ActionPublic.swipe_up(self.driver)
    # 点击设置按钮
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/fl_setting").click()
    # 点击账户与安全按钮
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/tv_account_safe").click()
    # 点击修改支付密码按钮
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/revise_transfer_password").click()
    # 点击返回按钮
    self.driver.back()
    # 点击修改登录密码按钮
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/revise_login_password").click()
    # 点击返回按钮
    self.driver.back()
    sleep(1)
    # 点击返回按钮
    self.driver.back()
    # 点击关于我们按钮
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/tv_about_us").click()
    # 点击返回按钮
    self.driver.back()
    # 点击退出登录按钮
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/activity_settings_logout").click()
    # 点击取消按钮
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/btn_dialog_cancel").click()
    # 点击退出登录按钮
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/activity_settings_logout").click()
    # 点击确定退出按钮
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/btn_dialog_confirm").click()
