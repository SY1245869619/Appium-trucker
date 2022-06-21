# encoding: utf-8
"""
@author: 沈缘
@contact: 1245869619@qq.com
@software: PyCharm
@file: Appium_Start.py
@time: 2022/6/13 20:33
"""
import subprocess
import time


def appium_start(host, port):
    '''
    启动appium server
    :param host:
    :param port:
    :return:
    '''
    # 指定bp端口号
    bootstrap_port = str(port + 1)
    # 把在cmd弹窗输入的命令，直接写到这里
    # cmd = 'start /b appium -a ' + host+' -p '+str(port) +' -bp '+ str(bootstrap_port)
    # 去掉 “/b”，即可以打开cmd弹窗运行
    cmd = 'start  appium -a ' + host + ' -p ' + str(port) + ' -bp ' + str(bootstrap_port)

    # 打印输入的cmd命令，及时间
    print("%s at %s " % (cmd, time.ctime()))

    subprocess.Popen(cmd, shell=True, stdout=open('./' + str(port) + '.log', 'a'), stderr=subprocess.STDOUT)


if __name__ == '__main__':
    host = '0.0.0.0'
    # 运行一个端口
    port = 4723
    appium_start(host, port)
    # 运行2个端口
