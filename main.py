# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。

def temp():
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    import time
    driver = webdriver.Edge()
    driver.get("https://navi.cnki.net/knavi/journals/JSJX/detail?uniplatform=NZKPT")
    driver.set_window_rect(450, 300, 32, 50)
    elem = driver.find_element(By.CSS_SELECTOR, "#CataLogContent > div > div > dd:nth-child(2) > span.name > a")
    if elem:

        elem.click()
    else:
        print("我不存在")

    driver.quit()


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
