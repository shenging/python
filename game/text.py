import pygame
class Text:
    def __init__(self, file, size, content, is_jagged, color):
        self.file=file # 文字檔案
        self.size=size # 文字大小
        self.content=content # 文字內容
        self.is_jagged=is_jagged # 文字是否要鋸齒
        self.color=color # 文字顏色
    def render(self):
        # 引入文字檔案
        font=pygame.font.Font(self.file, self.size)
        # 設定文字格式
        result=font.render(str(self.content), self.is_jagged, self.color)
        return result
    def update(self, content): # 更新文字內容
        self.content=str(content)