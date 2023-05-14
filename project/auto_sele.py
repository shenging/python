from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("detach", True)
# 建立 webdriver 物件，選擇 Chrome 瀏覽器
driver = webdriver.Chrome(options=options)
# 目標網址
url="https://shopee.tw/"
# 給網頁 10 秒載入時間 (最久)
driver.implicitly_wait(10)
# 取得網址
driver.get(url)
# 搜尋欄位
searchbar=driver.find_element(By.XPATH, "//input[@class='shopee-searchbar-input__input']")
# 清空欄位
searchbar.clear()
# 在搜尋欄位上打關鍵字
searchbar.send_keys("手電筒")
# # 送出
searchbar.send_keys(Keys.RETURN)