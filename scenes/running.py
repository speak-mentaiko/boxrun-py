import random
import pygame

from scenes.scene_base import SceneBase

import sys

sys.path.append("..")
from characters import enemy
from characters import player_run
from characters import back


class Running(SceneBase):
    def __init__(self):
        super().__init__()
        self.player = player_run.PlayerRun()
        self.back = back.Back()
        self.enemies = []
        self.interval_enemy = 0
        self.random_enemy = 0

    def update(self, screen):
        super().update(screen)
        sprite_group = pygame.sprite.Group()

        self.back.update(screen)
        self.player.update

        if self.interval_enemy == 0:
            self.random_enemy = random.randint(40, 90)
        if len(self.enemies) <= 3 & self.interval_enemy == self.random_enemy:
            enemy_inst = enemy.Enemy()
            self.enemies.append(enemy_inst)
            sprite_group.add(enemy_inst)
            sprite_group.add()
            self.interval_enemy = 0
        self.interval_enemy += 1

        for ene in self.enemies:
            ene.update(screen)
            # 当たり判定
            if ene.x < -10:
                del ene

        sprite_group.draw(screen)
