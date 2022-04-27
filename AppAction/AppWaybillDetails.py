# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: AppWaybillDetails.py
@time: 2022/4/27 17:35
"""
from time import sleep


# App运单详情页操作集合
def AppWaybillDetails(self):
    # 点击抢单按钮
    self.driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
        ".widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout"
        "/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup"
        "/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.TextView").click()
    sleep(2)
    # 选择车辆点击确认车辆
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/btn_confirm").click()
    # 核对订单弹窗点击取消按钮
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/btn_dialog_cancel").click()
    # 再次点击抢单按钮
    self.driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
        ".widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout"
        "/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup"
        "/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.TextView").click()
    sleep(2)
    # 选择车辆点击确认车辆
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/btn_confirm").click()
    # 核对订单弹窗点击确认按钮
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/btn_dialog_confirm").click()
    # 抢单成功提醒弹窗点击我知道了
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/btn_know").click()
    sleep(1)
    # 上传磅单引导图点击任意位置
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/iv_guide").click()
    sleep(2)
    # 点击返回按钮
    self.driver.find_element_by_xpath("//*[@text='运单详情' and contains(@class, "
                                      "'android.widget.TextView')]/../android.view.ViewGroup").click()
    # 点击返回按钮
    self.driver.find_element_by_xpath("//*[@text='货源详情' and contains(@class, "
                                      "'android.widget.TextView')]/../android.view.ViewGroup").click()
    sleep(2)
