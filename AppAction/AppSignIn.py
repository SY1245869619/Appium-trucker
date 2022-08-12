# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: AppSignIn.py
@time: 2022/4/26 18:13
"""
from time import sleep

# App的登录操作集合
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.core import driver


def AppSignIn(self):
    # 点击“登录/注册”按钮
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/user_center_enter").click()
    sleep(1)
    try:
        assert len(self.driver.find_elements("id", "com.android.permissioncontroller:id/permission_allow_button")) == 1
        # 协议弹窗点击同意
        self.driver.find_element("id", "com.android.permissioncontroller:id/permission_allow_button").click()
        print("\n存在权限弹窗，点击允许\n")
    except AssertionError:
        print("不存在权限弹窗\n")
    # 点击手机号输入框
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/et_phone").click()
    # 输入手机号
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/et_phone").send_keys("13171521557")
    # 点击获取验证码按钮
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/tv_send_vericode").click()
    # 点击验证码输入框
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/et_verify_code").click()
    # 输入验证码
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/et_verify_code").send_keys("123456")
    # 取消勾选协议
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/rb_auth_rule").click()
    # 点击登录注册按钮
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/btn_login").click()
    # 再次点击同意勾选协议
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/rb_auth_rule").click()
    sleep(2)
    # 点击登录注册按钮
    self.driver.find_element("id", "com.kachexiongdi.trucker:id/btn_login").click()
    # 显示等待5秒
    wait = WebDriverWait(driver, 5)
    # 动态页面，toast的定位
    num = wait.until(lambda _: self.driver.find_element(AppiumBy.XPATH, '//android.widget.Toast').text)
    print("toast提示为："+num)
    sleep(2)
