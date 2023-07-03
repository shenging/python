from flask import Flask, request, make_response, render_template
# 建立 Flask 物件
app=Flask(__name__)
app.debug=True
# 設置路由
@app.route("/")
def index():
    response=request.cookies.get("user")
    if not response: # 沒東西的話
        # 建立回應物件
        res=make_response("設定 Cookie...")
        # 寫入 Cookie
        res.set_cookie("user", "Maker", max_age=60*3)
    else:
        res=f"{response}你好啊"
    return res
# 啟動
if __name__=="__main__":
    app.run("0.0.0.0", 80)