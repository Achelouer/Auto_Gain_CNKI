from configparser import ConfigParser   # Python2中是from ConfigParser import ConfigParser

conf = ConfigParser()  # 需要实例化一个ConfigParser对象
conf.read('../set.ini')  # 需要添加上config.ini的路径，不需要open打开，直接给文件路径就读取，也可以指定encoding='utf-8'
url = conf['user']['url']
year = conf['user']['year']
num = conf['user']['num']
print(year)