import pygame

from win32com.shell import shell, shellcon
mydocuments = shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, 0, 0)



pygame.init()

FONT = pygame.font.Font(("data/fonts/font.ttf"), 16)
FONT32 = pygame.font.Font(("data/fonts/font.ttf"), 32)

pygame.display.set_mode((1,1))

ICON = pygame.image.load("Icon.ico")

"""BELMONT"""

CROUCH_LEFT = pygame.image.load('data/assets/Belmont/left/Belmont_Crouch.png').convert_alpha()
CROUCH_RIGHT = pygame.image.load('data/assets/Belmont/right/Belmont_Crouch.png').convert_alpha() 

STAIRS_LEFT_UP1 = pygame.image.load("data/assets/Belmont/left/Stairs_Up_0.gif").convert_alpha()
STAIRS_LEFT_UP2 = pygame.image.load("data/assets/Belmont/left/Stairs_Up_1.gif").convert_alpha()
STAIRS_LEFT_UP = [STAIRS_LEFT_UP1, STAIRS_LEFT_UP2]
STAIRS_LEFT_DOWN1 = pygame.image.load("data/assets/Belmont/left/Stairs_Down_0.gif").convert_alpha()
STAIRS_LEFT_DOWN2 = pygame.image.load("data/assets/Belmont/left/Stairs_Down_1.gif").convert_alpha()
STAIRS_LEFT_DOWN = [STAIRS_LEFT_DOWN1, STAIRS_LEFT_DOWN2]

STAIRS_RIGHT_UP1 = pygame.image.load("data/assets/Belmont/right/Stairs_Up_0.gif").convert_alpha()
STAIRS_RIGHT_UP2 = pygame.image.load("data/assets/Belmont/right/Stairs_Up_1.gif").convert_alpha()
STAIRS_RIGHT_UP = [STAIRS_RIGHT_UP1, STAIRS_RIGHT_UP2]
STAIRS_RIGHT_DOWN1 = pygame.image.load("data/assets/Belmont/right/Stairs_Down_0.gif").convert_alpha()
STAIRS_RIGHT_DOWN2 = pygame.image.load("data/assets/Belmont/right/Stairs_Down_1.gif").convert_alpha()
STAIRS_RIGHT_DOWN = [STAIRS_RIGHT_DOWN1, STAIRS_RIGHT_DOWN2]


HURT_LEFT = pygame.image.load("data/assets/Belmont/left/Belmont_Hurt.gif").convert_alpha()
HURT_RIGHT = pygame.image.load("data/assets/Belmont/right/Belmont_Hurt.gif").convert_alpha()

RUN_LEFT1 = pygame.image.load("data/assets/Belmont/left/Belmont_Walk_01.gif").convert_alpha()
RUN_LEFT2 = pygame.image.load("data/assets/Belmont/left/Belmont_Walk_02.gif").convert_alpha()
RUN_LEFT3 = pygame.image.load("data/assets/Belmont/left/Belmont_Walk_03.gif").convert_alpha()
RUN_LEFT = [RUN_LEFT1, RUN_LEFT2, RUN_LEFT3]

RUN_RIGHT1 = pygame.image.load("data/assets/Belmont/right/Belmont_Walk_01.gif").convert_alpha()
RUN_RIGHT2 = pygame.image.load("data/assets/Belmont/right/Belmont_Walk_02.gif").convert_alpha()
RUN_RIGHT3 = pygame.image.load("data/assets/Belmont/right/Belmont_Walk_03.gif").convert_alpha()
RUN_RIGHT = [RUN_RIGHT1, RUN_RIGHT2, RUN_RIGHT3]

HP0 = pygame.image.load("data/assets/UI/Life/0.png").convert()
HP1 = pygame.image.load("data/assets/UI/Life/1.png").convert()
HP2 = pygame.image.load("data/assets/UI/Life/2.png").convert()
HP3 = pygame.image.load("data/assets/UI/Life/3.png").convert()
HP4 = pygame.image.load("data/assets/UI/Life/4.png").convert()
HP5 = pygame.image.load("data/assets/UI/Life/5.png").convert()
HP6 = pygame.image.load("data/assets/UI/Life/6.png").convert()
HP7 = pygame.image.load("data/assets/UI/Life/7.png").convert()
HP8 = pygame.image.load("data/assets/UI/Life/8.png").convert()
HP9 = pygame.image.load("data/assets/UI/Life/9.png").convert()
HP10 = pygame.image.load("data/assets/UI/Life/10.png").convert()
HP11 = pygame.image.load("data/assets/UI/Life/11.png").convert()
HP12 = pygame.image.load("data/assets/UI/Life/12.png").convert()
HP13 = pygame.image.load("data/assets/UI/Life/13.png").convert()
HP14 = pygame.image.load("data/assets/UI/Life/14.png").convert()
HP15 = pygame.image.load("data/assets/UI/Life/15.png").convert()
HP16 = pygame.image.load("data/assets/UI/Life/16.png").convert()

