'''
此示例项目使用selenium无头浏览器查询12306车票信息，并将结果保存到result.txt文件中
使用edge浏览器及其对应版本的驱动，需要给驱动配置系统环境变量
selenium是第三方库
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

#输入起始站和终点站
from_ = input('from')
to_ = input('to')

def click_button(driver, type, value):# 自动点击按钮
    try:
        #根据type和value确定元素定位器
        if type.lower() == 'id':
            element_locator = (By.ID, value)
        elif type.lower() == 'class_name':
            element_locator = (By.CLASS_NAME, value)
        elif type.lower() == 'xpath':
            element_locator = (By.XPATH, value)
        else:
            raise ValueError("Unsupported element locator type. Use 'id', 'class_name' or 'xpath'.")
        # 等待元素可点击
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(element_locator))
        # 查找并点击元素
        element = driver.find_element(*element_locator)#解包元素定位器并查找元素
        ActionChains(driver).click(element).perform()#执行点击操作
    except Exception as e:
        print('异常:', '\n',e)

def input_text(driver, type, value, text):# 自动输入文本
    try:
        #根据type和value确定元素定位器
        if type.lower() == 'id':
            element_locator = (By.ID, value)
        elif type.lower() == 'class_name':
            element_locator = (By.CLASS_NAME, value)
        elif type.lower() == 'xpath':
            element_locator = (By.XPATH, value)
        else:
            raise ValueError("Unsupported element locator type. Use 'id', 'class_name' or 'xpath'.")
        # 等待元素可输入
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(element_locator))
        # 查找并输入文本
        element = driver.find_element(*element_locator)
        element.clear()#清空文本框中已存在的信息
        element.send_keys(text)#输入text的内容
        element.send_keys(Keys.ENTER)#按回车键
    except Exception as e:
        print('异常:', '\n',e)

#启动浏览器并根据输入的数据查询
driver = webdriver.Edge()
driver.get('https://kyfw.12306.cn/index/')
input_text(driver, 'id', 'fromStationText', from_)
input_text(driver, 'id', 'toStationText', to_)
click_button(driver, 'id', 'search_one')

driver.switch_to.window(driver.window_handles[-1])#切换到新打开的页面
print(driver.current_url)#打印新页面url

#等待页面加载完成并查找对应元素
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'queryLeftTable')))

#第一次保存爬取到的结果
with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(element.text)

driver.quit()#退出浏览器

#对结果整理
l = ['C','G','D','Z','T','K','Y']
with open('result.txt', 'r+', encoding='utf-8') as file:
    lines = file.readlines()
    file.seek(0)  # 将文件指针移动到文件开头
    file.truncate()  # 清空文件内容
    new_file = ''
    for line in lines:
        if line[0] in l:
            new_file += '\n' + line.rstrip()
        else:
            new_file += line[:-1]#切片掉最后一个换行符
    file.write(new_file[1:])#去掉开头的换行符并写入文件

print('Done.')