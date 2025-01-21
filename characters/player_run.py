import pygame

from characters.player_base import PlayerBase


class PlayerRun(PlayerBase):
    def __init__(self):
        self.image_path_0 = "images/box_0.png"
        self.image_path_1 = "images/box_1.png"
        super().__init__(self.image_path_0)
        self.distance = 0

    def update(self, screen):
        super().update(screen)
        self.change_image()
        if self.jumping == False:
            if pygame.key.get_pressed == pygame.K_SPACE:
                self.jumping = True
        elif self.jumping == True:
            self.jump

    def change_image(self):
        if self.distance % 7 == 0:
            self.distance += 1
        self.distance += 1
        if (self.distance / 4) % 2 == 0:
            self.image = pygame.image.load(self.image_path_0).convert_alpha()
            self.image_obj = self.image.get_rect()
        else:
            self.image = pygame.image.load(self.image_path_1).convert_alpha()
            self.image_obj = self.image.get_rect()
