# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: SnatchTheOrder.py
@time: 2021/10/3 20:28
"""

# -----------------------------------切换到货源页，进行抢单-----------------------------------------

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
# 切换到货源页
el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.view.View")
el1.click()
# 搜索货源专线7073
el2 = driver.find_element_by_id("com.kachexiongdi.trucker:id/et_content")
el2.click()
el2.send_keys("7073")
# 点击搜索按钮
el3 = driver.find_element_by_id("com.kachexiongdi.trucker:id/tv_search")
el3.click()
# 点击抢单按钮
el4 = driver.find_element_by_id("com.kachexiongdi.trucker:id/tv_grab_order")
el4.click()
# 点击确认车辆按钮
el5 = driver.find_element_by_id("com.kachexiongdi.trucker:id/btn_confirm")
el5.click()
# 点击核对货源信息确定按钮
el6 = driver.find_element_by_id("com.kachexiongdi.trucker:id/btn_dialog_confirm")
el6.click()
# 抢单成功，点击确认按钮
el7 = driver.find_element_by_id("com.kachexiongdi.trucker:id/btn_know")
el7.click()
# 跳转进入运单详情页，首次进入，引导页点击随意位置
el8 = driver.find_element_by_id("com.kachexiongdi.trucker:id/iv_guide")
el8.click()

driver.quit()

