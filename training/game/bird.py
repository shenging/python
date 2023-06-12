import pygame
class Bird(pygame.sprite.Sprite): # 繼承 sprite 類別 可以取得遊戲中所有物件
    def __init__(self, imags, x, y, game_over):
        pygame.sprite.Sprite.__init__(self)
        self.game_over=game_over # 起飛
        self.imags=imags # 所有的圖片
        self.number=0 # 圖片的序號
        self.speedy=0 # y 座標速度
        self.time=pygame.time.get_ticks() # 開始到現在的時間(最後一次切換的時間)
        self.fps=150 # 一張圖片 150 毫秒
        self.image=self.imags[self.number] # 圖片(一定要是 image)
        self.rect=self.image.get_rect() # 取得該圖片的定位
        self.rect.center=(x, y) # 使用 center 定位
    def update(self): # 更新鳥鳥的動作
        if not self.game_over: # 飛的話
            # 飛起來的動畫
            now_time=pygame.time.get_ticks() # 呼叫函式後開始的時間
            if now_time-self.time>self.fps: # (呼叫後的時間-切換後的時間)>切換頻率 (該換了)
                self.number+=1 # 換下一張
                if self.number>len(self.imags)-1: # 如果是最後一張了
                    self.number=0 # 回到第一張
                # 更新下一張圖片
                self.image=pygame.transform.rotate(self.imags[self.number], -self.speedy*2)
                self.time=now_time # 更新最後切換圖片時間
            # 地心引力
            self.rect.y+=self.speedy # 持續下墜
            self.speedy+=0.5 # 下墜速度增加 0.5 (重力加速度)
            if self.speedy>10: # 若下墜速度大於 10
                self.speedy=10 # 限制速度最大為 10
        else: # 不飛的話
            # 圖片更新為鳥鳥頭往下掉
            self.image=pygame.transform.rotate(self.imags[self.number], -90)
            if self.rect.y>475: # 頭撞到地板
                self.speedy=0 # 不再下墜
            else: # 還沒撞到地板
                self.speedy=10 # 往下墜 10
            self.rect.y+=self.speedy # 持續下墜
    def jump(self): # 往上飛
        self.speedy=-8 # 往上 10