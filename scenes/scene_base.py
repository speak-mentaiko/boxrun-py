import pygame


class SceneBase:
    def __init__(self):
        self.flg = False
        self.bg = pygame.image.load("images/stage.png").convert_alpha()
        self.bg_obj = self.bg.get_rect()

    def update(self, screen):
        # 背景画像の描画
        print("scene base")
        screen.blit(self.bg, self.bg_obj)

    def is_finish(self):
        return self.flg

    def reset(self):
        self.flg = False

    def next_scene(self):
        return self.next
