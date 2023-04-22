import pygame
from pygame.locals import *

from gamelib.Sprites import *
from gamelib.Constantes import *
from gamelib.Camera import *
from gamelib.Gabriel_properties import *
from gamelib.Loading import RUN_LEFT, RUN_RIGHT, WHIP_LEFT, WHIP_RIGHT, EXPERT_WHIP_LEFT, EXPERT_WHIP_RIGHT, HURT_LEFT, HURT_RIGHT, STAIRS_LEFT_UP, STAIRS_LEFT_DOWN, STAIRS_RIGHT_UP, STAIRS_RIGHT_DOWN, CROUCH_LEFT, CROUCH_RIGHT, ATTACK_SOUND, BELMONTHURT_SOUND, ITEMGRAB_SOUND, WEAPONGRAB_SOUND  
from gamelib.Weapon import *

class Belmont(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.nom = "belmont"
        self.movy = 0
        self.movx = 0
        self.jump_mode = False
        self.chute_libre = True
        self.crouch = False

        self.image = RUN_RIGHT[0]
        self.rect = self.image.get_rect()

        self.whip_left = WHIP_LEFT
        self.whip_right = WHIP_RIGHT

        self.direction = "right"
        self.rect.x = x
        self.rect.y = y
        self.frame = 0
        self.frame_stairs = 0

        self.climbx = self.rect.x

        self.health = 16
        self.hit_count = 0
        self.win = 0
        self.game_over = 0

        self.attack_mode = False
        self.attack_cooldown = 0
        self.attack_phase = 0
        
        self.secondary_weapon = None
        self.secondary_cooldown = 0
        self.ammo = 5

        self.hurt = False
        
        self.score = 0

        self.climbing_left = False
        self.climbing_right = False
        self.goto_climb = False
        self.climb_cooldown = 0


        self.whip = "basic"

    def update(self, up, left, right, down, all_sprite, camera, game):

        if self.secondary_cooldown > 0:
            self.secondary_cooldown -= 1

        if self.whip == "expert":
            self.whip_left = EXPERT_WHIP_LEFT
            self.whip_right = EXPERT_WHIP_RIGHT

        self.rect.clamp_ip(camera)
        
        if self.hit_count > 0:
            self.hit_count -= 1
            
        if self.attack_mode: self.test_attack(all_sprite)
        self.test_gameover(camera)
        
        self.pos_update(up, left, right, down, all_sprite)
            
        if not self.attack_mode:
            self.animation_update(up, left, right, down)

        self.start_boss(all_sprite, game)


    def determine_climbing(self, all_sprite, up, down):
        for o in all_sprite:
            if self.rect.colliderect(o):
                
                if o.nom == "stairs_up_left" and up:

                    self.goto_climb = True

                    if self.rect.centerx != o.rect.centerx :
                        if self.rect.centerx > o.rect.centerx :
                            self.direction = "left"
                            self.rect.centerx -= 1
                        if self.rect.centerx < o.rect.centerx :
                            self.direction = "right"
                            self.rect.centerx += 1
                    if self.rect.centerx == o.rect.centerx :
                        self.climbing_left = True
                        self.goto_climb = False
                        self.climbx = self.rect.right
                        if self.direction == "left":
                            self.direction = "right"
                        
                if o.nom == "stairs_down_left" and down:

                    self.goto_climb = True

                    if self.rect.right != o.rect.centerx :
                        if self.rect.right > o.rect.centerx :
                            self.direction = "left"
                            self.rect.right -= 1
                        if self.rect.right < o.rect.centerx :
                            self.direction = "right"
                            self.rect.right += 1
                    if self.rect.right == o.rect.centerx :
                        self.climbing_left = True
                        self.goto_climb = False
                        self.climbx = self.rect.x
                        if self.direction == "right":
                            self.direction = "left"
                    
                        
                if o.nom == "stairs_up_right" and up:

                    self.goto_climb = True

                    if self.rect.centerx != o.rect.centerx :
                        if self.rect.centerx > o.rect.centerx :
                            self.direction = "right"
                            self.rect.centerx -= 1
                        if self.rect.centerx < o.rect.centerx :
                            self.direction = "left"
                            self.rect.centerx += 1
                    if self.rect.centerx == o.rect.centerx :
                        self.climbing_right = True
                        self.goto_climb = False
                        self.climbx = self.rect.right
                        if self.direction == "right":
                            self.direction = "left"

                    
                if o.nom == "stairs_down_right" and down:

                    self.goto_climb = True

                    if self.rect.left != o.rect.centerx :
                        if self.rect.left > o.rect.centerx :
                            self.direction = "left"
                            self.rect.left -= 1
                        if self.rect.left < o.rect.centerx :
                            self.direction = "right"
                            self.rect.left += 1
                    if self.rect.left == o.rect.centerx :
                        self.climbing_right = True
                        self.goto_climb = False
                        self.climbx = self.rect.right
                        if self.direction == "left":
                            self.direction = "right"
        

    def climb_collide(self, all_sprite, up, down):
        
        self.climb_cooldown = 2

        if self.climbing_left:
            if up:
                self.rect.x += 1
                self.rect.y += -1

            if down:
                self.rect.x += -1
                self.rect.y += 1

        if self.climbing_right:
            if up:
                self.rect.x += -1
                self.rect.y += -1
                        
            if down:
                self.rect.x += 1
                self.rect.y += 1

        if (down and self.climbing_left) or (up and self.climbing_right):
            if self.direction == "right":
                self.direction = "left" 

        if (up and self.climbing_left) or (down and self.climbing_right):
            if self.direction == "left":
                self.direction = "right"
            
        for o in all_sprite:
            if self.rect.colliderect(o):
                
                if self.climbing_left:
                    if o.nom == "obstacle" or o.nom == "platform":
                        if (down and self.rect.right < self.climbx) or up:
                            self.climbing_left = False

                if self.climbing_right:
                    
                    if o.nom == "obstacle" or o.nom == "platform":
                        if o.rect.centery > self.rect.centery:
                            if (down and self.rect.left > self.climbx) or up:
                                self.climbing_right = False
                        

        
    def test_attack(self, all_sprite):
    
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
            
            if self.attack_cooldown <= 23 and self.attack_cooldown > 18:
                self.attack_phase = 2          
                if self.direction == "left":
                    self.image = self.whip_left[1]
                    
            if self.attack_cooldown <= 18 and self.attack_cooldown > 11:
                self.attack_phase = 3                 
                if self.direction == "left":
                    self.image = self.whip_left[2]
                    
            if self.attack_cooldown <= 11 and self.attack_cooldown > 2:
                self.attack_phase = 4
                if self.direction == "right":
                    self.image = self.whip_right[3]
                    
            if self.attack_cooldown == 2:
                self.attack_phase = 5
                if self.direction == "right":
                    self.image = self.whip_right[4]
                if self.direction == "left":
                    self.image = self.whip_left[4]

            if self.attack_cooldown == 1:
                self.attack_phase = 5
                if self.direction == "right":
                    self.image = self.whip_right[0]
                if self.direction == "left":
                    self.image = self.whip_left[0]
                
            
        if self.attack_cooldown == 0:
            self.attack_mode = False
            self.attack_phase = 0

    def test_gameover(self, camera):
    
        if self.rect.left > camera.world_rect.width or self.rect.right < -50 or self.rect.top > camera.world_rect.bottom:
            self.game_over = 1
            
        if self.health <= 0:
            self.game_over = 1
        
    def pos_update(self, up, left, right, down, all_sprite):

        if self.goto_climb:
            self.determine_climbing(all_sprite, up, down)
            
        if self.climbing_left or self.climbing_right:
            if self.climb_cooldown == 0:
                if up or down:
                    self.climb_collide(all_sprite, up, down)

            if self.climb_cooldown > 0:
                self.climb_cooldown -= 1


        if not self.climbing_left and not self.climbing_right and not self.goto_climb:
            if not down:         
                if (left or right) and not self.crouch and not self.jump_mode and not self.attack_mode and not self.hurt:
                    if right:
                        self.movx = HORIZ_MOV_INCR
                        self.direction = "right"
                    if left:
                        self.movx = -HORIZ_MOV_INCR
                        self.direction = "left"
                        
                if (left or right) and not self.attack_mode and not self.crouch: 
                    self.rect.x += self.movx    
                    self.collide(all_sprite, "x")

                if self.crouch and not self.attack_mode and not self.jump_mode:
                    self.crouch = False
                    self.rect.height = walk_left_rect.height
                
                if not self.jump_mode:
                    if self.chute_libre:
                        self.movy = 7
                    if not self.chute_libre:
                        self.movy = 1 
                
            if down and not self.attack_mode and not self.jump_mode and not self.chute_libre:
                self.crouch = True
                self.movx = 0
                self.movy = self.rect.height - crouch_left_rect.height + 1
                self.rect.height = crouch_left_rect.height
                
            if self.jump_mode:
                self.movy += 0.2
                    
            self.rect.y += self.movy
            self.collide(all_sprite, "y")

    def animation_update(self, up, left, right, down):
    
        if self.hurt:
            if self.movx == 1.1:
                self.image = HURT_LEFT
            if self.movx == -1.1:
                self.image = HURT_RIGHT
    
        if not self.hurt:
            if (not self.chute_libre and (right or left or down)) or ((self.climbing_left or self.climbing_right) and (up or down)) or self.goto_climb:
            
                if (not self.jump_mode and not down and not (self.climbing_left or self.climbing_right)) or ((self.climbing_left or self.climbing_right) and (up or down) and self.climb_cooldown == 0) or self.goto_climb:
                    self.frame += 1
                    self.frame_stairs +=1
                    if self.frame == 24: self.frame = 0
                    if self.frame_stairs == 12: self.frame_stairs = 0
                    
                    if self.frame <= 6:
                        walk_frame = 0
                    if (self.frame > 6 and self.frame <= 12) or (self.frame > 18 and self.frame <= 24):
                        walk_frame = 1
                    if (self.frame > 12 and self.frame <= 18):
                        walk_frame = 2

                    if self.frame_stairs <= 6:
                        stairs_frame = 0
                    if self.frame_stairs > 6:
                        stairs_frame = 1

                    if not self.climbing_left and not self.climbing_right:
                        if self.direction == "right":
                            self.image = RUN_RIGHT[walk_frame]
                        if self.direction == "left":
                            self.image = RUN_LEFT[walk_frame]

                    if self.climbing_left:
                        if up:
                            self.image = STAIRS_RIGHT_UP[stairs_frame]
                        if down:
                            self.image = STAIRS_LEFT_DOWN[stairs_frame]

                    if self.climbing_right:
                        if down:
                            self.image = STAIRS_RIGHT_DOWN[stairs_frame]
                        if up:
                            self.image = STAIRS_LEFT_UP[stairs_frame]
  
                        
                if (self.jump_mode or down) and not self.climbing_left and not self.climbing_right and not self.goto_climb:
                    if self.direction == "right":
                        self.image = CROUCH_RIGHT
                    if self.direction == "left":
                        self.image = CROUCH_LEFT
                    
            if ((self.chute_libre and not self.jump_mode) or (not self.chute_libre and self.crouch)) and not down or (not self.chute_libre and not right and not left and not down and not self.jump_mode) and not self.climbing_left and not self.climbing_right:
                if self.direction == "right":
                    self.image = RUN_RIGHT[0]
                if self.direction == "left":
                    self.image = RUN_LEFT[0] 
                     

    def jump(self, all_sprite):
        if not self.chute_libre and not self.hurt:
            self.movy = -2.95
            self.rect.y += self.movy
            self.chute_libre = True
            self.jump_mode = True
            self.collide(all_sprite, "y")
            if self.direction == "right":
                self.image = CROUCH_RIGHT
            if self.direction == "left":
                self.image = CROUCH_LEFT


    def stop(self):
        if not self.jump_mode:
            self.movx = 0
        elif self.jump_mode:
            self.movy = 0
            self.jump_mode = False


    def collide(self, all_sprite, orientation):
        contact = False
        movy = self.movy
        for o in all_sprite:
            if self.rect.colliderect(o):

                if o.nom == "platform" or o.nom == "stairsspecial":
                    if orientation == "x": 
                        if not self.chute_libre:
                            if self.movx > 0:
                                self.rect.right = o.rect.left
                                self.movx = 0 
                        
                            if self.movx < 0:
                                self.rect.left = o.rect.right
                                self.movx = 0 
                                
                    if orientation == "y":
                        if self.movy >= 0:
                            if self.rect.bottom < o.rect.centery+6:
                                contact = True
                                self.chute_libre = False
                                self.jump_mode = False
                                self.movy = 0
                                self.rect.bottom = o.rect.top
                                if self.hurt:
                                    self.hurt = False
                                    
                    
                if o.nom == "obstacle":
                    if orientation == "x": 
                        if self.movx > 0:
                            self.rect.right = o.rect.left
                            self.movx = 0 
                            
                        if self.movx < 0:
                            self.rect.left = o.rect.right
                            self.movx = 0 
                        
                    if orientation == "y":
                        if self.jump_mode:
                            self.jump_mode = False
                        
                        if self.movy >= 0:
                            contact = True
                            self.chute_libre = False
                            self.movy = 0
                            self.rect.bottom = o.rect.top
                            if self.hurt:
                                self.hurt = False
                            
                if o.nom == "zombie" or o.nom == "leopard" or o.nom == "bat":
                    if self.hit_count == 0 and not o.dying and not o.reset:
                        if o.rect.centerx > self.rect.centerx:
                            self.hit(o.degat, all_sprite, "right")
                        elif o.rect.centerx < self.rect.centerx:
                            self.hit(o.degat, all_sprite, "left")

                if o.nom == "boss1":
                    if self.hit_count == 0 and not o.dying:
                        if o.rect.centerx > self.rect.centerx:
                            self.hit(o.degat, all_sprite, "right")
                        elif o.rect.centerx < self.rect.centerx:
                            self.hit(o.degat, all_sprite, "left")

                if o.nom == "consommable":
                    if o.contact:
                        if o.dropped == "magicalcrystal":
                            self.win = 1
                        if o.dropped == "large_candle":
                            ITEMGRAB_SOUND.play()
                            self.ammo += 5
                        if o.dropped == "candle":
                            ITEMGRAB_SOUND.play()
                            self.ammo += 1
                        if o.dropped == "large_candle_whip":
                            WEAPONGRAB_SOUND.play()
                            if self.whip == "basic":
                                self.whip = "advanced"
                            elif self.whip == "advanced":
                                self.whip = "expert"
                        if o.dropped == "large_candle_dagger":
                            WEAPONGRAB_SOUND.play()
                            self.secondary_weapon = "dagger"
                        if o.dropped == "candle_axe":
                            WEAPONGRAB_SOUND.play()
                            self.secondary_weapon = "axe"
                        o.kill()
    
                                
        if not contact and orientation == "y" and movy > 0:
            if not self.chute_libre:
                self.chute_libre = True
                self.movy = 0.8
            
    def hit(self, degats, all_sprite, direction):
        self.health -= degats
        self.hit_count = 240
        BELMONTHURT_SOUND.play()
        if not self.climbing_left and not self.climbing_right:
            if self.crouch:
                self.crouch = False
                self.rect.height = walk_left_rect.height
                self.collide(all_sprite, "y")
            self.hurt = True
            self.attack_mode = False
            
            self.movy = -2
            self.movx = 0
            self.rect.y += self.movy
            self.chute_libre = True
            self.jump_mode = True
            self.collide(all_sprite, "y")
            
            if direction == "right":
                self.movx = -1.1
                
            if direction == "left":
                self.movx = 1.1

    def attack(self):
        if not self.attack_mode:
            ATTACK_SOUND.play()
            self.attack_phase = 1
            self.attack_mode = True
            self.attack_cooldown = 24
            if self.direction == "right":
                self.image = self.whip_right[0]
                
            if self.direction == "left":
                self.image = self.whip_left[0]

    def secondary_attack(self, secondary_weapons_sprites, all_sprite):
        if not self.attack_mode and self.secondary_cooldown == 0:
            self.secondary_cooldown = 40
            if self.secondary_weapon == "dagger" and self.ammo > 0:
                if self.direction == "right":
                    secondary_weapons_sprites.add(ThrewDagger(self.rect.right, self.rect.centery, "right"))
                if self.direction == "left":
                    secondary_weapons_sprites.add(ThrewDagger(self.rect.left, self.rect.centery, "left"))
                    
                all_sprite.add(secondary_weapons_sprites)
                self.ammo -= 1

            if self.secondary_weapon == "axe" and self.ammo > 0:
                secondary_weapons_sprites.add(ThrewAxe(self.rect.centerx, self.rect.top, self.direction))
                all_sprite.add(secondary_weapons_sprites)
                self.ammo -= 1   

    def start_boss(self, all_sprite, game):
        for o in all_sprite:
            if self.rect.colliderect(o):
                if o.nom == "startboss":
                    if not game.level.Boss.activate:
                        pygame.mixer.music.load("data/musics/Boss.ogg")
                        pygame.mixer.music.play(-1)
                    game.level.Boss.activate = True
    
