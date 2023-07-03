# 計算時間差的模組
from datetime import timedelta
from flask import (Flask, redirect, render_template, request, session, url_for)
# 建立 Flask 物件
app=Flask(__name__)
app.debug=True
# 設定密鑰
app.config["SECRET_KEY"]=b'ij\xbecT\xac\x07\xf1\x14\tG\xf8pk\x9e~6|\xca\xeb\xd5e\x14W'
# 設定 session 有效時間參數
app.config["PERMANENT_SESSION_LIFETIME"]=timedelta(minutes=3)
# 設置路由
# 首頁
@app.route("/")
def index():
    if session.get("user"):
        usr=session["user"]
        return f"歡迎回來啊，{usr}\
            <br><a href='/logout'>登出</a>"
    return "路人你好"
# 登入
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method=="POST":
        # 儲存 session
        session["user"]=request.form["user"]
        # 保留 session
        session.permanent=True
        return redirect(url_for("index"))
    return render_template("login_session.html")
# 登出
@app.route("/logout")
def logout():
    # 刪除 ssesion 裡的 "user" 資料
    session.pop("user", None)
    return redirect(url_for("index"))
if __name__=="__main__":
    app.run("0.0.0.0", 80)