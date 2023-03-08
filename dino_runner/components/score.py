import pygame
from dino_runner.utils.constants import FONT_STYLE

class Score:
    
    def __init__(self):
        
        self.score = 0
        self.music = pygame.mixer.Sound('level up.mp3')

    def update(self, game):

        game.score += 1
        self.score = game.score
        if game.score % 100 == 0 and game.game_speed < 500:
            game.game_speed += 5
            self.music.play()

        if game.score > game.best_score:
            game.best_score = self.score

    def draw(self, screen):

        if self.score > 500 and self.score < 900:
            font = pygame.font.Font(FONT_STYLE, 20)
            text = font.render(f'Score: {self.score}', True, (255,255,255))
            text_rect = text.get_rect()
            text_rect.center = (1000, 50)
            screen.screen.blit(text,text_rect)

        else:
            font = pygame.font.Font(FONT_STYLE, 20)
            text = font.render(f'Score: {self.score}', True, (0,0,0))
            text_rect = text.get_rect()
            text_rect.center = (1000, 50)
            screen.screen.blit(text,text_rect)




