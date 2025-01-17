import pygame


class Back(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.interval_back = 700
        self.back_num = 0
        self.count = 0
        self.back_x = [620, 620]
        image_path = "images/back.png"
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image_obj = self.image.get_rect()
        self.distance = 0

    def update(self, screen):
        # result
        font = pygame.font.Font(None, 55)
        screen.blit(font.render("{self.distance}", True, (0, 0, 0)), [550, 0])

        # back
        if self.interval_back == 700:
            if self.back_num != 2:
                self.back_num += 1
            self.interval_back = 0
        if self.back_num != 0:
            while self.back_num > self.count:
                self.back_x[self.count] -= 0.5
                self.image_obj.x = self.back_x[self.count]
                if self.back_x[self.count] > -40:
                    if self.count == 1:
                        self.image_obj.y = 60
                    else:
                        self.image_obj.y = 30
                else:
                    self.back_x[self.count] = 620
                self.count += 1
            self.count = 0
        self.interval_back += 1
        self.distance += 1

    def stop(self, screen):
        # スコア表示
        font = pygame.font.Font(None, 55)
        screen.blit(font.render("{self.distance}", True, (0, 0, 0)), [550, 0])

        while self.back_num > self.count:
            if self.back_x[self.count] > -20:
                if self.back_x[self.count] > -40:
                    if self.count == 1:
                        self.image_obj.y = 60
                    else:
                        self.image_obj.y = 30
                else:
                    self.back_x[self.count] = 620
                self.count += 1
            self.count = 0
