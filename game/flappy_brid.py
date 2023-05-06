import pygame
from ground import Ground
from bird import Bird
from pipe import Pipe
import random
import text
# 初始化 pygame
pygame.init()
#-------------------常數-----------------------
# 視窗寬度
SCREEN_WIDTH=780
# 視窗高度
SCREEN_HEIGHT=600
# 遊戲偵數
FPS=60
#-----------------遊戲狀態---------------------
# 遊戲輸了
game_over=False
# 通過的管子數量
pass_pipe=0
#-------------------文字格式-----------------------
# 文字顏色
CHAETREUSE="#7FFF00"
# 文字大小
text_size=50
# 創建文字
game_score=text.Text("game/微軟正黑體.ttf", text_size, pass_pipe, True, CHAETREUSE)
#-------------------視窗設定-----------------------
# 創建視窗
window=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# 視窗名子
pygame.display.set_caption("可愛的鳥鳥")
# 背景
background_image=pygame.image.load("image/bg.png")
# 調整視窗
background_image=pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
#-------------------重新開始-------------------------
# 載入圖片
restart_image=pygame.image.load("image/restart.png")
#---------------------鳥鳥-----------------------------
# 鳥鳥1
brid1_image=pygame.image.load("image/bird1.png")
# 鳥鳥2
brid2_image=pygame.image.load("image/bird2.png")
# 鳥鳥3
brid3_image=pygame.image.load("image/bird3.png")
# 所有的鳥鳥
brid_image=[brid1_image, brid2_image, brid3_image]
# 創建鳥鳥
brid_image_x=300
brid_image_y=300
brid=Bird(brid_image, brid_image_x, brid_image_y, game_over)
# 創建鳥鳥群組
brid_group=pygame.sprite.Group()
# 新增鳥鳥
brid_group.add(brid)
#------------------------地板--------------------------
ground_image_x=0 # 地板 x 座標
ground_image_y=500 # 地板 y 座標
ground_img=pygame.image.load("image/ground.png") # 載入地板圖片
# 創建地板
ground_image=Ground(ground_img, ground_image_x, ground_image_y, speedx=5)
#------------------------水管-------------------------
pipe_image=pygame.image.load("image/pipe.png") # 載入水管圖片
pipe_image_x=SCREEN_WIDTH # 水管 x 座標
pipe_image_flip=pygame.transform.flip(pipe_image, False, True) # 旋轉後的水管圖片
pipe_time=pygame.time.get_ticks() # 取得程式開始到現在的時間
pipe_frequency=1500 # 每 1500 毫秒產生一組新管子
def create(pipe_time, pipe_frequency, pipe_sprite): # 創建水管函式
    now_time=pygame.time.get_ticks() # 呼叫函式的時間
    pipe_image_y=random.randint(100, 400) # 水管 y 座標 (隨機產生)
    if (now_time-pipe_time)>pipe_frequency: 
        # 每過 1500ms : (函式的時間-上一次產生的時間)>切換頻率
        pipe_bottom=Pipe(pipe_image, pipe_image_x, pipe_image_y+75, is_top=True) # 創建圖片
        pipe_top=Pipe(pipe_image_flip, pipe_image_x, pipe_image_y-75, is_top=False) # 創建圖片
        pipe_sprite.add(pipe_bottom) # 新增下水管到群組
        pipe_sprite.add(pipe_top) # 新增上水管到群組
        return now_time # 更新換管子時間
    return pipe_time
# 創建水管群組
pipe_sprite=pygame.sprite.Group()
# ---------------------------------------------------
# 按下空白鍵重新開始遊戲
def draw_restart():
    # 畫上空白圖片
    window.blit(restart_image, (SCREEN_WIDTH/2-(restart_image.get_width())/2\
                                , SCREEN_HEIGHT/2-(restart_image.get_height())/2))
#----------------------------------------------------
# 創建時鐘，統一時間(每個人電腦效能不同，統一時間才能一樣)
time=pygame.time.Clock()
run=True
while run: # 不斷偵測事件
    # 1 秒跑60次 (60FPS)
    time.tick(FPS)
    # --------取得輸入--------
    for event in pygame.event.get(): # 偵測所有事件
        if event.type==pygame.QUIT:
            # 如果事件的類型是關閉視窗按鈕
            run=False # 關閉視窗
        elif event.type==pygame.MOUSEBUTTONDOWN:
            # 如果事件的類型是點擊滑鼠
            mouse=event.button
            if mouse==1 and not game_over: # 左鍵的話
                brid.jump() # 鳥鳥往上飛
        elif event.type==pygame.KEYDOWN: # 按下鍵盤
            if event.key==pygame.K_SPACE and game_over: # 按的是空白鍵且遊戲輸了
                brid.rect.x=brid_image_x # 重新設定鳥的 x 座標
                brid.rect.y=brid_image_y # 重新設定鳥的 y 座標
                brid.game_over=False # 鳥鳥重新飛翔
                pass_pipe=0 # 分數歸零
                for i in range(len(pipe_position)):
                    pipe_position[i].kill()
                # for pipe in pipe_position:
                #     pipe.kill()
                game_over=False # 重新開始
    # --------遊戲更新--------
    # 水管與鳥鳥碰撞
    collide_pipe=pygame.sprite.groupcollide(pipe_sprite, brid_group, False, False)
    if collide_pipe or brid.rect.y>475 or brid.rect.y<0: # 如果撞到水管和上邊界與地板
        game_over=True # 遊戲結束
        brid.game_over=True # 鳥鳥停止飛翔
    if not game_over:
        # 地板往左持續移動
        ground_image.update(SCREEN_WIDTH)
        # 移動水管
        pipe_sprite.update()
        # 產生水管
        last_pipe_time=create(pipe_time, pipe_frequency, pipe_sprite)
        # 最後產生水管的時間
        pipe_time=last_pipe_time
        # ------------得分判斷-----------------
        # 取得水管群組所有的物件
        pipe_position=pipe_sprite.sprites()
        if len(pipe_position)>0: # 如果水管被創建出來的話
            for i in range(0, len(pipe_position), 2): # 取得創建出來的下水管
                if pipe_position[i].brid_npass: # 還沒被通過的水管
                    if brid.rect.left>pipe_position[i].rect.right: # 鳥鳥的左邊超過水管右邊
                        pass_pipe+=1 # 分數加一
                        pipe_position[i].brid_npass=False # 將這個水管變成已通過的水管
    #----------------------------------------------------
    # 鳥鳥的動畫以及地心引力
    brid_group.update()
    # 更新分數
    game_score.update(pass_pipe)
    # --------畫面顯示--------
    # 畫上背景
    window.blit(background_image, (0, 0))
    # 畫上鳥鳥
    brid_group.draw(window)
    # 畫上水管
    pipe_sprite.draw(window)
    # 畫上分數
    window.blit(game_score.render(), (SCREEN_WIDTH/2-text_size/2, SCREEN_HEIGHT/5-text_size/2))
    # 畫上地板
    window.blit(ground_img, (ground_image.x, ground_image.y))
    if game_over: # 遊戲結束時
        draw_restart() # 畫上重新開始圖片
    # --------更新畫面--------
    pygame.display.update()
# 結束 pygame
pygame.quit()