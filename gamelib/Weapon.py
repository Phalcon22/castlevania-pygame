import pygame
from pygame.locals import *

from gamelib.Loading import WHIP_LEFT, HURT_SOUND, WHIP_RIGHT, EXPERT_WHIP_LEFT, EXPERT_WHIP_RIGHT, DAGGER, AXE

class Whip(pygame.sprite.Sprite):

    def __init__(self, player):

        pygame.sprite.Sprite.__init__(self)
        
        self.rect = pygame.Rect(player.rect.x, player.rect.y, 28, 8)
        self.rect.topright = player.rect.topleft

        self.nom = "whip"
        self.degat = 1
        self.whip_left = WHIP_LEFT
        self.whip_right = WHIP_RIGHT
        self.image = self.whip_left[0]
        
    def update(self, all_sprite, player, dynamic_items_sprites):

        if player.whip == "advanced":
            self.degat = 2

        if player.whip == "expert":
            self.degat = 2
            self.whip_left = EXPERT_WHIP_LEFT
            self.whip_right = EXPERT_WHIP_RIGHT
            self.rect.width = 44

        if not player.attack_mode:
            self.rect.topright = player.rect.topleft

        if player.attack_mode:
            if player.attack_phase == 2:
                if player.direction == "right":
                    self.rect.x = player.rect.x - 16
                    self.image = self.whip_right[1]
                    
            if player.attack_phase == 3:
                if player.direction == "right":
                    self.image = self.whip_right[2]
                    
            if player.attack_phase == 4:
                self.rect.y = player.rect.y + 7
                if player.direction == "left":
                    self.image = self.whip_left[3]
                    self.rect.right = player.rect.left
                if player.direction == "right":
                    self.rect.left = player.rect.right
                    
            if player.attack_phase == 1:
                self.rect.topright = player.rect.topleft

            self.collide(all_sprite, player, dynamic_items_sprites)

    def collide(self, all_sprite, player, dynamic_items_sprites):
        for o in all_sprite:
            if self.rect.colliderect(o):
                if o.nom == "candle" or o.nom == "large_candle" or o.nom == "large_candle_dagger" or o.nom == "candle_axe" or o.nom == "large_candle_whip":
                    if player.attack_phase == 4:
                        HURT_SOUND.play()
                        o.drop(dynamic_items_sprites, all_sprite)
                        o.kill()
                if o.nom == "bat" or o.nom == "zombie" or o.nom == "leopard" or o.nom == "boss1":
                    if player.attack_phase == 4:
                        o.get_hit(self.degat)


class SecondaryWeapon(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, image):
        pygame.sprite.Sprite.__init__(self)
        self.direction = direction
        self.nom = None
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.movy = 0
        self.contact = False
        
    def update(self, all_sprite):
        if self.direction == "right":
            self.rect.x += 3
        if self.direction == "left":
            self.rect.x -= 3

        self.collide(all_sprite)

    def collide(self, all_sprite):
        if self.direction == "right":
            self.rect.x += 3
        if self.direction == "left":
            self.rect.x -= 3
        
        for o in all_sprite:
            if self.rect.colliderect(o):
                if o.nom == "obstacle" or o.nom == "platform" or o.nom == "stairsspecial":
                    self.contact = True
                if (o.nom == "zombie" or o.nom == "bat" or o.nom == "leopard") and not o.dying and not o.reset:
                    HURT_SOUND.play()
                    o.health -= 1
                    self.contact = True
                if o.nom == "boss1":
                    HURT_SOUND.play()
                    o.health -= 1
                    self.contact = True

class ThrewDagger(SecondaryWeapon):
    def __init__(self, x, y, direction):
        SecondaryWeapon.__init__(self, x, y, direction, DAGGER)
        self.nom = "threw_dagger"
        self.movy = 0
        
    def update(self, all_sprite):
        self.collide(all_sprite)


class ThrewAxe(SecondaryWeapon):
    def __init__(self, x, y, direction):
        SecondaryWeapon.__init__(self, x, y, direction, AXE)
        self.nom = "threw_axe"
        self.movy = -5

    def update(self, all_sprite):
        self.movy += 0.3
        self.rect.y += self.movy
        self.collide(all_sprite)
