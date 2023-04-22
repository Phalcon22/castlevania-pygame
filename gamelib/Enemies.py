import pygame
from math import *
from gamelib.Constantes import *
from gamelib.Sprites import *

from gamelib.Loading import ZOMBIE, BLACKLEOPARD, BAT, FLAME, FISHMAN, BOSS1

class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.health = 1
        self.degat = 2
        self.points = 100
        self.nom = "zombie"
        self.movx = 0
        self.movy = 0.5
        self.walk_latency = 0
        self.contact = False
        self.image = ZOMBIE[0]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.phase = 0

        self.dying = False
        self.dying_state = 0
        self.death_phase = 0

        self.target = False
        self.reset = False
        self.reset_timer = 60

        self.hit_cooldown = 0


    def update(self, world_sprite, player):

        if self.hit_cooldown > 0:
            self.hit_cooldown -= 1

        if self.movy == 0.5:
            self.collide(0, self.movy, world_sprite)

        if self.health <= 0 and not self.dying and not self.reset:
            self.dying = True
            self.movx = 0
            self.dying_state = 1
            player.score += self.points

        if self.dying:
            self.death_phase += 1
            self.image = FLAME[self.dying_state]
            if self.death_phase == 5 or self.death_phase == 10 or self.death_phase == 15 or self.death_phase == 20:
                self.dying_state += 1
            if self.dying_state == 4:
                self.image = FLAME[4]
                self.reset = True
                self.dying = False
                
        if self.reset:
            self.reset_timer -= 1
            if self.reset_timer <= 0:
                if abs(self.x - player.rect.x) > 192:
                    self.__init__(self.x, self.y)
                    
        if self.target and not self.reset:
            if abs(self.rect.x - player.rect.x) > 192 and abs(self.x - player.rect.x) > 256:
                self.__init__(self.x, self.y)
            
        if not self.dying and self.target and not self.reset:

            if self.movx == -HORIZ_MOV_INCR:
                if self.phase < 8:
                    self.image = ZOMBIE[0]
                if self.phase >= 8:
                    self.image = ZOMBIE[1]
                    
            if self.movx == HORIZ_MOV_INCR:
                if self.phase < 8:
                    self.image = ZOMBIE[2]
                if self.phase >= 8:
                    self.image = ZOMBIE[3]
                    
            if self.phase == 16:
                self.phase = 0
            self.phase += 1
                
            if self.walk_latency == 2 or self.walk_latency == 3 or self.walk_latency == 1:
                self.walk_latency -= 1
            if self.walk_latency == 0 or self.walk_latency == 1:
                if self.walk_latency == 0:
                    self.walk_latency = 3
                self.rect.right += self.movx
            self.collide(self.movx, 0, world_sprite)

            if not self.contact:
                self.movy += 1
                if self.movy > 10:
                    self.movy = 10
                self.rect.top += self.movy  

            self.collide(0, self.movy, world_sprite)

        if abs(self.rect.x - player.rect.x) <= 384 and not self.target:
            self.target = True
            if self.rect.x < player.rect.x:
                self.movx = HORIZ_MOV_INCR
            if self.rect.x >= player.rect.x:
                self.movx = -HORIZ_MOV_INCR

    def collide(self, movx, movy, world_sprite):
        self.contact = False
        for o in world_sprite:
            if self.rect.colliderect(o):
                if o.nom == "obstacle" or o.nom == "platform" or o.nom == "stairsspecial":
                    if movx == HORIZ_MOV_INCR:
                        self.rect.right = o.rect.left
                        self.movx = -HORIZ_MOV_INCR
                    if movx == -HORIZ_MOV_INCR:
                        self.rect.left = o.rect.right
                        self.movx = HORIZ_MOV_INCR
                    if movy > 0:
                        self.rect.bottom = o.rect.top
                        self.movy = 0
                        self.contact = True

    def get_hit(self, degat):
        self.health -= degat
        self.hit_cooldown = 9


