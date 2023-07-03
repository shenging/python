from datetime import datetime
from dateutil import tz
from flask import Flask, render_template
# 操作資料庫
from flask_sqlalchemy import SQLAlchemy
# 處理用戶資料
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import re
# 宣告 Flask 物件
app=Flask(__name__)
# ------設定資料庫檔案路徑與其他參數------
# 資料庫檔案路徑存放於網站根目錄
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///bbs.db"
# 關閉追蹤修改
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
# 登入使用者程式所需要的密鑰
app.config["SECRET_KEY"]=b'\xd7\xaa\xa2\x07uFh\xbf\x06\xbbe\xea\x84\xb2\xef!$f\x04\x1f-\xc8\x14\x8d'
# 建立資料庫物件
db=SQLAlchemy(app)
# 建立儲存留言的資料表類別
class Guestbook(db.Model):
    # 留言編號，設置為主鍵
    id=db.Column(db.Integer, primary_key=True)
    # 留言者名子，必填
    name=db.Column(db.String(30), nullable=False)
    # 電子郵件，不能重複，必填
    email=db.Column(db.String(50), unique=True, nullable=False)
    # 留言內容，必填
    message=db.Column(db.Text, nullable=False)
    # 圖示名稱 必填，預設圖片
    icon=db.Column(db.String(10), nullable=False, default="S__58974268.jpg")
    # 留言的日期與時間，必填，預設為留言時間
    post_date=db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    # 把物件資料用字串格式呈現
    def __repr__(self):
        result="name: {}, email: {}, post_date: {}".format(self.name, self.email, self.post_date)
        return result
# 建立儲存留言版網站管理人員的資料表
class User(UserMixin, db.Model):
    # 使用者編號，主鍵
    id=db.Column(db.Integer, primary_key=True)
    # 姓名，必填
    name=db.Column(db.String(30), nullable=False)
    # 加密後的密碼
    pwd_hash=db.Column(db.String(80), nullable=False)
    # 電子郵件，唯一，必填
    email=db.Column(db.String(50), unique=True, nullable=False)
    # 是否為管理員，必填，預設為 False
    is_admin=db.Column(db.Boolean, nullable=False, default=False)
    @property # 將方法轉為屬性
    def password(self):
        # 若讀取該屬性，顯示「屬性錯誤」例外
        raise AttributeError("無法讀取 password 屬性")
    @password.setter # 將方法轉成「設定屬性值」
    def password(self, password):
        # 用安全雜湊演算處理輸入的密碼
        self.pwd_hash=generate_password_hash(password, "sha256")
    # 驗證密碼，通過驗證傳回 True
    def verity_password(self, password):
        return check_password_hash(self.pwd_hash, password)
    def __repr__(self):
        return f"name: {self.name}, email: {self.email}"

@app.template_filter() # 樣板引擎過濾器
def datetimefilter(utc): # 轉換與格式化日期時間
    utc_zone=tz.gettz("UTC") # 基準時間
    tw_zone=tz.gettz("Asia/Taipei") # 轉換目標時區為台北
    utc=utc.replace(tzinfo=utc_zone) # 將基準時間設定成 UTC 標準
    tw_time=utc.astimezone(tw_zone) # 將日期時間轉換成台灣時區
    return tw_time.strftime("%Y/%m/%d %H:%M") # 回傳喚成字串格式的日期

# 搜尋字串中的 \r\n, \n, \r
paragraph_re=re.compile(r"(?:\r\n|\r|\n){2, }")
# @app.template_filter()
# @evalcontextfilter
# def nl2br(eval_ctx, value):

login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view="admin"
@login_manager.user_loader # 透過此函式判定用戶的身分
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/admin")
def admin():
    return render_template("login.html")
@app.route("/login", methods=["POST"])
def login():
    email=User.request.form["email"]
if __name__=="__main__":
    app.run(debug=True)