import pygame
class Ball:
    def __init__(self, x, y, radius, speedx, speedy):
        self.x=x # x 座標
        self.y=y # y 座標
        self.speedx=speedx # x 移動的速度
        self.speedy=speedy # y 移動的速度
        self.radius=radius # 半徑
    def draw(self, window, color): # 在視窗上面畫圓形
        self.window=window # 選擇的視窗
        self.color=color # 選擇的顏色
        pygame.draw.circle(self.window, self.color, (self.x, self.y), self.radius)
    def update(self): # 更新圓形的座標
        self.x+=self.speedx # 更新 x 座標
        self.y+=self.speedy # 更新 y 座標
        # 新增球體的四個感應座標
        ball_top=self.y-self.radius # 球體上方
        ball_bottom=self.y+self.radius # 球體下方
        ball_left=self.x-self.radius # 球體左方
        ball_right=self.x+self.radius # 球體右方
        if ball_left<0 or ball_right>700: # 如果 x 座標 撞到最左邊 0, 或最右邊 700
            self.speedx*=-1 # 變換速度方向
        elif ball_top<0 or ball_bottom>500: # 如果 y 座標 撞到最上面 0, 或最下面 500
            self.speedy*=-1 # 變換速度方向
