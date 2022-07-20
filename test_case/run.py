# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: run.py
@time: 2022/5/14 0:18
"""
import os
import time
import pytest


def run_main():
    # 测试用例文件路径——参考具体项目路径
    test_case = r'test_trucker_process.py'
    # html报告命名
    name_html = time.strftime('%Y_%m_%d_%H', time.localtime(time.time())) + '.html'
    # html报告输出路径——参考具体项目路径
    report_path = os.path.join(r'Resources\Appium-trucker\test_case', name_html)
    # 通过python代码执行pytest命令行方式
    pytest.main(['-v', '--html={}'.format(report_path), '--self-contained-html', test_case])


if __name__ == "__main__":
    run_main()  # 可执行输出报告操作