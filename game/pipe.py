import pygame
class Pipe(pygame.sprite.Sprite):
    def __init__(self, img, x, y, is_top):
        super().__init__()
        self.speedx=4 # 移動速度
        self.image=img # 圖片
        self.brid_npass=True # 鳥鳥還沒通過
        self.rect=self.image.get_rect() # 取得圖片定位
        if is_top: # 座標位置
            self.rect.top=y # 距離視窗上面 y 
            self.rect.left=x # 距離視窗左邊 x
        else:
            self.rect.bottom=y # 上面的水管
            self.rect.left=x
    def update(self):
        self.rect.x-=self.speedx
