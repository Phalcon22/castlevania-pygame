import pygame
from pygame.locals import *

from gamelib.Constantes import *


class Camera():
    def __init__(self, screen, player, level_width, level_height):
        self.player = player
        self.rect = screen.get_rect()
        self.rect.height = 176
        self.rect.center = self.player.rect.center
        self.rect.centery = 616
        self.world_rect = Rect(0, 0, level_width, 880)

        self.cooldown = 0

        self.up_mode = False
        self.down_mode = False

        self.limit = 0
        self.limited = False

    def update(self, all_sprite, game):
        
        if self.limited:
            if self.player.rect.centerx > self.rect.centerx :
                self.rect.centerx = self.player.rect.centerx 
            if self.player.rect.centerx < self.rect.centerx and self.rect.left > self.limit:
                self.rect.centerx = self.player.rect.centerx

        if not self.limited:
            if self.player.rect.centerx > self.rect.centerx:
                self.rect.centerx = self.player.rect.centerx 
            if self.player.rect.centerx < self.rect.centerx:
                self.rect.centerx = self.player.rect.centerx

        if ((self.player.rect.top == self.rect.top and game.up) or (self.player.rect.bottom == self.rect.bottom and game.down)) and not self.down_mode and not self.up_mode and (self.player.climbing_left or self.player.climbing_right):
            self.cooldown = 174
            if (self.player.rect.bottom == self.rect.bottom and game.down):
                self.rect.centery += 2
                self.down_mode = True
            if (self.player.rect.top == self.rect.top  and game.up):
                self.rect.centery += -2
                self.up_mode = True

        if self.down_mode or self.up_mode:
            if self.cooldown > 0:
                self.cooldown -= 2
                if self.down_mode:
                    self.rect.centery += 2
                if self.up_mode:
                    self.rect.centery += -2
            if self.cooldown == 0:
                self.down_mode = False
                self.up_mode = False

        self.rect.clamp_ip(self.world_rect)

    def draw_sprites(self, screen, all_sprite):
        for s in all_sprite:    
            if s.rect.colliderect(self.rect):
                if (s.nom != "belmont" and s.nom != "whip") or (s.nom == "belmont" and not self.player.attack_mode):
                    try:
                        screen.blit(s.image, (s.rect.x-self.rect.x, s.rect.y-self.rect.y+32))
                    except:
                        pass
                if s.nom == "belmont" and self.player.attack_mode:
                    if (self.player.attack_phase == 2 and self.player.direction == "left") or (self.player.attack_phase == 3 and self.player.direction == "left") or (self.player.attack_phase == 4 and self.player.direction == "right") or self.player.attack_phase == 5:
                        screen.blit(s.image, (s.rect.x-self.rect.x, s.rect.y-self.rect.y+32))
                if s.nom == "whip" and self.player.attack_mode:
                    if (self.player.attack_phase == 2 and self.player.direction == "right") or (self.player.attack_phase == 3 and self.player.direction == "right") or (self.player.attack_phase == 4 and self.player.direction == "left"):
                        screen.blit(s.image, (s.rect.x-self.rect.x, self.player.rect.y-self.rect.y+32))

                if s.nom == "limit":
                    self.limited = True
                    self.limit = s.rect.x

                if s.nom == "unlimit":
                    self.limited = False
