import pygame
from pygame.locals import *

from gamelib.Sprites import *
from gamelib.Weapon import *
from gamelib.Player import *
from gamelib.Enemies import *
from gamelib.Constantes import *
from gamelib.Loading import BACKGROUND, CANDLE, LARGEHEART, SMALLHEART, LARGECANDLE, DAGGER, AXE, MAGICALCRYSTAL, WHIPUPGRADE

class Level():
    def __init__(self, choix):

        self.background = BACKGROUND[int(choix)-1]
        self.background_rect = self.background.get_rect()

        level = "levels/level" + choix
        
        self.level1 = []
        self.all_sprite = pygame.sprite.Group()
        self.enemies_sprites = pygame.sprite.Group()
        self.static_items_sprites = pygame.sprite.Group()
        self.dynamic_items_sprites = pygame.sprite.Group()
        self.secondary_weapons_sprites = pygame.sprite.Group()
        self.world_sprites = pygame.sprite.Group()
        self.boss_sprites = pygame.sprite.Group()
        self.level = open(level, "r")
        self.mobs = 0
        self.zombie_here = 0

    def create_level(self):
        x = 0
        y = 0
        for l in self.level:
            self.level1.append(l)

        for row in self.level1:
            for col in row:

                if col == "P":
                    self.belmont = Belmont(x,y)
                    self.all_sprite.add(self.belmont)
                    self.whip = Whip(self.belmont)
                    self.all_sprite.add(self.whip)
                
                if col == "X":
                    obstacle = Sprites(x, y, "obstacle")
                    self.world_sprites.add(obstacle)
                    self.all_sprite.add(self.world_sprites)
                if col == "x":
                    platform = Sprites(x, y, "platform")
                    self.world_sprites.add(platform)
                    self.all_sprite.add(self.world_sprites)
                if col == "Y":
                    stairsspecial = Sprites(x, y, "stairsspecial")
                    self.world_sprites.add(stairsspecial)
                    self.all_sprite.add(self.world_sprites)
                if col == "L":
                    limit = Sprites(x, y, "limit")
                    self.world_sprites.add(limit)
                    self.all_sprite.add(self.world_sprites)
                    
                if col == "A":
                    arriver = Sprites(x, y, "arriver")
                    self.all_sprite.add(arriver)
                if col == "W":
                    startboss = Sprites(x, y, "startboss")
                    self.all_sprite.add(startboss)
                if col == "R":
                    stairs_up_left = Sprites(x, y, "stairs_up_left")
                    self.all_sprite.add(stairs_up_left)
                if col == "r":
                    stairs_down_left = Sprites(x, y, "stairs_down_left")
                    self.all_sprite.add(stairs_down_left)
                if col == "Q":
                    stairs_up_right = Sprites(x, y, "stairs_up_right")
                    self.all_sprite.add(stairs_up_right)
                if col == "q":
                    stairs_down_right = Sprites(x, y, "stairs_down_right")
                    self.all_sprite.add(stairs_down_right)
                    
                if col == "z":
                    self.enemies_sprites.add(Zombie(x, y))
                    self.all_sprite.add(self.enemies_sprites)
                if col == "l":
                    self.enemies_sprites.add(Leopard(x, y))
                    self.all_sprite.add(self.enemies_sprites)
                if col == "b":
                    self.enemies_sprites.add(Bat(x, y))
                    self.all_sprite.add(self.enemies_sprites)
                    
                if col == "V":
                    self.Boss = Boss1(x, y)
                    self.boss_sprites.add(self.Boss)
                    self.all_sprite.add(self.boss_sprites)
                    
                if col == "c":
                    self.static_items_sprites.add(Destructible(x, y, CANDLE, "candle"))
                    self.all_sprite.add(self.static_items_sprites)
                if col == "C":
                    self.static_items_sprites.add(Destructible(x, y, LARGECANDLE, "large_candle"))
                    self.all_sprite.add(self.static_items_sprites)
                if col == "D":
                    self.static_items_sprites.add(Destructible(x, y, LARGECANDLE, "large_candle_dagger"))
                    self.all_sprite.add(self.static_items_sprites)
                if col == "h":
                    self.static_items_sprites.add(Destructible(x, y, CANDLE, "candle_axe"))
                    self.all_sprite.add(self.static_items_sprites)
                if col == "I":
                    self.static_items_sprites.add(Destructible(x, y, LARGECANDLE, "large_candle_whip"))
                    self.all_sprite.add(self.static_items_sprites)
                    
                x += BLOCK_SIZE
            y += BLOCK_SIZE
            x = 0

    def update(self, all_sprite, camera):
        self.whip.update(all_sprite, self.belmont, self.dynamic_items_sprites)
        self.enemies_sprites.update(self.world_sprites, self.belmont)
        self.static_items_sprites.update()
        self.dynamic_items_sprites.update(all_sprite)
        
        self.boss_sprites.update(self.belmont, camera)
        for i in self.boss_sprites:
            if i.health <= 0:
                pygame.mixer.music.load("data/musics/End_level.ogg")
                pygame.mixer.music.play()
                self.belmont.score += 3000
                i.drop(self.dynamic_items_sprites, self.all_sprite)
                i.kill()

        self.secondary_weapons_sprites.update(all_sprite)
        for i in self.secondary_weapons_sprites:
            if i.contact:
                i.kill()
                    
                    
    def get_size(self):
        lines = self.level1
        line = max(lines, key=len)
        self.width = (len(line)-1)*BLOCK_SIZE
        self.height = (len(lines))*BLOCK_SIZE
        return (self.width, self.height)
