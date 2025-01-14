import random
import scene_base

import sys

sys.path.append("..")
from characters import enemy


class Running(scene_base):
    def __init__(self):
        super().__init__()
        self.player
        self.enemy
        self.back
        self.enemies = []
        self.interval_enemy = 0
        self.random_enemy = 0

    def update(self, screen):
        super
        self.back.update
        self.player.update

        if self.interval_enemy == 0:
            self.random_enemy = random.randint(40, 90)
        if len(self.enemies) <= 3 & self.interval_enemy == self.random_enemy:
            self.enemies.append(enemy())
            self.interval_enemy = 0
        self.interval_enemy += 1