HP = [HP0, HP1, HP2, HP3, HP4, HP5, HP6, HP7, HP8, HP9, HP10, HP11, HP12, HP13, HP14, HP15, HP16]

HPBOSS0 = pygame.image.load("data/assets/UI/Boss_life/0.png").convert()
HPBOSS1 = pygame.image.load("data/assets/UI/Boss_life/1.png").convert()
HPBOSS2 = pygame.image.load("data/assets/UI/Boss_life/2.png").convert()
HPBOSS3 = pygame.image.load("data/assets/UI/Boss_life/3.png").convert()
HPBOSS4 = pygame.image.load("data/assets/UI/Boss_life/4.png").convert()
HPBOSS5 = pygame.image.load("data/assets/UI/Boss_life/5.png").convert()
HPBOSS6 = pygame.image.load("data/assets/UI/Boss_life/6.png").convert()
HPBOSS7 = pygame.image.load("data/assets/UI/Boss_life/7.png").convert()
HPBOSS8 = pygame.image.load("data/assets/UI/Boss_life/8.png").convert()
HPBOSS9 = pygame.image.load("data/assets/UI/Boss_life/9.png").convert()
HPBOSS10 = pygame.image.load("data/assets/UI/Boss_life/10.png").convert()
HPBOSS11 = pygame.image.load("data/assets/UI/Boss_life/11.png").convert()
HPBOSS12 = pygame.image.load("data/assets/UI/Boss_life/12.png").convert()
HPBOSS13 = pygame.image.load("data/assets/UI/Boss_life/13.png").convert()
HPBOSS14 = pygame.image.load("data/assets/UI/Boss_life/14.png").convert()
HPBOSS15 = pygame.image.load("data/assets/UI/Boss_life/15.png").convert()
HPBOSS16 = pygame.image.load("data/assets/UI/Boss_life/16.png").convert()

HPBOSS = [HPBOSS0, HPBOSS1, HPBOSS2, HPBOSS3, HPBOSS4, HPBOSS5, HPBOSS6, HPBOSS7, HPBOSS8, HPBOSS9, HPBOSS10, HPBOSS11, HPBOSS12, HPBOSS13, HPBOSS14, HPBOSS15, HPBOSS16]

WHIP_RIGHT1 = pygame.image.load("data/assets/Belmont/right/attack/frame-1.gif").convert_alpha()
WHIP_RIGHT2 = pygame.image.load("data/assets/Belmont/right/attack/frame-2.gif").convert_alpha()
WHIP_RIGHT3 = pygame.image.load("data/assets/Belmont/right/attack/frame-3.gif").convert_alpha()
WHIP_RIGHT4 = pygame.image.load("data/assets/Belmont/right/attack/frame-4.gif").convert_alpha()
WHIP_RIGHT5 = pygame.image.load("data/assets/Belmont/right/attack/frame-5.gif").convert_alpha()

WHIP_RIGHT = [WHIP_RIGHT1, WHIP_RIGHT2, WHIP_RIGHT3, WHIP_RIGHT4, WHIP_RIGHT5]

WHIP_LEFT1 = pygame.image.load("data/assets/Belmont/left/attack/frame-1.gif").convert_alpha()
WHIP_LEFT2 = pygame.image.load("data/assets/Belmont/left/attack/frame-2.gif").convert_alpha()
WHIP_LEFT3 = pygame.image.load("data/assets/Belmont/left/attack/frame-3.gif").convert_alpha()
WHIP_LEFT4 = pygame.image.load("data/assets/Belmont/left/attack/frame-4.gif").convert_alpha()
WHIP_LEFT5 = pygame.image.load("data/assets/Belmont/left/attack/frame-5.gif").convert_alpha()

WHIP_LEFT = [WHIP_LEFT1, WHIP_LEFT2, WHIP_LEFT3, WHIP_LEFT4, WHIP_LEFT5]



EXPERT_WHIP_RIGHT1 = pygame.image.load("data/assets/Belmont/right/expert_attack/frame-1.gif").convert_alpha()
EXPERT_WHIP_RIGHT2 = pygame.image.load("data/assets/Belmont/right/expert_attack/frame-2.gif").convert_alpha()
EXPERT_WHIP_RIGHT3 = pygame.image.load("data/assets/Belmont/right/expert_attack/frame-3.gif").convert_alpha()
EXPERT_WHIP_RIGHT4 = pygame.image.load("data/assets/Belmont/right/expert_attack/frame-4.gif").convert_alpha()
EXPERT_WHIP_RIGHT5 = pygame.image.load("data/assets/Belmont/right/expert_attack/frame-5.gif").convert_alpha()

