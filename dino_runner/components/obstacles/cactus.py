from dino_runner.components.obstacles.obstacle import Obstacle
import random

class Cactus(Obstacle):

    def __init__(self, image):
        self.type = random.randint(0,6)
        super().__init__(image, self.type)

        if self.type > 2:
            self.rect.y = 300

        else:
            self.rect.y = 325