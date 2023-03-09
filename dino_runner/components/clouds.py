import random
from pygame.sprite import Sprite
from dino_runner.utils.constants import CLOUD, SCREEN_WIDTH

class Nube(Sprite):

    def __init__(self):
        self.image = CLOUD
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(50,200)
        self.cloud = []
        self.game = 0

    def update_cloud(self, game_speed, cloud):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            self.cloud.append(self.image)
            cloud.pop()

    def update(self, game):

        if game.game_speed % 2 == 0:
            self.update_cloud(game.game_speed, self.cloud)
            self.cloud.append(self.image)
            for cloud in self.cloud:
                self.cloud.remove(cloud)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))