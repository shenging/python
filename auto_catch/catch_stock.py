import requests
import time
import schedule
import pandas
# base url
BASE_URL="https://openapi.twse.com.tw/v1"
# api
api="/exchangeReport/STOCK_DAY_ALL"
# url
url=BASE_URL+api
# 取得最新資料
def news_data(url):
    # 發送請求
    data=requests.get(url)
    # 解析為 json 格式
    json_data=data.json()
    # 建立 DataFrame
    result=pandas.DataFrame(json_data)
    # 本地時間
    now_time=time.localtime()
    # 檔名
    file_name=f"{now_time.tm_year}-{now_time.tm_mon}-{now_time.tm_mday} {now_time.tm_hour}-{now_time.tm_min}-{now_time.tm_sec}"
    # 輸出 csv 檔案
    result.to_csv(f"auto_catch/{file_name}.csv", encoding="utf_8_sig", index=False)
    print(f"{file_name} 取得股票資訊")
# 每過 5 秒取得最新資料
schedule.every(5).seconds.do(news_data, url)
while True:
    # 檢查是否有待辦排程
    schedule.run_pending()
    # 每 5 秒檢查一次
    time.sleep(5)
    