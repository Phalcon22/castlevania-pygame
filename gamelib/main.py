import pygame, os, sys

from pygame.locals import *

from gamelib.Level import *
from gamelib.Camera import *
from gamelib.Constantes import *
from gamelib.menus import *
from gamelib.game import *
from gamelib.cutscenes import *
from gamelib.Loading import MAP, ICON


def main():
    pygame.init()
    pygame.mouse.set_visible(0)
    pygame.display.set_caption("Castlevania")
    pygame.display.set_icon(ICON)
    screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN, 32)
    Title(screen)
    

def SelectLevel(screen, niveau):
    Game(screen, niveau)

def Help(screen):
    cutscene(screen, ["CONTROLS",
    "",
    "Move: Arrow Keys",
    "Jump: Space",
    "Attack : Ctrl",
    "",
    ""])

class Menu():

    def __init__(self, screen):

        try:
            pygame.mixer.music.stop()
        except:
            pass
        
        self.screen = screen
        self.menu = Main_menu(["SELECT LEVEL", lambda: GotoMap(screen)], ["CONTROLS", lambda: Help(screen)], ["QUIT GAME", sys.exit])
        self.menu.set_highlight_color((255, 0, 0))
        self.menu.set_normal_color((255, 255, 255))
        self.menu.center_at(128, 104)
        self.clock = pygame.time.Clock()
        events = pygame.event.get()
        self.bg = pygame.Surface((256, 208))
        self.bg.fill((0, 0, 0))
        self.menu.update(events)
        self.menu.draw(self.screen)
        self.main_loop()

    def main_loop(self):
        while 1:
            self.clock.tick(30)
            events = pygame.event.get()
            self.menu.update(events)
            for e in events:
                if e.type == QUIT:
                    sys.exit()
                    return
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    sys.exit()
                    return
                
            self.screen.blit(self.bg, (0, 0))         
            
            self.menu.draw(self.screen)
            pygame.display.flip()


class GameOver():

    def __init__(self, screen, niveau):

        try:
            pygame.mixer.music.stop()
        except:
            pass

        self.screen = screen
        self.menu = Main_menu(["RESTART", lambda: Game(screen, niveau)], ["MAIN MENU", lambda: Menu(screen)], ["HELP", lambda: Help(screen)], ["QUIT GAME", sys.exit])
        self.menu.set_highlight_color((255, 0, 0))
        self.menu.set_normal_color((255, 255, 255))
        self.menu.center_at(128, 104)
        self.bg = pygame.Surface((256, 208))
        self.bg.fill((0, 0, 0))
        self.clock = pygame.time.Clock()
        events = pygame.event.get()
        self.menu.update(events)
        self.menu.draw(self.screen)
        self.main_loop()

    def main_loop(self):
        while 1:
            self.clock.tick(30)
            events = pygame.event.get()
            self.menu.update(events)
            for e in events:
                if e.type == QUIT:
                    pygame.quit()
                    return
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    pygame.quit()
                    return
                
            self.screen.blit(self.bg, (0, 0))         
            
            self.menu.draw(self.screen)
            pygame.display.flip()

            

class GotoMap():

    def __init__(self, screen):

        try:
            pygame.mixer.music.stop()
        except:
            pass

        self.move = 0
        self.screen = screen
        self.menu = Map(screen)
        self.menu.set_highlight_color((255, 0, 0))
        self.menu.set_normal_color((255, 255, 255))
        self.menu.center_at(128, 104)
        self.bg = MAP
        self.clock = pygame.time.Clock()
        events = pygame.event.get()
        self.menu.update(events)
        self.menu.draw(self.screen, self.move)
        self.main_loop()

    def main_loop(self):
        while 1:
            self.clock.tick(30)
            events = pygame.event.get()
            self.menu.update(events)
            for e in events:
                if e.type == QUIT:
                    pygame.quit()
                    return
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    Menu(self.screen)
                    return

            if self.menu.option == 0:
                if self.move != -20:
                    if self.move > -20:
                        self.move -= 2
                    if self.move < -20:
                        self.move += 2

            if self.menu.option == 1:
                if self.move != -0:
                    if self.move > -0:
                        self.move -= 2
                    if self.move < -0:
                        self.move += 2


            if self.menu.option == 2:
                if self.move != -50:
                    if self.move > -50:
                        self.move -= 2
                    if self.move < -50:
                        self.move += 2

                
            if self.menu.option == 3:
                if self.move != -160:
                    if self.move > -160:
                        self.move -= 2
                    if self.move < -160:
                        self.move += 2


            if self.menu.option == 4:
                if self.move != -130:
                    if self.move > -130:
                        self.move -= 2
                    if self.move < -130:
                        self.move += 2


            if self.menu.option == 5:
                if self.move != -70:
                    if self.move > -70:
                        self.move -= 2
                    if self.move < -70:
                        self.move += 2

                
            self.screen.blit(self.bg, (self.move, 0))         
            
            self.menu.draw(self.screen, self.move)
            pygame.display.flip()


