# 引入 flask 裡的 Flask
from flask import Flask
# --------------------------建立 Flask 物件----------------------------------
app=Flask(__name__) # 參數: 應用程式的名子
app.debug=True
# -----------------------------設置路由--------------------------------------
# def index():
#     return "welcome to here!"
# app.add_url_rule("/", "index", index)
# 和下面裝飾器寫法相同
@app.route("/")
@app.route("/index.html")
def index():
    return "首頁"
@app.route("/about")
def about():
    return "關於我們"
@app.route("/faq/")
def faq():
    return "問答集"
# -----------------------------啟動伺服器-----------------------------------
if __name__=="__main__":
    app.run()