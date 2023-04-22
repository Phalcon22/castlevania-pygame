import pygame
from pygame.locals import *

from gamelib.Constantes import *
from gamelib.Loading import CANDLE, LARGEHEART, SMALLHEART, LARGECANDLE, DAGGER, AXE, MAGICALCRYSTAL, WHIPUPGRADE

class Sprites(pygame.sprite.Sprite):
    def __init__(self, x, y, nom):
        pygame.sprite.Sprite.__init__(self)
        self.nom = nom
        surface = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.rect = surface.get_rect()
        self.rect.x = x
        self.rect.y = y

class Destructible(pygame.sprite.Sprite):
    def __init__(self, x, y, image, nom):
        pygame.sprite.Sprite.__init__(self)
        self.nom = nom
        self.image1 = image[0]
        self.image2 = image[1]
        self.image = self.image1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.phase = 0

    def update(self):
        
        if self.phase < 8:
            self.image = self.image1
        if self.phase >= 8:
            self.image = self.image2

        if self.phase == 16:
            self.phase = 0
        self.phase += 1

    def drop(self, dynamic_items_sprites, all_sprite):
        dynamic_items_sprites.add(Consommable(self.rect.x, self.rect.y, self.nom))
        all_sprite.add(dynamic_items_sprites)


class Consommable(pygame.sprite.Sprite):
    def __init__(self, x, y, nom):
        pygame.sprite.Sprite.__init__(self)
        self.nom = "consommable"
        self.dropped = nom
        
        if self.dropped == "large_candle":
            self.image = LARGEHEART
        if self.dropped == "candle":
            self.image = SMALLHEART
        if self.dropped == "large_candle_whip":
            self.image = WHIPUPGRADE
        if self.dropped == "large_candle_dagger":
            self.image = DAGGER
        if self.dropped == "candle_axe":
            self.image = AXE
        if self.dropped == "magicalcrystal":
            self.image = MAGICALCRYSTAL[0]
            
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.movy = 0
        self.contact = False

    def update(self, all_sprite):
        
        if self.dropped == "magicalcrystal":
            if self.image == MAGICALCRYSTAL[0]:
                self.image = MAGICALCRYSTAL[1]
            elif self.image == MAGICALCRYSTAL[1]:
                self.image = MAGICALCRYSTAL[0]

        if not self.contact:
            self.movy += 0.5
            self.rect.y += self.movy
            self.collide(all_sprite)

    def collide(self, all_sprite):
        for o in all_sprite:
            if self.rect.colliderect(o):
                if o.nom == "obstacle" or o.nom == "platform" or o.nom == "stairsspecial":
                    self.rect.bottom = o.rect.top
                    self.contact = True
