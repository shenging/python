# 密碼產生器 GUI 介面
import PIL
from PIL import ImageTk, Image
import tkinter
from tkinter import messagebox
import json
def clear(): # 清空欄位
    name_entry.delete(0, tkinter.END)
    account_entry.delete(0, tkinter.END)
    password_entry.delete(0, tkinter.END)
def search_file(name): # 查詢資料
    try:
        with open ("data.json", mode="r", encoding="utf-8") as file:
            # 讀取檔案
            data=file.read()
    except:
        with open ("data.json", mode="w", encoding="utf-8") as file:
            file.write("")
    else:
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
def read_file(): # 讀取檔案
    try:
        # 取得名子的輸入
        name=name_entry.get()
        # 查詢檔案
        result=search_file(name)
        if name=="": # 若名子欄位輸入為空
            raise ValueError("搜尋不得為空")
    except ValueError:
        messagebox.showerror(title="錯誤", message="搜尋不得為空")
    except FileNotFoundError: # 若檔案尚未建立或遺失
        with open ("data.json", mode="w", encoding="utf-8") as file:
            messagebox.showerror(title="提示", message="查無資料")
            clear()
    else:
        # 查到資料
        if result!=None:
            account=result[name]["帳號"]
            password=result[name]["密碼"]
            data=f"帳號: {account}\n密碼: {password}"
            messagebox.showinfo(title="帳號資訊", message=data)
            # 清空所有欄位
            clear()
        else: # 查不到資料
            messagebox.showerror(title="提示", message="查無資料")
            clear()
def write_file(): # 寫入資料
    # 取得名子的輸入
    name=name_entry.get()
    # 取得帳號的輸入
    account=account_entry.get()
    # 取得密碼的輸入
    password=password_entry.get()
    # 若有一欄位為空
    if name=="" or account=="" or password=="":
        messagebox.showwarning(title="錯誤", message="輸入不可為空")
        # 清空所有欄位
        clear()
    else:
        # 查詢資料
        result=search_file(name)
        # 有重複的資料
        if result!=None:
            messagebox.showwarning(title="錯誤", message="已有此名稱")
            # 清空所有欄位
            clear()
        else:
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
                        messagebox.showinfo(title="提示", message="新增成功")
                        # 清空欄位
                        clear()

# 建立視窗物件
window=tkinter.Tk()
# 視窗標題
window.title("密碼產生器")
# 視窗大小
window.geometry("400x420")
window.resizable(False, False)
# 視窗設定
window.config(padx=50, pady=10)

# 開啟圖片
img=Image.open("lock.png")
# 轉換為 Tk 物件
tk_img=ImageTk.PhotoImage(img)
# 建立畫布
canvas=tkinter.Canvas(width=224, height=225)
# 將圖片物件畫上畫布
canvas.create_image(112, 112.5, image=tk_img)
# 建立文字
name=tkinter.Label(text="帳號名稱", font=("標楷體", 14))
account=tkinter.Label(text="帳號", font=("標楷體", 14))
password=tkinter.Label(text="密碼", font=("標楷體", 14))
# 建立輸入框
name_entry=tkinter.Entry(width=20, font=("標楷體", 14))
account_entry=tkinter.Entry(width=20, font=("標楷體", 14))
password_entry=tkinter.Entry(width=20, font=("標楷體", 14))
# 建立按鈕
add_button=tkinter.Button(text="新增", font=("標楷體", 14), bg="blue",fg="white", width=29, command=write_file)
search_button=tkinter.Button(text="搜尋", font=("標楷體", 14), bg="black",fg="white", width=29, command=read_file)
# 顯示畫布
canvas.grid(row=0, column=0, columnspan=2)
#顯示文字
name.grid(row=1, column=0)
account.grid(row=2, column=0, pady=5)
password.grid(row=3, column=0)
# 顯示輸入框
name_entry.grid(row=1, column=1)
account_entry.grid(row=2, column=1, pady=5)
password_entry.grid(row=3, column=1)
# 顯示按鈕
search_button.grid(row=4, column=0, columnspan=2, pady=5)
add_button.grid(row=5, column=0, columnspan=2)
window.mainloop()