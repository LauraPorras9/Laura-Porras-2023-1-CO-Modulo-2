import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, GAMEOVER, DEAD, DEFAULT_TYPE
from dino_runner.components.dinosaur import Dinasaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManger
from dino_runner.components.menu import Menu
from dino_runner.components.score import Score
from dino_runner.utils.constants import FONT_STYLE
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

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
        self.menu = Menu( self.screen)
        self.draw_score = Score()
        self.running = False
        self.score = 0
        self.best_score = 0
        self.death_count = 0
        self.power_up_manager = PowerUpManager()

    def execute(self):
        
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.reset_game()
        self.playing = True
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
        self.power_up_manager.update(self)
        self.draw_score.update(self)

    def draw(self):
        self.clock.tick(FPS)
        if self.score > 500 and self.score < 1000:
            self.screen.fill((0, 0, 0))
        else:
            self.screen.fill((255, 255, 255))
        self.player.draw(self.screen)
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score.draw(self)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
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
            self.menu.draw(self.screen, 'Press any key to start..')
            self.screen.blit(ICON, (half_screen_width - 50, half_screen_heigth - 140))
        else:
            self.screen.blit(DEAD, (half_screen_width - 45, half_screen_heigth - 160))
            self.screen.blit(GAMEOVER, (half_screen_width - 195, half_screen_heigth - 50))
            self.menu.draw(self.screen, f'best score: {self.best_score}', half_screen_width, 350)
            self.menu.draw(self.screen, f'score: {self.score}', half_screen_width, 400)
            self.menu.draw(self.screen, f'deaths: {self.death_count}', half_screen_width, 450)

        self.menu.update(self)

    def reset_game (self):
        self.obstacle_manager.resert_obstacles()
        self.game_speed = self.GAME_SPEED
        self.player.reset()
        self.score = 0

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks()) / 1000, 2)

            if time_to_show >= 0:
                self.menu.draw(self.screen, f'{self.player.type.capitalize()}: {time_to_show}', 500, 50 )
            else:
                self.has_power_up = False
                self.player.type = DEFAULT_TYPE

