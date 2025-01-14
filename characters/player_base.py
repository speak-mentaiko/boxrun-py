import pygame


class Player_base(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image_obj = self.image.get_rect()

        self.x = 30
        self.y = 370
        self.distance = 0
        self.jumping = False
        self.power = 0
        self.v0 = 17

    def update(self, screen):
        screen.bilt(self.image, self.image_obj)

    def jump(self):
        self.power += 1
        self.y = self.y - (self.v0 - self.power)
        if self.y >= 370:
            self.jumping = False
            self.power = 0
            self.y = 370
