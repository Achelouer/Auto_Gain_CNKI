#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
利用xlml获取信息
'''
from lxml import etree
from selenium import webdriver

url = 'https://kns.cnki.net/kcms2/article/abstract?v=a2v2doqF8jK-Cu4AK0s8texwkg8tP6L98BAqHlaI0StsnbZ_Ktf82jdx0I5g1qDNW8AF7AudtADX0i0Irmo_lWzgy7odXBK2j670ly-tHU2_IxBejYqqI0otSTXGs0xA&uniplatform=NZKPT'

driver = webdriver.Edge()
driver.get(url)
temp = driver.page_source

t_html=etree.HTML(temp)
#print(temp)
t_xpath = '//*[@id="abstract_text"]/@value'#摘要
t_xpath2 = '/html/body/div[2]/div[1]/div[3]/div/div/div[5]/p'#关键词
t = t_html.xpath(t_xpath)
t2 = t_html.xpath(t_xpath2)
print(t)
for i in t2:
    print(i)