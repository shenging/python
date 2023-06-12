import pygame
class Paddle:
    def __init__(self, x, y, width, height, speed):
        self.x=x # x 座標
        self.y=y # y 座標
        self.width=width # 寬
        self.height=height # 高
        self.speed=speed # 速度
    def draw(self, window, color): # 在視窗上面畫矩形
        self.window=window # 選擇的視窗
        self.color=color # 選擇的顏色
        pygame.draw.rect(self.window, self.color, [self.x, self.y, self.width, self.height])
    def update(self, HEIGHT, key_up, key_down): # 更新 y 座標
        self.HEIGHT=HEIGHT # 視窗高度
        self.key_up=key_up # 往上鍵
        self.key_down=key_down # 往下鍵
        # 取得鍵盤的持續輸入
        key_pressed=pygame.key.get_pressed()
        if self.y>(self.HEIGHT-self.height): # 到底了的話
            if key_pressed[self.key_up]: # 只能按下往上鍵
                self.y-=self.speed # y 座標 --
        elif self.y<=0: # 到頂的話
            if key_pressed[self.key_down]: # 只能按下往下鍵
                self.y+=self.speed # y 座標 ++
        elif self.y>0 and self.y<self.HEIGHT: # 在視窗範圍中的話
            if key_pressed[self.key_up]: # 按下往上鍵
                self.y-=2 # y 座標 --
            elif key_pressed[self.key_down]: # 按下往下鍵
                self.y+=2 # y 座標 ++

