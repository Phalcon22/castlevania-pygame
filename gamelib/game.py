import pygame, os, sys, gamelib.main

from gamelib.Camera import *
from gamelib.Level import *
from gamelib.menus import *
from gamelib.UI import *
from gamelib.Constantes import *
from gamelib.Loading import PAUSE_SOUND, FONT, mydocuments


class Game:

    def __init__(self, screen, niveau):

        pygame.mixer.music.load("data/musics/Level_" + str(niveau) + ".ogg")
        pygame.mixer.music.play(-1)
        self.niveau = niveau
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.level = Level(str(niveau))
        self.level.create_level()
        self.belmont = self.level.belmont
        self.UI = UI(self.niveau)
        self.camera = Camera(self.screen, self.belmont, self.level.get_size()[0], self.level.get_size()[1])
        self.all_sprite = self.level.all_sprite
        self.dynamic_items_sprites = self.level.dynamic_items_sprites
        self.secondary_weapons_sprites = self.level.secondary_weapons_sprites
        self.x, self.y = 0, 0
        self.up = self.down = self.left = self.right = False
        self.continuer_jeu = True
        self.clock = pygame.time.Clock()
        self.font = FONT
        self.update_game()

    def update_game(self):
        try:
            pygame.mixer.music.unpause()
        except:
            pass
        
        while self.continuer_jeu:    
            for event in pygame.event.get():
                if event.type == QUIT:
                    continuer_jeu = 0
                    continuer  = 0
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.pause()
                    
                if event.type == KEYDOWN and event.key == K_UP:
                    self.up = True
                    if not self.belmont.climbing_left and not self.belmont.climbing_right:
                        self.belmont.determine_climbing(self.all_sprite, self.up, self.down)
                        
                if event.type == KEYDOWN and event.key == K_SPACE:
                    if not self.belmont.climbing_left and not self.belmont.climbing_right:
                        self.belmont.jump(self.all_sprite)
                if event.type == KEYDOWN and event.key == K_DOWN:
                    self.down = True
                    if not self.belmont.climbing_left and not self.belmont.climbing_right:
                        self.belmont.determine_climbing(self.all_sprite, self.up, self.down)
                if event.type == KEYDOWN and event.key == K_LEFT:
                    self.left = True
                if event.type == KEYDOWN and event.key == K_RIGHT:
                    self.right = True
                if event.type == KEYDOWN and (event.key == K_RCTRL or event.key == K_LCTRL):
                    self.belmont.attack()
                if event.type == KEYDOWN and event.key == K_RETURN:
                    self.belmont.secondary_attack(self.secondary_weapons_sprites, self.all_sprite)

                if event.type == KEYUP and event.key == K_UP:
                    self.up = False
                if event.type == KEYUP and event.key == K_DOWN:
                    self.down = False
                if event.type == KEYUP and event.key == K_LEFT:
                    self.left = False
                if event.type == KEYUP and event.key == K_RIGHT:
                    self.right = False

            self.screen.blit(self.level.background, (-self.camera.rect.x, -self.camera.rect.y+32))

            self.camera.draw_sprites(self.screen, self.all_sprite)
            self.UI.draw(self.screen, self.belmont, self.level)

            self.belmont.update(self.up, self.left, self.right, self.down, self.all_sprite, self.camera, self)
            self.camera.update(self.all_sprite, self)
            self.level.update(self.all_sprite, self.camera)
            self.UI.update(self.screen, self.belmont, self.level)
            pygame.display.flip()

            if self.belmont.game_over:
                self.continuer_jeu = 0
                gamelib.main.GameOver(self.screen, self.niveau)

            if self.belmont.win:
                self.up = self.down = self.left = self.right = False
                self.belmont.win = 0
                self.continuer_jeu = 1
                self.continuer()

            self.clock.tick(FPS)

            
    def pause(self):

        pygame.mixer.music.pause()
        PAUSE_SOUND.play()
        self.up = self.down = self.left = self.right = False
        self.menu = Main_menu(["CONTINUE", lambda: self.update_game()], ["MAIN MENU", lambda: gamelib.main.Menu(self.screen)], ["CONTROLS", lambda: gamelib.main.Help(self.screen)], ["QUIT GAME", lambda: sys.exit()])
        self.menu.set_highlight_color((255, 0, 0))
        self.menu.set_normal_color((255, 255, 255))
        self.menu.center_at(128, 120)
        self.font = FONT
        self.clock = pygame.time.Clock()
        events = pygame.event.get()
        self.menu.update(events)
        self.menu.draw(self.screen)
        self.pause_main_loop()

    def pause_main_loop(self):
        while 1:
            self.clock.tick(30)
            events = pygame.event.get()
            self.menu.update(events)
            for e in events:
                if e.type == QUIT:
                    pygame.quit()
                    return
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    self.update_game()
                    return      
            
            self.menu.draw(self.screen)
            pygame.display.flip()
            
    def continuer(self):

        try:
            save_file = open((mydocuments + "\\my games\\Castlevania\\saves\\save.sav"), "r")
            niveau = int(save_file.read())
            save_file.close()
        except:
            save_file = open((mydocuments + "\\my games\\Castlevania\\saves\\save.sav"), "w+")
            save_file.write(str(1))
            save_file.close()
            niveau = 1

        if self.niveau + 1 > niveau and self.niveau + 1 < 7:
            save_file = open((mydocuments + "\\my games\\Castlevania\\saves\\save.sav"), "w+")
            save_file.write(str(self.niveau + 1 ))
            save_file.close()

        self.niveau = int(self.niveau)
        if self.niveau != 6:
            self.niveau += 1
            self.niveau = str(self.niveau)
            self.__init__(self.screen, self.niveau)
        if self.niveau == 6:
            Menu(self.screen)

                              
    def save_game(self, niveau):
        save_file = open((mydocuments + "\\my games\\Castlevania\\saves\\save.sav"), "w+")
        save_file.write(str(niveau))
        save_file.close()
