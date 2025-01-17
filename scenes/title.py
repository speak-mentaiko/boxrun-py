import pygame
import sys

from scenes.scene_base import SceneBase
from scenes.running import Running

sys.path.append("..")
from characters.player_start import PlayerStart


class Title(SceneBase):
    def __init__(self):
        super().__init__()
        self.player = PlayerStart()
        self.start = False

    def update(self, screen):
        super().update(screen)
        self.player.update(screen)
        if pygame.key.get_pressed == pygame.K_SPACE:
            self.start = True
        if self.start:
            self.player.jump
            self.player.update(screen)
            if self.player.y == 370:
                self.flg = True

    def next_scene(self):
        self.next = Running()
