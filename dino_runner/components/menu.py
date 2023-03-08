import pygame
from dino_runner.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

class Menu:

    half_screen_height = SCREEN_HEIGHT // 2
    half_screen_width = SCREEN_WIDTH // 2
    screen_height = SCREEN_HEIGHT

    def __init__(self, message, screen):
        screen.fill((255,255,255))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_width, self.half_screen_height)

    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)

    def draw(self, screen):
        screen.blit(self.text, self.text_rect)

    def reset_screen_color(self, screen):
        screen.fill((255, 255, 255))

    def handle_events_on_menu (self, game):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                game.running = False
                game.playing = False

            elif event.type == pygame.KEYDOWN:
                game.run()

    def update_message (self):
        self.text = self.font.render('Press a key to restart.', True,(0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_width, self.half_screen_height )

    def update_best_score (self, game):
        font = pygame.font.Font(FONT_STYLE, 20)
        self.text = font.render(f'best score: {game.best_score}', True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_width, self.screen_height - 255 )

    def update_score (self, game):
        font = pygame.font.Font(FONT_STYLE, 20)
        self.text = font.render(f'score: {game.score}', True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_width, self.screen_height - 230 )

    def update_death (self, game):
        font = pygame.font.Font(FONT_STYLE, 20)
        self.text = font.render(f'deaths: {game.death_count}', True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.half_screen_width, self.screen_height - 205 )

    

