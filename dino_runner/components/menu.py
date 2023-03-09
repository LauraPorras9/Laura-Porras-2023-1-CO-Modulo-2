import pygame
from dino_runner.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

class Menu:

    half_screen_height = SCREEN_HEIGHT // 2
    half_screen_width = SCREEN_WIDTH // 2

    def __init__(self, screen):
        screen.fill((255,255,255))
        self.font = pygame.font.Font(FONT_STYLE, 25)

    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)

    def draw(self, screen, message, x = half_screen_width, y = half_screen_height):
        text = self.font.render(message, True, (83,83,83))
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        screen.blit(text, text_rect)

    def reset_screen_color(self, screen):
        screen.fill((255, 255, 255))

    def handle_events_on_menu (self, game):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                game.running = False
                game.playing = False

            elif event.type == pygame.KEYDOWN:
                game.run()
