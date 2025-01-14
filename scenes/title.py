import pygame
import scene_base
import running
import sys

sys.path.append("..")
from characters import player_start


class Title(scene_base):
    def __init__(self):
        super
        self.player = player_start()
        self.start = False

    def update(self, screen):
        super
        self.player.update
        if pygame.key.get_pressed == pygame.K_SPACE:
            self.start = True
        if self.start:
            self.player.jump
            self.player.update(screen)
            if self.player.y == 370:
                self.flg = True

    def next_scene(self):
        self.next = running()
