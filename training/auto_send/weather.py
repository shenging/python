import requests
# base_url
BASE_URL="https://opendata.cwb.gov.tw/api"
# api
api="/v1/rest/datastore/F-C0032-001"
# url
url=BASE_URL+api
# 參數
parameters={
    # 會員授權碼
    "Authorization": "CWB-22C608E5-0E47-4C82-A5A9-1B69B5EBA337",
    # 地方
    "locationName": "新北市",
    # 天氣因子
    "elementName": "PoP"
}
# 發送請求
weather_data=requests.get(url, parameters)
# 解析為 json 取得新北市最近的降雨機率
time_data=weather_data.json()["records"]["location"][0]["weatherElement"][0]["time"]
result=time_data[-1]["parameter"]["parameterName"]
print(result)