# 引入 flask 裡的 Flask
from flask import Flask, render_template
# --------------------------建立 Flask 物件----------------------------------
app=Flask(__name__) # 參數: 應用程式的名子
app.debug=True
# -----------------------------設置路由--------------------------------------
# -----------------首頁------------------
@app.route("/")
@app.route("/index.html")
def index():
    return app.send_static_file("index.html")
# ---------------關於使用者---------------
@app.route("/about/<user>/")
def about(user):
    return render_template("index.html", name=user)
# ---------------成績發表-----------------
@app.route("/test/<int:score>/")
def test(score):
    return render_template("score.html", score=score)
# -----------------訂單------------------
@app.route("/order/")
def order():
    return render_template("order.html")
# -----------------------------啟動伺服器------------------------------------
if __name__=="__main__":
    app.run("0.0.0.0", 80)