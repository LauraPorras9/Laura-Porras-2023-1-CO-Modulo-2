import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManger:
    def __init__(self):

        SMALL_CACTUS.extend(LARGE_CACTUS)

        self.obstacles = []
        self.music = pygame.mixer.Sound('muerte.mp3')

    def update(self, game):

        if len(self.obstacles) == 0:

            random_obstacle = random.randint(0,200)

            if random_obstacle > 150:

                bird = Bird(BIRD)
                self.obstacles.append(bird)

            else:
                cactus = Cactus(SMALL_CACTUS)
                self.obstacles.append(cactus)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.death_count += 1
                game.playing = False
                self.music.play()
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def resert_obstacles(self):
        self.obstacles = []