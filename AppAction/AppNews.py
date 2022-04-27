# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: AppNews.py
@time: 2022/4/26 18:19
"""
from time import sleep

# App的消息功能操作集合
def AppNews(self):
    # 点击货源页
    # 真机
    self.driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
        ".widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout"
        "/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
        ".LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout").click()
    # # 模拟器
    # self.driver.find_element_by_xpath("//*[@text='货源' and contains(@resource-id, "
    #                                   "'com.kachexiongdi.trucker:id/tv_tab_name')]").click()
    sleep(2)
    # 点击消息按钮
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/iv_toolbar_msg").click()
    sleep(3)
    # 点击运单消息
    self.driver.find_element_by_xpath("//*[@text='运单消息' and contains(@resource-id, "
                                      "'com.kachexiongdi.trucker:id/tv_my_news')]").click()
    # 点击第一个运单消息
    self.driver.find_element_by_xpath("//*[@index='0' and contains(@resource-id, "
                                      "'com.kachexiongdi.trucker:id/rl_status')]").click()
    sleep(1)
    # 点击返回按钮
    self.driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
        ".widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view"
        ".View/android.widget.Button").click()

    # 点击设置按钮
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/tb_right_tv").click()
    # 点击第一个按钮，关闭所有此类消息开关
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/off_newmsg").click()
    # 点击第一个按钮，打开第一个开关
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/off_newmsg").click()
    # 点击第二个按钮，打开第二个开关
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/off_push_notification").click()
    # 点击返回按钮，返回至运单消息页
    self.driver.find_element_by_xpath("//*[@text='消息设置' and contains(@resource-id, "
                                      "'com.kachexiongdi.trucker:id/tb_center_title')]/../android.widget"
                                      ".ImageButton").click()
    # 点击返回按钮，通过找到他的兄弟元素，再定位到他
    self.driver.find_element_by_xpath("//*[@text='运单消息' and contains(@resource-id, "
                                      "'com.kachexiongdi.trucker:id/tb_center_title')]/../android.widget"
                                      ".ImageButton").click()
    # 点击我的钱包
    self.driver.find_element_by_xpath("//*[@text='我的钱包' and contains(@resource-id, "
                                      "'com.kachexiongdi.trucker:id/tv_my_news')]").click()
    # 点击返回按钮，通过找到他的兄弟元素，再定位到他
    self.driver.find_element_by_xpath("//*[@text='我的钱包' and contains(@resource-id, "
                                      "'com.kachexiongdi.trucker:id/tb_center_title')]/../android.widget"
                                      ".ImageButton").click()
    # 点击货源消息
    self.driver.find_element_by_xpath("//*[@text='货源消息' and contains(@resource-id, "
                                      "'com.kachexiongdi.trucker:id/tv_my_news')]").click()
    # 点击返回按钮，通过找到他的兄弟元素，再定位到他
    self.driver.find_element_by_xpath("//*[@text='货源消息' and contains(@resource-id, "
                                      "'com.kachexiongdi.trucker:id/tb_center_title')]/../android.widget"
                                      ".ImageButton").click()
    # 点击系统消息
    self.driver.find_element_by_xpath("//*[@text='系统消息' and contains(@resource-id, "
                                      "'com.kachexiongdi.trucker:id/tv_my_news')]").click()
    # 点击返回按钮，通过找到他的兄弟元素，再定位到他
    self.driver.find_element_by_xpath("//*[@text='系统消息' and contains(@resource-id, "
                                      "'com.kachexiongdi.trucker:id/tb_center_title')]/../android.widget"
                                      ".ImageButton").click()
    # 点击车队消息
    self.driver.find_element_by_xpath("//*[@text='车队消息' and contains(@resource-id, "
                                      "'com.kachexiongdi.trucker:id/tv_my_news')]").click()
    # 点击返回按钮，通过找到他的兄弟元素，再定位到他
    self.driver.find_element_by_xpath("//*[@text='车队消息' and contains(@resource-id, "
                                      "'com.kachexiongdi.trucker:id/tb_center_title')]/../android.widget"
                                      ".ImageButton").click()
    # 点击返回按钮，通过找到他的兄弟元素，再定位到他
    self.driver.find_element_by_xpath("//*[@text='消息' and contains(@resource-id, "
                                      "'com.kachexiongdi.trucker:id/tb_center_title')]/../android.widget"
                                      ".ImageButton").click()
