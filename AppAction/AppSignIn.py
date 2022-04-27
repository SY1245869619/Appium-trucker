# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: AppSignIn.py
@time: 2022/4/26 18:13
"""
from time import sleep


# App的登录
def AppSignIn(self):
    # 点击“登录/注册”按钮
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/user_center_enter").click()
    # 点击手机号输入框
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/et_phone").click()
    # 输入手机号
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/et_phone").send_keys("13171521557")
    # 点击获取验证码按钮
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/tv_send_vericode").click()
    # 点击验证码输入框
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/et_verify_code").click()
    # 输入验证码
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/et_verify_code").send_keys("123456")
    # 取消勾选协议
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/rb_auth_rule").click()
    # 点击登录注册按钮
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/btn_login").click()
    # 再次点击同意勾选协议
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/rb_auth_rule").click()
    sleep(1)
    # 点击登录注册按钮
    self.driver.find_element_by_id("com.kachexiongdi.trucker:id/btn_login").click()
    sleep(2)
