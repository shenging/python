import requests
# base url
base="https://opendata.cwb.gov.tw/api"
# api
api="/v1/rest/datastore/F-C0032-001"
# url
url=base+api
# 參數
params={
    "Authorization": "CWB-22C608E5-0E47-4C82-A5A9-1B69B5EBA337",
    "locationName": "宜蘭縣",
    "elementName": "PoP",
    "sort": "time"
}
# 發送請求
response=requests.get(url, params)
# 請求內容
content=response.json()
print(content["records"]["location"][0]["weatherElement"][0]["time"])
