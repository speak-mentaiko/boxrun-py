import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image_obj = self.image.get_rect()

        self.x = 700
        self.y = 380

    def update(self, screen):
        self.x -= 8
        screen.bilt(self.image, self.image_obj)
