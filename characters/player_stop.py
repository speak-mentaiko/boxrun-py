import player_base


class PlayerStop(player_base.PlayerBase):
    def __init__(self, distance):
        self.image_path = (
            "../images/box_0_hit.png"
            if distance % 2 == 0
            else "../images/box_1_hit.png"
        )
        super().__init__(self.image_path)

    def update(self, screen):
        super(screen)
