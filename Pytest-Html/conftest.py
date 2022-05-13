# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: conftest.py
@time: 2022/5/14 0:14
"""
import pytest
from py.xml import html


def pytest_configure(config):  # 修改Environment展示信息
    # 添加项目名称
    config._metadata["项目名称"] = "HTML封装测试"
    # 删除JAVA_HOME
    config._metadata.pop("JAVA_HOME")
    # 删除Plugins
    config._metadata.pop("Plugins")


def pytest_html_results_summary(prefix):
    # Summary部分在此设置
    prefix.extend([html.p("测试组：沈缘")])


def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))  # 表头添加Description
    cells.pop()  # 删除link


def pytest_html_results_table_row(report, cells):
    if hasattr(report, 'description'):  # 判断对象是否包含对应的属性
        cells.insert(1, html.td(report.description))  # 表头对应的内容
        cells.pop()
    else:
        print("!!!", report.longreprtext)


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):  # description取值为用例说明'''doc'''
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
