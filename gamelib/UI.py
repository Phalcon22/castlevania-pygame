import pygame

from gamelib.Loading import FONT, UIBACKGROUND, HP, UIDAGGER, UIAXE, HPBOSS

class UI:
    def __init__(self, niveau):
        
        self.score = 0
        self.level_time = 300
        self.timer = 0
        self.time = 0
        self.stage = niveau
        self.player = 16
        self.enemy = 16
        self.ammo = 0
        self.font = FONT

        self.bg = UIBACKGROUND

        self.hp = HP[16]

        self.boss = 16
        self.hpboss = HPBOSS[16]

        self.secondary_weapon = pygame.Surface((0, 0))

    def update(self, screen, player, level):

        if self.timer > 0:
            self.time += 1
        self.timer = self.level_time - (self.time /60)
        if self.timer == 0:
            player.game_over = True
        
        self.player = player.health
        self.ammo = player.ammo
        self.score = player.score

        self.hp = HP[self.player]
        self.hpboss = HPBOSS[level.Boss.health]

        if player.secondary_weapon == "dagger":
            self.secondary_weapon = UIDAGGER

        if player.secondary_weapon == "axe":
            self.secondary_weapon = UIAXE

    def draw(self, screen, player, level):

        ammo = self.font.render(str(self.ammo), 1, (255,255,255))
        score = self.font.render(str(self.score), 1, (255,255,255))
        time = self.font.render(str(int(self.timer)), 1, (255,255,255))
        stage = self.font.render(str(self.stage), 1, (255,255,255))

        screen.blit(self.bg, (0,0))
        screen.blit(ammo, (185, 9))
        screen.blit(score, (60,1))
        screen.blit(time, (145,1))
        screen.blit(stage, (230,1))
        screen.blit(self.hp, (56,10))
        screen.blit(self.hpboss, (56,18))
        screen.blit(self.secondary_weapon, (135, 12))
