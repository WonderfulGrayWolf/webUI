# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver
import allure
# 作者-上海悠悠 QQ交流群:717225969
# blog地址 https://www.cnblogs.com/yoyoketang/


def test_login():
    with allure.step("step1：打开登录首页"):
        print('one')
    with allure.step("step2：输入账号：admin"):
        print('two')
    with allure.step("step2：输入密码：123456"):
       print('three')
    # 故意断言失败，看是否会截图
    assert 1==2