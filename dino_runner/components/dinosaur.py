import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD, DEFAULT_TYPE, SHIELD_TYPE, HAMMER_TYPE, JUMPING_HAMMER, DUCKING_HAMMER, RUNNING_HAMMER

RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}


class Dinasaur(Sprite):
    X_POS = 80
    Y_POS = 310
    JUMP_SPEED = 8.5
    DUCK = 340

    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0 #contador
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.dino_dead = False
        self.jump_speed = self.JUMP_SPEED
        self.music = False
        self.sound = pygame.mixer.Sound('dinosaurio.mp3')
        self.has_power_up = False
        self.power_time_up = 0
        self.hammer_throw = False

    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False

        elif user_input[pygame.K_DOWN] and not self.dino_duck:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False

        elif user_input[pygame.K_RIGHT]:
            self.hammer_throw = True

        elif not self.dino_jump:
            self.dino_jump = False
            self.dino_run = True
            self.dino_duck = False
    
        if self.step_index >= 10:
            self.step_index = 0

    def run(self):
        self.image = RUN_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1
        self.music = False

    def duck(self):
        self.image = DUCK_IMG[self.type][self.step_index // 5]
        if self.dino_duck:
            self.dino_rect.y = self.Y_POS + 30
            self.step_index += 1
            if not self.music:
                self.sound.play()
                self.music = True
        
        if self.dino_rect.y == self.DUCK:
            self.dino_duck = False
            
    def jump(self):
        self.image = JUMP_IMG[self.type]
        self.dino_rect.y -= self.jump_speed * 4
        self.jump_speed -= 0.8
        if not self.music:
            self.sound.play()
            self.music = True

        if self.jump_speed < -self.JUMP_SPEED:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_speed = self.JUMP_SPEED

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def reset(self):
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_speed = self.JUMP_SPEED