EXPERT_WHIP_RIGHT = [EXPERT_WHIP_RIGHT1, EXPERT_WHIP_RIGHT2, EXPERT_WHIP_RIGHT3, EXPERT_WHIP_RIGHT4, EXPERT_WHIP_RIGHT5]

EXPERT_WHIP_LEFT1 = pygame.image.load("data/assets/Belmont/left/expert_attack/frame-1.gif").convert_alpha()
EXPERT_WHIP_LEFT2 = pygame.image.load("data/assets/Belmont/left/expert_attack/frame-2.gif").convert_alpha()
EXPERT_WHIP_LEFT3 = pygame.image.load("data/assets/Belmont/left/expert_attack/frame-3.gif").convert_alpha()
EXPERT_WHIP_LEFT4 = pygame.image.load("data/assets/Belmont/left/expert_attack/frame-4.gif").convert_alpha()
EXPERT_WHIP_LEFT5 = pygame.image.load("data/assets/Belmont/left/expert_attack/frame-5.gif").convert_alpha()

EXPERT_WHIP_LEFT = [EXPERT_WHIP_LEFT1, EXPERT_WHIP_LEFT2, EXPERT_WHIP_LEFT3, EXPERT_WHIP_LEFT4, EXPERT_WHIP_LEFT5]

    

DAGGER = pygame.image.load("data/assets/Weapons/Dagger.png").convert_alpha()
UIDAGGER = pygame.image.load("data/assets/UI/Weapons/Dagger.png").convert()

AXE = pygame.image.load("data/assets/Weapons/Axe.png").convert_alpha()
UIAXE = pygame.image.load("data/assets/UI/Weapons/Axe.png").convert()

FLAME1 = pygame.image.load("data/assets/Others/FlameHit/frame-1.gif").convert_alpha()
FLAME2 = pygame.image.load("data/assets/Others/FlameHit/frame-2.gif").convert_alpha()
FLAME3 = pygame.image.load("data/assets/Others/FlameHit/frame-3.gif").convert_alpha()
FLAME4 = pygame.image.load("data/assets/Others/FlameHit/frame-4.gif").convert_alpha()
FLAME5 = pygame.image.load("data/assets/Others/FlameHit/frame-5.gif").convert_alpha()

FLAME = [FLAME1, FLAME2, FLAME3, FLAME4, FLAME5]

CANDLE1 = pygame.image.load("data/assets/Others/Candle/frame-1.gif").convert_alpha()
CANDLE2 = pygame.image.load("data/assets/Others/Candle/frame-2.gif").convert_alpha()

CANDLE = [CANDLE1, CANDLE2]

LARGEHEART = pygame.image.load("data/assets/Items/LargeHeart/LargeHeart.png").convert_alpha()
SMALLHEART = pygame.image.load("data/assets/Items/SmallHeart/SmallHeart.png").convert_alpha()

LARGECANDLE1 = pygame.image.load("data/assets/Others/LargeCandle/frame-1.gif").convert_alpha()
LARGECANDLE2 = pygame.image.load("data/assets/Others/LargeCandle/frame-2.gif").convert_alpha()
LARGECANDLE = [LARGECANDLE1, LARGECANDLE2]

MAGICALCRYSTAL1 = pygame.image.load("data/assets/Items/MagicalCrystal/frame-1.gif").convert_alpha()
MAGICALCRYSTAL2 = pygame.image.load("data/assets/Items/MagicalCrystal/frame-2.gif").convert_alpha()

MAGICALCRYSTAL = [MAGICALCRYSTAL1, MAGICALCRYSTAL2]

WHIPUPGRADE = pygame.image.load("data/assets/Weapons/MorningStar.png").convert_alpha()


"""ENEMY"""

BLACKLEOPARD_LEFT1 = pygame.image.load("data/assets/Enemies/BlackLeopard/left/frame-1.gif").convert_alpha()
BLACKLEOPARD_LEFT2 = pygame.image.load("data/assets/Enemies/BlackLeopard/left/frame-2.gif").convert_alpha()
BLACKLEOPARD_LEFT3 = pygame.image.load("data/assets/Enemies/BlackLeopard/left/frame-3.gif").convert_alpha()
BLACKLEOPARD_RIGHT1 = pygame.image.load("data/assets/Enemies/BlackLeopard/right/frame-1.gif").convert_alpha()
BLACKLEOPARD_RIGHT2 = pygame.image.load("data/assets/Enemies/BlackLeopard/right/frame-2.gif").convert_alpha()
BLACKLEOPARD_RIGHT3 = pygame.image.load("data/assets/Enemies/BlackLeopard/right/frame-3.gif").convert_alpha()
BLACKLEOPARD_LEFT_SITTING = pygame.image.load("data/assets/Enemies/BlackLeopard/right/BlackLeopardSitting.png").convert_alpha()
BLACKLEOPARD_RIGHT_SITTING = pygame.image.load("data/assets/Enemies/BlackLeopard/left/BlackLeopardSitting.png").convert_alpha()

