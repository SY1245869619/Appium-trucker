# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: demo.py
@time: 2021/9/13 16:58
"""
# 司机端用例执行demo
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

# 属性配置
caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "fxwl"
caps["app"] = "E:\\文件\\Appiumtest\\dailyTrucker-1.5.55-117-debug.apk"
caps["autoGrantPermissions"] = True
caps["ensureWebviewsHavePages"] = True
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
# 增加隐式等待
driver.implicitly_wait(10)

# 协议弹窗点击同意
el1 = driver.find_element_by_id("com.kachexiongdi.trucker:id/btn_dialog_confirm")
el1.click()
# 启动图滑动2次
TouchAction(driver).press(x=1058, y=1079).move_to(x=154, y=1066).release().perform()
TouchAction(driver).press(x=1028, y=1058).move_to(x=176, y=1058).release().perform()
# 点击立即体验按钮
# TouchAction(self.driver).tap(x=630, y=1822).perform()
el2 = driver.find_element_by_id("com.kachexiongdi.trucker:id/b_enter")
el2.click()
# 增加隐式等待
driver.implicitly_wait(10)
# 点击“我的”
el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                   "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                   ".widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                   ".LinearLayout/android.widget.RelativeLayout/android.widget"
                                   ".FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout"
                                   "/android.widget.RelativeLayout["
                                   "3]/android.widget.LinearLayout/android.view.View")
el3.click()
# 点击“登录/注册”按钮
el4 = driver.find_element_by_id("com.kachexiongdi.trucker:id/user_center_enter")
el4.click()

driver.quit()
