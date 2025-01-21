import pygame


class PlayerBase(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image_obj = self.image.get_rect()

        self.image_obj.x = 30
        self.image_obj.y = 370
        self.distance = 0
        self.jumping = False
        self.power = 0
        self.v0 = 17
        print("init")

    def update(self, screen):
        screen.blit(self.image, self.image_obj)

    def jump(self):
        self.power += 1
        self.image_obj.y = self.image_obj.y - (self.v0 - self.power)
        if self.image_obj.y >= 370:
            self.jumping = False
            self.power = 0
            self.image_obj.y = 370
