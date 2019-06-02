#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/16 16:52
# @Author  : Chris.Ma
from selenium import webdriver
import time

driver = webdriver.Chrome()
time.sleep(5)
driver.get("http://www.baidu.com")
time.sleep(5)
driver.find_element_by_id("kw").send_keys("测试环境")
time.sleep(5)
driver.find_element_by_id("su").click()
time.sleep(5)
driver.quit()