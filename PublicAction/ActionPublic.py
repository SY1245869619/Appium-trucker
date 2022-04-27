# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: ActionPublic.py
@time: 2022/4/26 17:40
"""


# 封装滑动操作
# 向上滑动
def swipe_up(driver, t=500, n=1):
    u = driver.get_window_size()
    x1 = u['width'] * 0.5  # x坐标
    y1 = u['height'] * 0.75  # 起点y坐标
    y2 = u['height'] * 0.25  # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)


# 向下滑动
def swipe_down(driver, t=500, n=1):
    d = driver.get_window_size()
    x1 = d['width'] * 0.5
    y1 = d['height'] * 0.25
    y2 = d['height'] * 0.75
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)


# 向左滑动
def swipe_left(driver, t=500, n=1):
    l = driver.get_window_size()
    x1 = l['width'] * 0.75
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.25
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)


# 向右滑动
def swipe_right(driver, t=500, n=1):
    r = driver.get_window_size()
    x1 = r['width'] * 0.25
    y1 = r['height'] * 0.5
    x2 = r['width'] * 0.75
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)
