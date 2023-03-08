from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD
import random

class Bird(Obstacle):

    def __init__(self, image):
        self.type = random.randint(0,1)
        super().__init__(image, self.type)
        self.rect.y = random.randint(150,300)
        self.index = 0

    def draw(self, screen):
        if self.index >= 9:
            self.index = 0

        screen.blit(BIRD[self.index // 5], self.rect)
        self.index += 1