BLACKLEOPARD = [BLACKLEOPARD_LEFT1 ,BLACKLEOPARD_LEFT2 ,BLACKLEOPARD_RIGHT1, BLACKLEOPARD_RIGHT2, BLACKLEOPARD_LEFT_SITTING, BLACKLEOPARD_RIGHT_SITTING, BLACKLEOPARD_LEFT3, BLACKLEOPARD_RIGHT3]

ZOMBIE_LEFT1 = pygame.image.load("data/assets/Enemies/Zombie/left/frame-1.gif").convert_alpha()
ZOMBIE_LEFT2 = pygame.image.load("data/assets/Enemies/Zombie/left/frame-2.gif").convert_alpha()
ZOMBIE_RIGHT1 = pygame.image.load("data/assets/Enemies/Zombie/right/frame-1.gif").convert_alpha()
ZOMBIE_RIGHT2 = pygame.image.load("data/assets/Enemies/Zombie/right/frame-2.gif").convert_alpha()

ZOMBIE = [ZOMBIE_LEFT1, ZOMBIE_LEFT2, ZOMBIE_RIGHT1, ZOMBIE_RIGHT2]

BAT_LEFT1 = pygame.image.load("data/assets/Enemies/VampireBat/left/frame-1.gif").convert_alpha()
BAT_LEFT2 = pygame.image.load("data/assets/Enemies/VampireBat/left/frame-2.gif").convert_alpha()
BAT_RIGHT1 = pygame.image.load("data/assets/Enemies/VampireBat/right/frame-1.gif").convert_alpha()
BAT_RIGHT2 = pygame.image.load("data/assets/Enemies/VampireBat/right/frame-2.gif").convert_alpha()

BAT = [BAT_LEFT1, BAT_LEFT2, BAT_RIGHT1, BAT_RIGHT2]

FISHMAN_LEFT1 = pygame.image.load("data/assets/Enemies/FishMan/left/frame-1.gif").convert_alpha()
FISHMAN_LEFT2 = pygame.image.load("data/assets/Enemies/FishMan/left/frame-2.gif").convert_alpha()
FISHMAN_LEFT_MOUTH = pygame.image.load("data/assets/Enemies/FishMan/left/FishManOpenMouth.png").convert_alpha()
FISHMAN_RIGHT1 = pygame.image.load("data/assets/Enemies/FishMan/right/frame-1.gif").convert_alpha()
FISHMAN_RIGHT2 = pygame.image.load("data/assets/Enemies/FishMan/right/frame-2.gif").convert_alpha()
FISHMAN_RIGHT_MOUTH = pygame.image.load("data/assets/Enemies/FishMan/right/FishManOpenMouth.png").convert_alpha()

FISHMAN = [FISHMAN_LEFT1, FISHMAN_LEFT2, FISHMAN_LEFT_MOUTH, FISHMAN_RIGHT1, FISHMAN_RIGHT2, FISHMAN_RIGHT_MOUTH]


"""OTHERS"""

TITLE = pygame.image.load("data/assets/Title.png").convert()

PAUSE_SOUND = pygame.mixer.Sound("data/sounds/pause.wav")
HURT_SOUND = pygame.mixer.Sound("data/sounds/Hurt.wav")
BELMONTHURT_SOUND = pygame.mixer.Sound("data/sounds/BelmontHurt.wav")
ITEMGRAB_SOUND = pygame.mixer.Sound("data/sounds/Item_Grab.wav")
WEAPONGRAB_SOUND = pygame.mixer.Sound("data/sounds/Weapon_Grab.wav")
ATTACK_SOUND = pygame.mixer.Sound("data/sounds/Attack.wav")

BACKGROUND1 = pygame.image.load("data/assets/Levels/level_1.png").convert_alpha()
BACKGROUND2 = pygame.image.load("data/assets/Levels/level_2.png").convert_alpha()

BACKGROUND = [BACKGROUND1, BACKGROUND2]

MAP = pygame.image.load("data/assets/Map/Map.png").convert()

UIBACKGROUND = pygame.image.load("data/assets/UI/UI_font.png").convert()


"""BOSS"""

BOSS1_1 = pygame.image.load("data/assets/Boss/PhantomBat/frame-1.gif").convert()
BOSS1_2 = pygame.image.load("data/assets/Boss/PhantomBat/frame-2.gif").convert()
BOSS1_3 = pygame.image.load("data/assets/Boss/PhantomBat/PhantomBatHanging.png").convert()

BOSS1 = [BOSS1_1, BOSS1_2, BOSS1_3]








