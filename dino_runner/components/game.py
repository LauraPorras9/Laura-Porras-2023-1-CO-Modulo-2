import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, GAMEOVER, DEAD
from dino_runner.components.dinosaur import Dinasaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManger
from dino_runner.components.reset_game import ResetGame
from dino_runner.components.menu import Menu
from dino_runner.components.score import Score
from dino_runner.utils.constants import FONT_STYLE

class Game:
    GAME_SPEED = 20
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = self.GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinasaur()
        self.obstacle_manager = ObstacleManger()
        self.menu = Menu('Press any key to start..', self.screen)
        self.reset_game = ResetGame()
        self.draw_score = Score()
        self.running = False
        self.score = 0
        self.best_score = 0
        self.death_count = 0

    def execute(self):
        
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.obstacle_manager.resert_obstacles()
        self.reset_game.run(self)
        while self.playing:
            self.events()
            self.update()
            self.draw()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):

        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.draw_score.update(self)

    def draw(self):
        self.clock.tick(FPS)
        if self.score > 500 and self.score < 900:
            self.screen.fill((0, 0, 0))
        else:
            self.screen.fill((255, 255, 255))
        self.player.draw(self.screen)
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score.draw(self)
        pygame.display.update()
        #pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def show_menu(self):
        self.menu.reset_screen_color(self.screen)
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_heigth = SCREEN_HEIGHT // 2

        if self.death_count == 0:
            self.menu.draw(self.screen)
            self.screen.blit(ICON, (half_screen_width - 50, half_screen_heigth - 140))
        else:
            self.screen.blit(DEAD, (half_screen_width - 40, half_screen_heigth - 200))
            self.screen.blit(GAMEOVER, (half_screen_width - 195, half_screen_heigth - 80))
            self.menu.update_message()
            self.menu.draw(self.screen)
            self.menu.update_best_score(self)
            self.menu.draw(self.screen)
            self.menu.update_score(self)
            self.menu.draw(self.screen)
            self.menu.update_death(self)
            self.menu.draw(self.screen)

        self.menu.update(self)


