# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: test_trucker_process.py
@time: 2021/10/6 22:02
"""
import pytest
from time import sleep
from appium import webdriver
from PublicAction import Appium_Start
from AppAction import GetIntoApp, AppSignIn, AppNews, AppSourceList, AppWaybillDetails


class TestDemo:
    Appium_Start.appium_start('0.0.0.0', 4723)

    def setup_class(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "fxwl"
        caps["app"] = "C:\\Users\\SHENYUAN\\Desktop\\trucker-daily5.1.5.apk"
        caps["autoGrantPermissions"] = True
        # caps["ensureWebviewsHavePages"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 增加隐式等待
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        self.driver.quit()

    # 初始进入app的操作集测试用例
    def test_GetIntoApp(self):
        GetIntoApp.GetIntoApp(self)

    # App登录功能的操作集测试用例
    def test_AppSignIn(self):
        AppSignIn.AppSignIn(self)

    # App消息功能的操作集测试用例
    def test_AppNews(self):
        AppNews.AppNews(self)

    # App货源列表的操作集测试用例
    def test_AppSourceList(self):
        AppSourceList.AppSourceList(self)

    # App运单详情页操作集测试用例
    def test_AppWaybillDetails(self):
        AppWaybillDetails.AppWaybillDetails(self)

    def test_demo1(self):
        # 切换到运单页
        # 真机
        self.driver.find_element("xpath", "//*[@index='1' and contains(@class, "
                                          "'android.widget.RelativeLayout')]").click()
        # 进入运单详情页
        self.driver.find_element("xpath", "//*[@text='待装货' and contains(@resource-id, "
                                          "'com.kachexiongdi.trucker:id/tv_order_status')]").click()
        # self.driver.find_element("xpath",
        #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
        #     ".widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout"
        #     "/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android"
        #     ".widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget"
        #     ".LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget"
        #     ".RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget"
        #     ".LinearLayout[1]").click()
        # 点击过磅二维码按钮
        self.driver.find_element("accessibility_id", "过磅二维码").click()
        sleep(2)
        # self.driver.find_element("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
        #                                   ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
        #                                   "/android.widget.LinearLayout/android.widget.LinearLayout/android.widget"
        #                                   ".FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android"
        #                                   ".view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup["
        #                                   "1]/android.widget.TextView").click()
        # 点击返回按钮
        # 调用系统自带返回按钮
        self.driver.keyevent(4)
        # self.driver.find_element("xpath","//*[@text='过磅二维码' and contains(@resource-id, "
        #                                   "'com.kachexiongdi.trucker:id/tb_center_title')]/../android.widget"
        #                                   ".ImageButton").click()
        # 点击取消运单
        self.driver.find_element("accessibility_id", "取消运单").click()
        # self.driver.find_element("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
        #                                   ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
        #                                   "/android.widget.LinearLayout/android.widget.LinearLayout/android.widget"
        #                                   ".FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android"
        #                                   ".view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView["
        #                                   "2]").click()
        # 点击确定按钮
        self.driver.find_element("accessibility_id", "确认").click()
        # self.driver.find_element("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
        #                                   ".widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup"
        #                                   "/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup"
        #                                   "/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView["
        #                                   "3]").click()
        # 模拟器
        # self.driver.find_element("xpath","//*[@text='运单' and contains(@resource-id, "
        #                                   "'com.kachexiongdi.trucker:id/tv_tab_name')]").click()
        # 点击企业名称输入框
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/et_content").click()
        # 输入企业名称信息
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/et_content").send_keys("北京测试")
        # 点击搜索按钮
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/tv_search").click()
        # 点击清空输入框信息按钮
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/iv_clear").click()
        # 点击运输中tab
        self.driver.find_element("xpath", "//*[@text='运输中' and contains(@class, "
                                          "'android.widget.TextView')]").click()
        # 点击结算中tab
        self.driver.find_element("xpath", "//*[@text='结算中' and contains(@class, "
                                          "'android.widget.TextView')]").click()
        # 点击已完成tab
        self.driver.find_element("xpath", "//*[@text='已完成' and contains(@class, "
                                          "'android.widget.TextView')]").click()
        # 进入运单详情页
        self.driver.find_element("xpath", "//*[@index='0' and contains(@class, "
                                          "'android.widget.LinearLayout')]").click()
        sleep(3)
        # 点击返回按钮
        # 调用系统自带返回按钮
        self.driver.keyevent(4)
        # self.driver.find_element("xpath",
        #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
        #     ".widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout"
        #     "/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup"
        #     "/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView").click()
        # self.driver.find_element("xpath","//*[@text='运单详情' and contains(@class, "
        #                                   "'android.widget.TextView')]/../android.widget"
        #                                   ".ImageButton").click()
        # 点击“我的”页
        # 真机
        self.driver.find_element("xpath", "//*[@index='2' and contains(@class, "
                                          "'android.widget.RelativeLayout')]").click()
        # self.driver.find_element("xpath",
        #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
        #     ".widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout"
        #     "/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
        #     ".LinearLayout/android.widget.RelativeLayout[3]/android.widget.LinearLayout").click()
        # 模拟器
        # self.driver.find_element("xpath","//*[@text='我的' and contains(@resource-id, "
        #                                   "'com.kachexiongdi.trucker:id/tv_tab_name')]").click()
        # 点击认证状态栏，进入认证详情页
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/tv_no_auth").click()
        # 点击返回按钮
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/iv_left_back").click()
        # 点击钱包栏，进入钱包页
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/tv_user_center_wallet").click()
        sleep(3)
        # 点击提现栏，进入提现页
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/item_withdrawal").click()
        # 点击返回按钮
        # 调用系统自带返回按钮
        self.driver.keyevent(4)
        # self.driver.find_element("xpath","//*[@text='提现' and contains(@resource-id, "
        #                                   "'com.kachexiongdi.trucker:id/tb_center_title')]/../android.widget"
        #                                   ".ImageButton").click()
        # self.driver.find_element("xpath",
        #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
        #     ".widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout"
        #     "/android.widget.FrameLayout/android.widget.RelativeLayout["
        #     "2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view"
        #     ".ViewGroup/android.widget.ImageButton").click()
        # 点击银行卡栏，进入我的银行卡页
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/item_bankcard").click()
        # 点击返回按钮
        # 调用系统自带返回按钮
        self.driver.keyevent(4)
        # self.driver.find_element("xpath","//*[@text='我的银行卡' and contains(@resource-id, "
        #                                   "'com.kachexiongdi.trucker:id/tb_center_title')]/../android.widget"
        #                                   ".ImageButton").click()
        # self.driver.find_element("xpath",
        #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
        #     ".widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout"
        #     "/android.widget.FrameLayout/android.widget.RelativeLayout["
        #     "2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view"
        #     ".ViewGroup/android.widget.ImageButton").click()
        # 点击账单按钮，进入账单页
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/tb_right_tv").click()
        # 点击返回按钮
        # 调用系统自带返回按钮
        self.driver.keyevent(4)
        # self.driver.find_element("xpath","//*[@text='我的账单' and contains(@resource-id, "
        #                                   "'com.kachexiongdi.trucker:id/tb_center_title')]/../android.widget"
        #                                   ".ImageButton").click()
        # self.driver.find_element("xpath",
        #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
        #     ".widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout"
        #     "/android.widget.FrameLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout["
        #     "1]/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget"
        #     ".ImageButton").click()
        # 点击运费记录的第一个，进入账单详情页
        self.driver.find_element("xpath",
                                 "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                                 ".widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout"
                                 "/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view"
                                 ".ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout["
                                 "2]/android.widget.RelativeLayout").click()
        # 点击返回按钮
        self.driver.find_element("xpath", "//*[@text='账单详情' and contains(@resource-id, "
                                          "'com.kachexiongdi.trucker:id/tb_center_title')]/../android.widget"
                                          ".ImageButton").click()
        # 点击返回按钮
        self.driver.find_element("xpath", "//*[@text='我的钱包' and contains(@resource-id, "
                                          "'com.kachexiongdi.trucker:id/tb_center_title')]/../android.widget"
                                          ".ImageButton").click()
        # 点击我的车辆栏，进入车辆列表
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/tv_user_center_vehicle").click()
        # 点击一辆车，进入车辆详情页
        self.driver.find_element("xpath",
                                 "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                                 ".widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout["
                                 "2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx"
                                 ".recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.RelativeLayout").click()
        # 点击返回按钮
        self.driver.find_element("xpath", "//*[@text='车辆信息' and contains(@resource-id, "
                                          "'com.kachexiongdi.trucker:id/tb_center_title')]/../android.widget"
                                          ".ImageButton").click()
        # 点击返回按钮
        self.driver.find_element("xpath", "//*[@text='我的车辆' and contains(@resource-id, "
                                          "'com.kachexiongdi.trucker:id/tb_center_title')]/../android.widget"
                                          ".ImageButton").click()
        # 点击我的车队栏，进入我的车队页
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/rl_fleet").click()
        sleep(3)
        # 点击搜索框
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/et_content").click()
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/et_content").click()
        # 搜索框输入“沈”
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/et_content").send_keys("沈")
        # 点击搜索按钮
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/tv_search").click()
        # 点击“+”
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/tb_right_icon").click()
        # 点击加入车队按钮
        self.driver.find_element("xpath", "//*[@text='加入车队' and contains(@resource-id, "
                                          "'com.kachexiongdi.trucker:id/forum_menu_item')]").click()
        # 点击返回按钮
        self.driver.find_element("xpath", "//*[@text='加入车队' and contains(@resource-id, "
                                          "'com.kachexiongdi.trucker:id/tb_center_title')]/../android.widget"
                                          ".ImageButton").click()
        # self.driver.find_element("xpath",
        #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
        #     ".widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout["
        #     "1]/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget"
        #     ".ImageButton").click()
        # 点击返回按钮
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/iv_left_back").click()
        # 点击运费代收按钮
        self.driver.find_element("xpath", "//*[@text='运费代收' and contains(@class, "
                                          "'android.widget.TextView')]").click()
        # self.driver.find_element("xpath",
        #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
        #     ".widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout"
        #     "/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android"
        #     ".widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget"
        #     ".RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout["
        #     "5]/android.widget.TextView[2]").click()
        sleep(3)
        # 点击返回按钮
        self.driver.find_element("xpath",
                                 "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                                 ".widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout["
                                 "1]/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget"
                                 ".ImageButton").click()
        # 点击意见反馈按钮
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/fl_item_opinion").click()
        # 点击返回按钮
        self.driver.find_element("xpath",
                                 "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                                 ".widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout["
                                 "1]/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget"
                                 ".ImageButton").click()
        # 点击在线客服按钮
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/fl_contactus").click()
        # 点击取消按钮
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/btn_dialog_cancel").click()
        # 滑动屏幕至设置按钮位置
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("设置").'
                                                        'instance(0));')
        # 点击设置按钮
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/fl_setting").click()
        # 点击账户与安全按钮
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/tv_account_safe").click()
        # 点击修改支付密码按钮
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/revise_transfer_password").click()
        # 点击返回按钮
        self.driver.find_element("xpath", "//*[@text='修改支付密码' and contains(@resource-id, "
                                          "'com.kachexiongdi.trucker:id/tb_center_title')]/../android.widget"
                                          ".ImageButton").click()
        # 点击修改登录密码按钮
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/revise_login_password").click()
        # 点击返回按钮
        self.driver.find_element("xpath", "//*[@text='修改登录密码' and contains(@resource-id, "
                                          "'com.kachexiongdi.trucker:id/tb_center_title')]/../android.widget"
                                          ".ImageButton").click()
        # 点击返回按钮
        self.driver.find_element("xpath", "//*[@text='账户与安全' and contains(@resource-id, "
                                          "'com.kachexiongdi.trucker:id/tb_center_title')]/../android.widget"
                                          ".ImageButton").click()
        # 点击关于我们按钮
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/tv_about_us").click()
        # 点击返回按钮
        self.driver.find_element("xpath", "//*[@text='关于我们' and contains(@resource-id, "
                                          "'com.kachexiongdi.trucker:id/tb_center_title')]/../android.widget"
                                          ".ImageButton").click()
        # 点击退出登录按钮
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/activity_settings_logout").click()
        # 点击取消按钮
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/btn_dialog_cancel").click()
        # 点击退出登录按钮
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/activity_settings_logout").click()
        # 点击确定退出按钮
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/btn_dialog_confirm").click()
        # 点击注册/登录按钮
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/ll_user_center_auth_status").click()
        # 切换为密码登录
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/tv_password_login").click()
        # 点击手机号输入框
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/et_phone").click()
        # 输入手机号
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/et_phone").send_keys("13171521557")
        # 点击密码输入框
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/et_verify_code").click()
        # 输入密码
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/et_verify_code").send_keys("cs123456")
        # 点击登录按钮
        self.driver.find_element("id", "com.kachexiongdi.trucker:id/btn_login").click()
        sleep(5)
