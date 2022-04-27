# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: PasswordLogin.py
@time: 2021/10/3 20:15
"""
# --------------------------------------密码登录-----------------------------------------------

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "fxwl"
caps["app"] = "E:\\文件\\Appiumtest\\dailyTrucker-1.5.55-117-debug.apk"
caps["autoGrantPermissions"] = True
caps["ensureWebviewsHavePages"] = True
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

# 增加隐式等待
driver.implicitly_wait(10)
# 登录由验证码登录切换为密码登录
el1 = driver.find_element_by_id("com.kachexiongdi.trucker:id/tv_password_login")
el1.click()
# 输入手机号
el2 = driver.find_element_by_id("com.kachexiongdi.trucker:id/et_phone")
el2.click()
el2.send_keys("13171521557")
# 输入密码
el3 = driver.find_element_by_id("com.kachexiongdi.trucker:id/et_verify_code")
el3.click()
el3.send_keys("cs123456")
# 点击登录
el4 = driver.find_element_by_id("com.kachexiongdi.trucker:id/btn_login")
el4.click()

driver.quit()