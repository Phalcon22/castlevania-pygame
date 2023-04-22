import pygame, gamelib.main, os, errno

from gamelib.Loading import FONT32, mydocuments

class Main_menu:

    def __init__(self, *options):

        self.options = options
        self.x = 0
        self.y = 0
        self.font = FONT32
        self.option = 0
        self.width = 1
        self.color = [0, 0, 0]
        self.hcolor = [255, 0, 0]
        self.height = len(self.options)*self.font.get_height()
        for o in self.options:
            text = o[0]
            ren = self.font.render(text, 1, (0, 0, 0))
            if ren.get_width() > self.width:
                self.width = ren.get_width()

    def draw(self, surface):
        i=0
        for o in self.options:
            if i==self.option:
                clr = self.hcolor
            else:
                clr = self.color
            text = o[0]
            ren = self.font.render(text, 1, clr)
            if ren.get_width() > self.width:
                self.width = ren.get_width()
            surface.blit(ren, ((self.x+self.width/2) - ren.get_width()/2, self.y + i*(self.font.get_height()+4)))
            i+=1
            
    def update(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_DOWN:
                    self.option += 1
                if e.key == pygame.K_UP:
                    self.option -= 1
                if e.key == pygame.K_RETURN:
                    self.options[self.option][1]()
        if self.option > len(self.options)-1:
            self.option = 0
        if self.option < 0:
            self.option = len(self.options)-1

    def set_pos(self, x, y):     
        self.x = x
        self.y = y
        
    def set_font(self, font):
        self.font = font
        
    def set_highlight_color(self, color):
        self.hcolor = color
        
    def set_normal_color(self, color):
        self.color = color
        
    def center_at(self, x, y):
        self.x = x-(self.width/2)
        self.y = y-(self.height/2)


class Map:

    def __init__(self, screen):

        self.options = ["STAGE 01", lambda: gamelib.main.SelectLevel(screen, 1)],["STAGE 02", lambda: gamelib.main.SelectLevel(screen, 2)],["STAGE 03", lambda: gamelib.main.SelectLevel(screen, 3)],["STAGE 04", lambda: gamelib.main.SelectLevel(screen, 4)],["STAGE 05", lambda: gamelib.main.SelectLevel(screen, 5)],["STAGE 06", lambda: gamelib.main.SelectLevel(screen, 6)]
        self.x = 0
        self.y = 0
        self.font = FONT32
        self.option = 0
        self.width = 1
        self.color = [0, 0, 0]
        self.hcolor = [255, 0, 0]
        self.height = len(self.options)*self.font.get_height()
        
        self.block1 = pygame.Surface((14, 11))
        self.block2 = pygame.Surface((14, 11))
        self.block3 = pygame.Surface((14, 11))
        self.block4 = pygame.Surface((14, 11))
        self.block5 = pygame.Surface((14, 11))
        self.block6 = pygame.Surface((14, 11))
        
        self.list_block = [self.block1,self.block2,self.block3,self.block4,self.block5,self.block6]

    def draw(self, surface, move):
    
        i=0
        if i == self.option:
            self.block1.set_alpha(255)
            self.block1.fill((255,255,255))
        else:
            self.block1.set_alpha(0)
        surface.blit(self.block1, ((143 + move),111))
        
        i=1
        if i == self.option:
            self.block2.set_alpha(255)
            self.block2.fill((255,255,255))
        else:
            self.block2.set_alpha(0)
        surface.blit(self.block2, ((95 + move) ,79))
        
        i=2
        if i == self.option:
            self.block3.set_alpha(255)
            self.block3.fill((255,255,255))
        else:
            self.block3.set_alpha(0)
        surface.blit(self.block3, ((175 + move), 63))
        
        i=3
        if i == self.option:
            self.block4.set_alpha(255)
            self.block4.fill((255,255,255))
        else:
            self.block4.set_alpha(0)
        surface.blit(self.block4, ((294 + move), 95))
        
        i=4
        if i == self.option:
            self.block5.set_alpha(255)
            self.block5.fill((255,255,255))
        else:
            self.block5.set_alpha(0)
        surface.blit(self.block5, ((271 + move), 47))
        
        i=5
        if i == self.option:
            self.block6.set_alpha(255)
            self.block6.fill((255,255,255))
        else:
            self.block6.set_alpha(0)
        surface.blit(self.block6, ((180 + move), 23))
            
    def update(self, events):

        try:
            os.makedirs((mydocuments + "\\my games"))
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
                
        try:
            os.makedirs((mydocuments + "\\my games\\Castlevania"))
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
                
        try:
            os.makedirs((mydocuments + "\\my games\\Castlevania\\saves"))
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
    
        try:
            save_file = open((mydocuments + "\\my games\\Castlevania\\saves\\save.sav"), "r")
            niveau = int(save_file.read())
            save_file.close()
        except:
            save_file = open((mydocuments + "\\my games\\Castlevania\\saves\\save.sav"), "w+")
            save_file.write(str(1))
            save_file.close()
            niveau = 1
        
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    if self.option + 1 <= (niveau-1) and self.option + 1 < 6:
                        self.option += 1
                if e.key == pygame.K_LEFT:
                    if self.option - 1 >= 0:
                        self.option -= 1
                if e.key == pygame.K_RETURN:
                    self.options[self.option][1]()

    def set_pos(self, x, y):     
        self.x = x
        self.y = y
        
    def set_font(self, font):
        self.font = font
        
    def set_highlight_color(self, color):
        self.hcolor = color
        
    def set_normal_color(self, color):
        self.color = color
        
    def center_at(self, x, y):
        self.x = x-(self.width/2)
        self.y = y-(self.height/2)
