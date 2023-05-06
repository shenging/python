# 乒乓球遊戲
import pygame
import ball
import paddle
import text
import random
# 初始化 pygame
pygame.init()
RANDOM_LIST=(-2, -1.5, 1.5, 2)
STEEL_BLUE="#4682B4"
ALICE_BLUE="#F0F8FF"
CHAETREUSE="#7FFF00"
AMETHYST="#6633CC"
WIDTH=700
HEIGHT=500
# 創建視窗
window=pygame.display.set_mode((WIDTH, HEIGHT))
# 更改視窗名子
pygame.display.set_caption("乒乓球")
# 創建文字
text_size=50
text_left=text.Text("game\微軟正黑體.ttf", text_size, 0, True, CHAETREUSE)
text_right=text.Text("game\微軟正黑體.ttf", text_size, 0, True, CHAETREUSE)
# 創建球
ball1=ball.Ball(350, 250, 7, random.choice(RANDOM_LIST), random.choice(RANDOM_LIST))
# 創建球拍
paddle_width=15
paddle_height=100
paddle_left=paddle.Paddle(10, (HEIGHT-100)/2, paddle_width, paddle_height, 2)
paddle_right=paddle.Paddle(WIDTH-15-10, (HEIGHT-100)/2, paddle_width, paddle_height, 2)
# 遊戲評分
def game():
    # 取得球體的左右方
    ball1_left=[int(ball1.x-ball1.radius), int(ball1.y)] # 球體左方
    ball1_right=[int(ball1.x+ball1.radius), int(ball1.y)] # 球體右方
    # 取得左球拍的座標(靠近球那面)
    paddle_left_localx=paddle_left.x+paddle_width # x 座標(整面都一樣)
    paddle_left_localy=[] # y 座標(整面很多)
    paddle_left.y=int(paddle_left.y) # 將浮點數轉換成整數
    for i in range(paddle_left.y, paddle_left.y+paddle_height+1): # 那面所有的 y 座標
        local=[paddle_left_localx, i]
        paddle_left_localy.append(local) # 存入 paddle_left_localy
    if ball1_left in paddle_left_localy: # 有碰到的話
        ball1.speedx*=-1
    elif ball1_left[0]<=0: # 沒擋到的話
        ball1.x=350
        ball1.y=250
        ball1.speedx=random.choice(RANDOM_LIST)
        ball1.speedy=random.choice(RANDOM_LIST)
        text_right.content+=1
    # 取得右球拍的座標(靠近球那面)
    paddle_right_localx=paddle_right.x # x 座標(整面都一樣)
    paddle_right_localy=[] # y 座標(整面很多)
    paddle_right.y=int(paddle_right.y) # 將浮點數轉換成整數
    for i in range(paddle_right.y, paddle_right.y+paddle_height+1): # 那面所有的 y 座標
        local=[paddle_right_localx, i]
        paddle_right_localy.append(local) # 存入 paddle_right_localy
    if ball1_right in paddle_right_localy: # 有碰到的話
        ball1.speedx*=-1
    elif ball1_right[0]>=700: # 沒擋到的話
        ball1.x=350
        ball1.y=250
        ball1.speedx=random.choice(RANDOM_LIST)
        ball1.speedy=random.choice(RANDOM_LIST)
        text_left.content+=1
# 創建時鐘，統一時間 (每個人電腦效能不同，統一時間才能一樣)
time=pygame.time.Clock()
run=True
while run: # 不斷的偵測事件
    # 限制迴圈一秒跑幾次 (統一)
    time.tick(300)
    # 取得輸入
    # 逐一偵測所有的事件
    for event in pygame.event.get():
        # 如果事件的類型是點擊關閉視窗按鍵
        if event.type==pygame.QUIT:
            # 結束迴圈，關閉視窗
            run=False
    # 遊戲更新
    ball1.update()
    paddle_left.update(HEIGHT, pygame.K_w, pygame.K_s)
    paddle_right.update(HEIGHT, pygame.K_o, pygame.K_l)
    game()
    # 畫面顯示
    # 視窗填滿色彩
    window.fill(STEEL_BLUE)
    # 顯示文字
    window.blit(text_left.render(), (100, 0))
    window.blit(text_right.render(), (WIDTH-100-(text_size/2), 0))
    # 畫上球
    ball1.draw(window, ALICE_BLUE)
    # 畫上球拍
    paddle_left.draw(window, AMETHYST)
    paddle_right.draw(window, AMETHYST)
    # 更新畫面
    pygame.display.update()
# 結束 pygame
pygame.quit()