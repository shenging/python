# 密碼產生器
import json
print("歡迎使用密碼產生器~")
def write_file(name, account, password): # 寫入資料
    # 讀取檔案
    with open ("data.json", mode="r", encoding="utf-8") as file:
        data=file.read()
        if data=="": # 若沒資料
            data={
                name:{
                    "帳號": account,
                    "密碼": password
            }
            }
        else: # 若沒重複
            data=json.loads(data)
            add_name={
                "帳號": account,
                "密碼": password
            }
            data[name]=add_name
        with open ("data.json", mode="w", encoding="utf-8") as file:
                data=json.dumps(data, indent=4, ensure_ascii=False)
                file.write(data)
                return ("新增成功!")
def search_file(name): # 查詢資料
    with open ("data.json", mode="r", encoding="utf-8") as file:
        # 讀取檔案
        data=file.read()
        if data=="": # 若沒資料
            return None
        else: # 若有資料
            # 將 json 資料轉為 python 格式
            data=json.loads(data)
            # 取得 python dict 裡面的鍵值
            keys=data.keys()
            # 將鍵值轉換為 list
            keys=list(keys)
            # 運用 if in 檢查每一個鍵
            if name in keys: # 若有和查詢值相同的鍵值
                return data # 回傳 python 格式資料 (dict)
            # 沒有的話回傳 None
            else:
                return None
# 選擇的功能
while True:
    user_selection=input("請問要使用什麼功能? (r 查詢, a 新增, q 離開): ")
    if user_selection=="r": # 查詢
        name=input("請輸入名稱: ")
        result=search_file(name)
        # 找到相符合的資料
        if result!=None:
            account=result[name]["帳號"]
            password=result[name]["密碼"]
            print(f"帳號: {account}")
            print(f"密碼: {password}")
        else:
            print("查無資料")
    elif user_selection=="a": # 新增
        name=input("請輸入名稱: ")
        result=search_file(name)
        # 有重複的資料
        if result!=None:
            print("已經有此名稱了")
        else:
            account=input("請輸入帳號: ")
            password=input("請輸入密碼: ")
            # 沒資料、沒有重複的
            add_data=write_file(name, account, password)
            print(add_data)
    elif user_selection=="q":
        print("離開")
        break