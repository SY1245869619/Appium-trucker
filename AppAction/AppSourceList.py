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
    # 勾选常跑路线
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/rb_often_run_route").click()
    # 勾选车队单
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/rb_orientation").click()
    # 点击排序按钮
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/tv_sort").click()
    # 点击距我最近按钮
    self.driver.find_element_by_xpath("//*[@text='距我最近' and contains(@resource-id, "
                                      "'com.kachexiongdi.trucker:id/tv_item_title')]").click()
    sleep(1)
    # 再次点击排序按钮
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/tv_sort").click()
    # 点击价格最高按钮
    self.driver.find_element_by_xpath("//*[@text='价格最高' and contains(@resource-id, "
                                      "'com.kachexiongdi.trucker:id/tv_item_title')]").click()
    sleep(1)
    # 点击第一个货源，会进入货源详情页
    self.driver.find_element_by_xpath(
        '//*[@resource-id="com.kachexiongdi.trucker:id/tv_company" and @index="0"]').click()
    sleep(3)

