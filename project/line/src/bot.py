from flask import Flask, request, abort
# Linebot 核心程式庫
from linebot import LineBotApi, WebhookHandler
# 處理密鑰錯誤
from linebot.exceptions import InvalidSignatureError
# 接收並處理文字類型的訊息
from linebot.models import (MessageEvent, TextMessage, TextSendMessage, StickerMessage, StickerSendMessage, FollowEvent)
# 建立 Flask 物件
app=Flask(__name__)
# 頻道存取代碼 access token
line_bot_api=LineBotApi("yg3b2u5TiWN6aH6/sTXWNJsvL5i1iBkdgPN+udG/QWeSEm1yA72I+0xLPTNbR1yMqwYNvQqGPUHYl+G/bHZH93qjcncySCHHMA4Nn3BdN7lvp/lWnqcf6WJolQYzYZ8f3xGTENcAvdKXptoS00+d6AdB04t89/1O/w1cDnyilFU=")
# 頻道密鑰
handler=WebhookHandler("72a45476c1948125191ee64021375872")

# 使用者資料
users={}
# 接收使用者識別碼和姓名的兩個參數
def check_user(id, name):
    global users
    if id not in users: # 若使用者識別碼不在 users 字典之中
        users[id]={
            "name": name,
            "word": "",
            "save": False
        }
        print("新增一名用戶: ", id)
    else:
        print("用戶已經存在，id: ", id)
        print("目前用戶數: ", len(users))

# 儲存關鍵字
word=''
# 是否已儲存關鍵字，預設為否
save=False

# 接收回覆令牌、使用者識別碼和訊息文字參數
def reply_txt(token, id, txt):
    # 資料內容, 是否準備儲存
    global users
    # 如果收到的訊息文字內含 hi 你好
    if (txt=="hi") or (txt=="你好"):
        # 向使用者打招呼
        name=users[id]["name"]
        reply=f"{name}，你好"
    # 如果收到的訊息文字內含 secret (關鍵字)
    elif "secret" in txt: 
        if users[id]["word"] !='': # 如果有資料
            reply="Your secret: "+ users[id]["word"]
        else:
            reply="Please tell me your secret"
            users[id]["save"]=True # 準備儲存秘密
            print(users)
    elif users[id]["save"]:
        # 儲存收到的訊息
        key=users[id]["word"]=txt
        # 儲存完畢
        users[id]["save"]=False
        reply="Has saved"
    else:
        reply="Something may I help you?"
    # 儲存回應文字
    reply_txts=TextSendMessage(text=reply)
    # 儲存回應貼圖
    reply_stk=StickerSendMessage(
        package_id=11538,
        sticker_id=51626495
    )
    # 回覆訊息
    line_bot_api.reply_message(
        token, [reply_txts, reply_stk]
    )

# 建立路由

# 處理瀏覽首頁的請求
@app.route("/")
def index():
    return "Welcom to Line Bot!"

# 確認請求是 LINE 訊息伺服器的路由程式
@app.route("/callback", methods=["POST"])
def callback():
    # 取得 HTTP 標頭的密鑰欄位
    signature=request.headers["X-Line-Signature"]
    # 取得 HTTP 訊息本體並轉換為文字格式
    body=request.get_data(as_text=True)
    try:
        # 結合密鑰與訊息本體並驗證
        handler.handle(body, signature)
    except InvalidSignatureError:
        # 驗證失敗，回傳 400 錯誤代碼，中斷連結
        abort(400)
    return 'OK'

# 捕捉 LINE 訊息事件
@handler.default() # 接收任意 LINE 訊息的預設裝飾器
def default(event): # event: 接收訊息事件的參數
    print("捕捉到事件", event) # 輸出收到的訊息內容

# 新增接收文字事件
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 取得使用者唯一識別碼
    _id=event.source.user_id
    # 取得個人檔案
    profile=line_bot_api.get_profile(_id)
    # 紀錄使用者名稱
    _name=profile.display_name
    # 收到訊息文字
    txt=event.message.text
    
    # 儲存使用者資料
    check_user(_id, _name)
    # 回覆
    reply_txt(event.reply_token, _id, txt)
    
# 新增接收貼圖事件
@handler.add(MessageEvent, message=StickerMessage)
def handler_sticker_message(event):
    # 回應文字
    txt="還沒有辦法回應貼圖"
    # 儲存回應文字
    reply_txt=TextMessage(text=txt)
    # 儲存回應貼圖
    reply_stk=StickerSendMessage(
        package_id=446,
        sticker_id=1990
    )
    # 回應訊息
    line_bot_api.reply_message(
        event.reply_token, [reply_txt, reply_stk]
    )

# 處理被加入好友事件
@handler.add(FollowEvent)
def followed(event):
    # 取得使用者唯一識別碼
    _id=event.source.user_id
    # 取得個人檔案
    profile=line_bot_api.get_profile(_id)
    # 取得姓名
    _name=profile.display_name
    print("歡迎新好友ID: ", _id)
    print("名字: ", _name)
# 啟動 Flask
if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=80)