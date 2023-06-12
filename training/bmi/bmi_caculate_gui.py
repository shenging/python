# tkinter GUI BMI 計算機
import tkinter
import tkinter.font
import tkinter.messagebox
# 建立視窗物件
window=tkinter.Tk()
# 視窗標題
window.title("BMI 計算機")
# 視窗大小
window.geometry("300x250")
# 視窗設定
window.config(padx=30, pady=30)
# 按鈕點擊後
def click():
    try:
        # 取得 height.entry 輸入框的資料
        h_data=float(height_entry.get())
        # 取得 weight.entry 輸入框的資料
        w_data=float(weight_entry.get())
        if h_data<0 or w_data<0:
            raise ValueError("不能輸入負數")
        # 結果顯示在 result
        result["text"]=round(w_data/((h_data/100)**2), 1)
    except:
        tkinter.messagebox.showerror(title="錯誤", message="輸入錯誤")
        
# 建立文字
height=tkinter.Label(text="身高", font=("標楷體", 14))
weight=tkinter.Label(text="體重", font=("標楷體", 14))
cm=tkinter.Label(text="公分", font=("標楷體", 14))
kg=tkinter.Label(text="公斤", font=("標楷體", 14))
bmi=tkinter.Label(text="您的BMI: ", font=("標楷體", 14))
result=tkinter.Label(text=0, font=("標楷體", 14))
# 文字顯示
height.grid(row=0, column=0, )
weight.grid(row=1, column=0, pady=5)
cm.grid(row=0, column=2)
kg.grid(row=1, column=2)
bmi.grid(row=2, column=0)
result.grid(row=2, column=1)
# 建立按鈕
caculate=tkinter.Button(text="計算", font=("標楷體", 14), command=click)
# 按鈕顯示
caculate.grid(row=3, column=1)
# 建立輸入框
height_entry=tkinter.Entry(width=7, font=("標楷體", 14))
weight_entry=tkinter.Entry(width=7, font=("標楷體", 14))
# 輸入框顯示
height_entry.grid(row=0, column=1)
weight_entry.grid(row=1, column=1)
# 所有字體
# all_word=tkinter.font.families()
# print(all_word)
# # 文字顯示位置
# hello.pack(side="left")
# 建立無窮迴圈，讓視窗物件不斷偵測動作
window.mainloop()