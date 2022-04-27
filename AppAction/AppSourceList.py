# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: AppSourceList.py
@time: 2022/4/27 17:13
"""
from time import sleep

# App货源列表的操作集合
def AppSourceList(self):
    # 点击联系客服按钮
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/iv_toolbar_customer").click()
    # 点击取消按钮
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/btn_dialog_cancel").click()
    # 点击发布企业/专线号搜索框
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/et_content").click()
    # 输入发布企业信息
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/et_content").send_keys("北京测试")
    # 点击搜索按钮
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/tv_search").click()
    # 点击第一个货源，会进入货源详情页
    self.driver.find_element_by_xpath(
        '//*[@resource-id="com.kachexiongdi.trucker:id/tv_company" and @index="0"]').click()
    sleep(3)