class Leopard(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.health = 1
        self.degat = 2
        self.points = 200
        self.nom = "leopard"
        self.movx = 0
        self.movy = 0.5
        self.contact = False
        self.jump_mode = False
        self.jumped = False
        self.x = x
        self.y = y
        
        self.phase = 0

        self.dying = False
        self.dying_state = 0
        self.death_phase = 0

        self.target = False
        self.reset = False
        self.reset_timer = 60
        self.latency = 0

        self.image = BLACKLEOPARD[5]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.hit_cooldown = 0


    def update(self, world_sprite, player):

        if self.hit_cooldown > 0:
            self.hit_cooldown -= 1

        if self.movy == 0.5:
            self.collide(world_sprite)

        self.latency +=1
        if self.latency == 3: self.latency = 0

        if self.health <= 0 and not self.dying and not self.reset:
            self.dying = True
            self.movx = 0
            self.dying_state = 1
            player.score += self.points

        if self.dying:
            self.death_phase += 1
            self.image = FLAME[self.dying_state]
            if self.death_phase == 5 or self.death_phase == 10 or self.death_phase == 15 or self.death_phase == 20:
                self.dying_state += 1
            if self.dying_state == 4:
                self.image = FLAME[4]
                self.reset = True
                self.dying = False
                
        if self.reset:
            self.reset_timer -= 1
            if self.reset_timer <= 0:
                if abs(self.x - player.rect.x) > 128:
                    self.__init__(self.x, self.y)
                    
        if self.target and not self.reset:
            if abs(self.rect.x - player.rect.x) > 192 and abs(self.x - player.rect.x) > 128:
                self.__init__(self.x, self.y)
            
            
        if not self.dying and self.target and not self.reset:
            if self.movx < 0:
                if not self.jump_mode:
                    if self.phase < 8:
                        self.image = BLACKLEOPARD[0]
                    if self.phase >= 8:
                        self.image = BLACKLEOPARD[1]
                if self.jump_mode:
                    self.image = BLACKLEOPARD[6]
                        
            if self.movx > 0:
                if not self.jump_mode:
                    if self.phase < 8:
                        self.image = BLACKLEOPARD[2]
                    if self.phase >= 8:
                        self.image = BLACKLEOPARD[3]
                if self.jump_mode:
                    self.image = BLACKLEOPARD[7]
                    
            if self.phase == 16:
                self.phase = 0
            self.phase += 1

            if (self.latency == 0 or self.latency == 1) or self.jump_mode:
                self.rect.right += self.movx

            if not self.contact:
                self.movy += 0.25
                if self.movy > 10:
                    self.movy = 10
                self.rect.top += self.movy

            self.collide(world_sprite)

            if not self.jumped:
                contact = False
                self.rect.x -= self.rect.width
                self.rect.y += 8
                for o in world_sprite:
                    if self.rect.colliderect(o):
                        if o.nom == "obstacle" or o.nom == "platform" or o.nom == "stairsspecial":
                            contact = True
                self.rect.x += self.rect.width
                self.rect.y -= 8
                if not contact:
                    self.jump()
                    self.movx = self.movx*2

        if abs(self.rect.x - player.rect.x) <= 45 and not self.target:
            self.target = True
            if self.rect.x < player.rect.x:
                self.movx = HORIZ_MOV_INCR*2
            if self.rect.x >= player.rect.x:
                self.movx = -HORIZ_MOV_INCR*2

    def jump(self):
        self.movy = -1
        self.jump_mode = True
        self.jumped = True

    def collide(self, world_sprite):
        self.contact = False
        for o in world_sprite:
            if self.rect.colliderect(o):
                if o.nom == "obstacle" or o.nom == "platform" or o.nom == "stairsspecial":
                    if self.movy >= 0 and not self.jump_mode:
                        self.rect.bottom = o.rect.top
                        self.movy = 0
                        self.contact = True
                    if self.movy > 3 and self.jump_mode:
                        if self.jumped:
                            self.jump_mode = False
                            self.movx = -self.movx/2

    def get_hit(self, degat):
        self.health -= degat
        self.hit_cooldown = 9

                     
                     
class Bat(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.health = 1
        self.degat = 2
        self.points = 200
        self.nom = "bat"
        self.movx = 0
        self.movy = 0
        self.walk_latency = 0
        self.image = BAT[0]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        
        self.phase = 0
        
        self.go_up = 0
        self.go_down = 20

        self.dying = False
        self.dying_state = 0
        self.death_phase = 0

        self.target = False
        self.reset = False
        self.reset_timer = 60

        self.hit_cooldown = 0


    def update(self, world_sprite, player):

        if self.hit_cooldown > 0:
            self.hit_cooldown -= 1
        
        if self.health <= 0 and not self.dying and not self.reset:
            self.dying = True
            self.movx = 0
            self.dying_state = 1
            player.score += self.points

        if self.dying:
            self.death_phase += 1
            self.image = FLAME[self.dying_state]
            if self.death_phase == 5 or self.death_phase == 10 or self.death_phase == 15 or self.death_phase == 20:
                self.dying_state += 1
            if self.dying_state == 4:
                self.image = FLAME[4]
                self.reset = True
                self.dying = False
                
        if self.reset:
            self.reset_timer -= 1
            if self.reset_timer <= 0:
                if abs(self.x - player.rect.x) > 128:
                    self.__init__(self.x, self.y)
                    
        if self.target and not self.reset:
            if abs(self.rect.x - player.rect.x) > 192 and abs(self.x - player.rect.x) > 128:
                self.__init__(self.x, self.y)
            
        if not self.dying and self.target and not self.reset:  
            self.rect.right += self.movx
            if self.walk_latency == 0 or self.walk_latency == 1:
                self.walk_latency = 2

                if self.movx == -HORIZ_MOV_INCR:
                    if self.phase < 8:
                        self.image = BAT[0]
                    if self.phase >= 8:
                        self.image = BAT[1]
                        
                if self.movx == HORIZ_MOV_INCR:
                    if self.phase < 8:
                        self.image = BAT[2]
                    if self.phase >= 8:
                        self.image = BAT[3]
                        
                if self.phase == 16:
                    self.phase = 0
                self.phase += 1

                if self.target:
                    if self.go_up > 0:
                        self.go_up -= 1
                        self.rect.y -= 1
                        if self.go_up == 0:
                            self.go_down = 20
                    if self.go_down > 0:
                        self.go_down -= 1
                        self.rect.y += 1
                        if self.go_down == 0:
                            self.go_up = 20
                           
            else: self.walk_latency -= 1

        if abs(self.rect.x - player.rect.x) <= 156 and not self.target:
            self.target = True
            if self.rect.x < player.rect.x:
                self.movx = HORIZ_MOV_INCR
            if self.rect.x >= player.rect.x:
                self.movx = -HORIZ_MOV_INCR
                
    def get_hit(self, degat):
        self.health -= degat
        self.hit_cooldown = 9



class Fishman(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.health = 1
        self.degat = 2
        self.points = 200
        self.nom = "bat"
        self.movx = 0
        self.movy = 0
        self.walk_latency = 0
        
        self.image = FISHMAN[0]
        
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        
        self.phase = 0

        self.dying = False
        self.dying_state = 0
        self.death_phase = 0

        self.target = False

        self.direction = -HORIZ_MOV_INCR

class Boss1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.health = 1
        self.degat = 2
        self.points = 3000
        self.nom = "boss1"
        self.movx = 0
        self.movy = 0
        self.image = BOSS1[0]
        self.rect = self.image.get_rect()
        self.image = BOSS1[2]
        self.frame = 12

        self.rect.x = x
        self.rect.y = y

        self.dying = False
        self.dying_state = 0
        self.death_phase = 0

        self.activate = False
        self.activated = False

        self.attack = False
        self.timer = 240
        self.transition = True
        self.action = False
        self.wait = False
        self.transiting = False

        self.hit_cooldown = 0

    def update(self, player, camera):

        if self.hit_cooldown > 0:
            self.hit_cooldown -= 1
        
        if self.activate and not self.activated:
            self.image = BOSS1[0]
            self.activated = True

        if self.frame == 0:
            self.frame = 12
            if self.image == BOSS1[0]:
                self.image = BOSS1[1]
            elif self.image == BOSS1[1]:
                self.image = BOSS1[0]
        else: self.frame -= 1
        
        if self.health <= 0 and not self.dying:
            self.dying = True
            self.movx = 0
            self.dying_state = 1
            player.score += self.points

        if self.dying:
            self.death_phase += 1
            self.image = FLAME[self.dying_state]
            if self.death_phase == 5 or self.death_phase == 10 or self.death_phase == 15 or self.death_phase == 20:
                self.dying_state += 1
            if self.dying_state == 4:
                self.image = FLAME[4]
                self.dying = False
            

        if self.activated:

            if self.transition:
                if self.rect.y - camera.rect.y > 110:
                    self.movy = -1
                elif self.rect.y - camera.rect.y < 110:
                    self.movy = 1
                    
                if player.rect.centerx - self.rect.centerx < 0:
                    self.movx = 1
                elif player.rect.centerx - self.rect.centerx > 0:
                    self.movx = -1
                self.transiting = True
                self.transition = False
                self.timer = 60
                
            if self.transiting:
                self.timer -= 1
                self.rect.x += self.movx
                self.rect.y += self.movy
                self.rect.clamp_ip(camera)
                if self.timer == 0:
                    self.transiting = False
                    self.attack = True
                    self.timer = 60
                        
            if self.attack:
                self.movx = -(self.rect.x - player.rect.x)/30
                if self.movx < -4:
                    self.movx = -4
                if self.movx > 4:
                    self.movx = 4
                self.movy = int((player.rect.centery - self.rect.centery+20)/40)
                if self.movy == 0 and (player.rect.centery - self.rect.centery) > 0:
                    self.movy = 1
                if self.movy == 0 and (player.rect.centery - self.rect.centery) < 0:
                    self.movy = -1
                self.attack = False
                self.wait = True
                self.timer = 120

            if self.wait:
                self.timer -= 1
                if self.timer == 0:
                    self.timer = 60
                    self.wait = False
                    self.action = True
                
            if self.action:
                self.timer -= 1
                self.rect.x += self.movx
                self.rect.y += self.movy
                self.rect.clamp_ip(camera)

                if (self.rect.left == camera.rect.left) or (self.rect.right == camera.rect.right):
                    self.movx = - self.movx
                
                
                if self.timer == 0:
                    self.action = False
                    self.transition = True

    def fire(self):
        pass

    def get_hit(self, degat):
        if self.hit_cooldown == 0:
            self.health -= degat
            self.hit_cooldown = 9

    def drop(self, dynamic_items_sprites, all_sprite):
        dynamic_items_sprites.add(Consommable(self.rect.x, self.rect.y, "magicalcrystal"))
        all_sprite.add(dynamic_items_sprites)
