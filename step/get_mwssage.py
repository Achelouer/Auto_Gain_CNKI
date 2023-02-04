from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://kns.cnki.net/kcms2/article/abstract?v=j14_WWxyq7KYcH7UDKkX_WxSgQep6w9WbP7rkMifScsBBx-J8ytRbtFXVZLyqganCFApgJNzx5BFo4fnPEjvLK82f13Wla4AIPdz0opd2No49fsx2RxKGg==&uniplatform=NZKPT"
driver = webdriver.Edge()
driver.get(url)
driver.set_window_rect(450,300,32,50)


# driver.quit() #关闭页面
