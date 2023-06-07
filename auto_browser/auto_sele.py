from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("detach", False)
# 建立 webdriver 物件，選擇 Chrome 瀏覽器
driver = webdriver.Chrome(options=options)
# 目標網址
url="https://jable.tv/models/aizawa-minami/"
# 給網頁 10 秒載入時間 (最久)
driver.implicitly_wait(10)
# 取得網址
driver.get(url)
# 連結欄位
searchbar=driver.find_elements(By.TAG_NAME, "a")
# 印出所有欄位
for i in searchbar:
    print(i.text)