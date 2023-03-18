'''
url:链接
year:年份
num:月份
'''
import time
import lxml
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from configparser import ConfigParser   # Python2中是from ConfigParser import ConfigParser
def get_m(urls,sort):
    url = urls
    driver = webdriver.Edge()
    driver.get(url)
    temp = driver.page_source
    t_html = etree.HTML(temp)
    # print(temp) #调试可打印此数据看页面是否加载
    _xpath = '//*[@class="wx-tit"]/h1/text()'
    t_xpath = '//*[@id="abstract_text"]/@value'  # 摘要
    t_xpath2 = '//*[@class="keywords"]/a/text()'  # 关键词
    t_xpath3 = '(//*[@class="top-space"])[last()]/p/text()' #分类号 /html/body/div[2]/div[1]/div[3]/div/div/div[7]/ul/li[3]/p/text()
    t_xpath4 = '//*[@class="author"]/span/a/text()'  # 作者
    t_xpath42 = '//*[@class="author"]/span/text()'  # 作者
    t_xpath4_1 = '//*[@class="author"]/span/a/sup/text()' #作者标号
    t_xpath5 = '//*[@class="wx-tit"]/h3[2]/descendant::*/text()'  # 单位-->引入查取下级
    title = t_html.xpath(_xpath)
    t = t_html.xpath(t_xpath)
    t2 = t_html.xpath(t_xpath2)
    t3 = t_html.xpath(t_xpath3)
    t4 = t_html.xpath(t_xpath4)
    t42 = t_html.xpath(t_xpath42)
    t4_1 = t_html.xpath(t_xpath4_1)
    t5 = t_html.xpath(t_xpath5)
    driver.close()
    with open('message.txt', 'a', encoding='utf-8') as f:
        if title[0]:
            f.write('标题：'+title[0]+'\n')
        if t4:
            f.write('作者：')
            j = 0
            for i in t4:
                f.write(i+' ')  # 去除后面格式
                if len(t4_1)>0:
                    f.write(t4_1[j]+'')
                if len(t42)>0:
                    f.write(t42[j]+'')
                j = j+1
            f.write('\n')
        if t5:
            f.write('单位：')
            for i in t5:
                f.write(i+' ')  # 去除后面格式
            f.write('\n')
        f.write('摘要：'+t[0] + '\n')
        f.write('关键字：')
        for i in t2:
            f.write(i[:-23])#去除后面格式
        f.write('\n')
        f.write('分类号：')
        for i in t3:
            f.write(i)#去除后面格式
        f.write('\n')

        f.write('\n')
        f.close()
    print(title[0]) #标题
    print(t3)  #


#ini 获取信息


conf = ConfigParser()  # 需要实例化一个ConfigParser对象
conf.read('set.ini')  # 需要添加上config.ini的路径，不需要open打开，直接给文件路径就读取，也可以指定encoding='utf-8'
urls = conf['user']['url']
year = conf['user']['year']
num = conf['user']['num']
sort = conf['mess']['sort']
f_time = int(conf['time']['f_time'])#首页加载时间

driver = webdriver.Edge()
driver.get(urls)
#选择2022年第2期


time.sleep(f_time)

driver.find_element(By.XPATH,'//*[@id="'+str(year)+'_Year_Issue"]/dt/em').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="yq'+str(year)+str(num)+'"]').click()
time.sleep(2)

#获取文件列表
url = driver.page_source
#print(url)
temp_html = etree.HTML(url)
temp_xpath = '//*[@id="CataLogContent"]/div/div/dd/span/a/@href'
temp = temp_html.xpath(temp_xpath)
for i in temp:
    # 循环进入
    web = driver.find_element(By.XPATH, '//*[@id="CataLogContent"]/div/div/dd[1]/span[1]/a')
    time.sleep(1)
    web.click()

    get_m(i,sort)



