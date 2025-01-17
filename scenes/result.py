import scene_base
import sys
import pygame

sys.path.append("..")
from characters import player_stop
from characters import back


class Result(scene_base.Scene_base):
    def __init__(self):
        super().__init__()
        self.player = player_stop.PlayerStop()
        self.back = back.Back()

    def update(self, screen):
        super
        self.back.stop
        self.player.update
        if pygame.key.get_pressed == pygame.K_SPACE:
            self.flg = True
        font = pygame.font.Font(None, 24)
        screen.blit(font.render("PUSH SPACE", True, (0, 0, 0)), [230, 200])
        screen.blit(font.render("{self.distance}", True, (0, 0, 0)), [550, 0])
