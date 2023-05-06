class Ground():
    def __init__(self, image, x, y,speedx):
        self.image=image # 圖片
        self.x=x # x 座標
        self.y=y # y 座標
        self.speedx=speedx # x 的速度
    def update(self, SCREEN_WIDTH):
        self.x-=self.speedx # 往左更新 x 座標
        if self.x<=(SCREEN_WIDTH-self.image.get_width()): # 如果 x 座標小於(視窗寬-圖片寬)
            self.x=0 # 回到原來的位置
            self.x-=self.speedx # 繼續往左更新 x 座標