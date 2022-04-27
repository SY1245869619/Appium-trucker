# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: test.py
@time: 2021/10/5 23:24
"""

# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: test_demo_pytest.py
@time: 2021/10/4 21:18
"""
import datetime

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "fxwl"
        caps["app"] = "E:\\文件\\Appiumtest\\dailyTrucker-1.5.55-117-debug.apk"
        caps["autoGrantPermissions"] = True
        caps["ensureWebviewsHavePages"] = True
        # 可以输入中文的配置
        caps["unicodeKeyboard"] = True
        caps['noReset'] = True  # 需要设置的就是这个参数
        caps["appPackage"] = "com.kachexiongdi.trucker"
        caps["appWaitActivity"] = "com.kachexiongdi.trucker/com.kachesiji.module_login.ui.activities.LoginActivity"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 增加隐式等待
        self.driver.implicitly_wait(10)

    def test_demo(self):
        # 增加隐式等待
        self.driver.implicitly_wait(10)
        # 登录由验证码登录切换为密码登录
        el1 = self.driver.find_element_by_id("com.kachexiongdi.trucker:id/tv_password_login")
        el1.click()
        # 输入手机号
        el2 = self.driver.find_element_by_id("com.kachexiongdi.trucker:id/et_phone")
        el2.click()
        el2.send_keys("13171521557")
        # 输入密码
        el3 = self.driver.find_element_by_id("com.kachexiongdi.trucker:id/et_verify_code")
        el3.click()
        el3.send_keys("cs123456")
        # 点击登录
        el4 = self.driver.find_element_by_id("com.kachexiongdi.trucker:id/btn_login")
        el4.click()

        self.driver.quit()
        assert len(self.driver.find_elements_by_xpath('//*[@text="Edit"]')) ==1
        assert "这个文本是否存在" in self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
    def teardown(self):
        self.driver.quit()
