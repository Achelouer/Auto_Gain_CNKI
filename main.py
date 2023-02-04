#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import lxml
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
def get_m(urls):
    url = urls
    driver = webdriver.Edge()
    driver.get(url)
    temp = driver.page_source

    t_html = etree.HTML(temp)
    # print(temp)
    t_xpath = '//*[@id="abstract_text"]/@value'  # 摘要
    t_xpath2 = '//*[@class="keywords"]/a/text()'  # 关键词
    t = t_html.xpath(t_xpath)
    t2 = t_html.xpath(t_xpath2)
    print(t)
    print(t2)

driver = webdriver.Chrome()
driver.get('https://navi.cnki.net/knavi/journals/JSJX/detail?uniplatform=NZKPT')
#选择2022年第2期
year = 2021
num = '03'
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="'+str(year)+'_Year_Issue"]/dt/em').click()
driver.find_element(By.XPATH,'//*[@id="yq'+str(year)+num+'"]').click()
time.sleep(2)
#循环进入
web = driver.find_element(By.XPATH,'//*[@id="CataLogContent"]/div/div/dd[1]/span[1]/a')
time.sleep(1)
web.click()
get_m('https://kns.cnki.net/kcms2/article/abstract?v=a2v2doqF8jJihly_OvgbqBuaQYGwLNb4ephEFL_9bmW8ZPAO5ThkfwvUkFh660Me_tEeRKQuYy_FE1cppWn9N3vSQSIryB0Hk08ZtCa2uqVzHdgXCtz5Uu0nG26vAmuf&uniplatform=NZKPT')
time.sleep(3)
url = driver.page_source
#print(url)
temp_html = etree.HTML(url)
temp_xpath = '//*[@id="CataLogContent"]/div/div/dd/span/a/@href'
temp = temp_html.xpath(temp_xpath)
for i in temp:
    ############写入xlml操作
    print(i)
