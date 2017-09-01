#Evan Schirle
#Pac Man Pygame

import pygame, sys, random, time
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

#Every rectangle is one of the pellets on the level
def setFood ():
    FOODSIZE = 6
    foods = [pygame.Rect(47, 47, FOODSIZE, FOODSIZE),
         pygame.Rect(73, 47, FOODSIZE, FOODSIZE),
         pygame.Rect(99, 47, FOODSIZE, FOODSIZE),
         pygame.Rect(125, 47, FOODSIZE, FOODSIZE),
         pygame.Rect(151, 47, FOODSIZE, FOODSIZE),
         pygame.Rect(177, 47, FOODSIZE, FOODSIZE),
         pygame.Rect(203.5, 47, FOODSIZE, FOODSIZE),
         pygame.Rect(230, 47, FOODSIZE, FOODSIZE),
         pygame.Rect(256.5, 47, FOODSIZE, FOODSIZE),
         pygame.Rect(283, 47, FOODSIZE, FOODSIZE),
         pygame.Rect(310, 47, FOODSIZE, FOODSIZE),
         pygame.Rect(337, 47, FOODSIZE, FOODSIZE),
         
         pygame.Rect(47, 72, FOODSIZE, FOODSIZE),
         pygame.Rect(177, 72, FOODSIZE, FOODSIZE),
         pygame.Rect(337, 72, FOODSIZE, FOODSIZE),

         pygame.Rect(177, 98, FOODSIZE, FOODSIZE),
         pygame.Rect(337, 98, FOODSIZE, FOODSIZE),
         
         pygame.Rect(47, 122, FOODSIZE, FOODSIZE),
         pygame.Rect(177, 122, FOODSIZE, FOODSIZE),
         pygame.Rect(337, 122, FOODSIZE, FOODSIZE),

         pygame.Rect(47, 147, FOODSIZE, FOODSIZE),
         pygame.Rect(73, 147, FOODSIZE, FOODSIZE),
         pygame.Rect(99, 147, FOODSIZE, FOODSIZE),
         pygame.Rect(125, 147, FOODSIZE, FOODSIZE),
         pygame.Rect(151, 147, FOODSIZE, FOODSIZE),
         pygame.Rect(177, 147, FOODSIZE, FOODSIZE),
         pygame.Rect(203.5, 147, FOODSIZE, FOODSIZE),
         pygame.Rect(230, 147, FOODSIZE, FOODSIZE),         
         pygame.Rect(256.5, 147, FOODSIZE, FOODSIZE),
         pygame.Rect(283, 147, FOODSIZE, FOODSIZE),
         pygame.Rect(310, 147, FOODSIZE, FOODSIZE),
         pygame.Rect(337, 147, FOODSIZE, FOODSIZE),
         pygame.Rect(364, 147, FOODSIZE, FOODSIZE),
         
         pygame.Rect(47, 174, FOODSIZE, FOODSIZE),
         pygame.Rect(177, 174, FOODSIZE, FOODSIZE),
         pygame.Rect(256.5, 174, FOODSIZE, FOODSIZE),

         pygame.Rect(47, 201.5, FOODSIZE, FOODSIZE),
         pygame.Rect(177, 201.5, FOODSIZE, FOODSIZE),
         pygame.Rect(256.5, 201.5, FOODSIZE, FOODSIZE),

         pygame.Rect(47, 229, FOODSIZE, FOODSIZE),
         pygame.Rect(73, 229, FOODSIZE, FOODSIZE),
         pygame.Rect(99, 229, FOODSIZE, FOODSIZE),
         pygame.Rect(125, 229, FOODSIZE, FOODSIZE),
         pygame.Rect(151, 229, FOODSIZE, FOODSIZE),
         pygame.Rect(177, 229, FOODSIZE, FOODSIZE),
         pygame.Rect(256.5, 229, FOODSIZE, FOODSIZE),
         pygame.Rect(283, 229, FOODSIZE, FOODSIZE),
         pygame.Rect(310, 229, FOODSIZE, FOODSIZE),
         pygame.Rect(337, 229, FOODSIZE, FOODSIZE),

         pygame.Rect(177, 256, FOODSIZE, FOODSIZE),
         pygame.Rect(337, 256, FOODSIZE, FOODSIZE),
         pygame.Rect(177, 283, FOODSIZE, FOODSIZE),
         pygame.Rect(337, 283, FOODSIZE, FOODSIZE),
         pygame.Rect(177, 310.7, FOODSIZE, FOODSIZE),
         pygame.Rect(177, 338.4, FOODSIZE, FOODSIZE),
         pygame.Rect(177, 366.1, FOODSIZE, FOODSIZE),
         pygame.Rect(177, 393.8, FOODSIZE, FOODSIZE),
         pygame.Rect(177, 421.5, FOODSIZE, FOODSIZE),
         pygame.Rect(177, 449.3, FOODSIZE, FOODSIZE),
         pygame.Rect(177, 477.5, FOODSIZE, FOODSIZE),
         pygame.Rect(177, 505.7, FOODSIZE, FOODSIZE),

         pygame.Rect(47, 534, FOODSIZE, FOODSIZE),
         pygame.Rect(73, 534, FOODSIZE, FOODSIZE),
         pygame.Rect(99, 534, FOODSIZE, FOODSIZE),
         pygame.Rect(125, 534, FOODSIZE, FOODSIZE),
         pygame.Rect(151, 534, FOODSIZE, FOODSIZE),
         pygame.Rect(177, 534, FOODSIZE, FOODSIZE),
         pygame.Rect(203.5, 534, FOODSIZE, FOODSIZE),
         pygame.Rect(230, 534, FOODSIZE, FOODSIZE),
         pygame.Rect(256.5, 534, FOODSIZE, FOODSIZE),
         pygame.Rect(283, 534, FOODSIZE, FOODSIZE),
         pygame.Rect(310, 534, FOODSIZE, FOODSIZE),
         pygame.Rect(337, 534, FOODSIZE, FOODSIZE),

         pygame.Rect(47, 562.5, FOODSIZE, FOODSIZE),
         pygame.Rect(177, 562.5, FOODSIZE, FOODSIZE),
         pygame.Rect(337, 562.5, FOODSIZE, FOODSIZE),
         pygame.Rect(47, 591, FOODSIZE, FOODSIZE),
         pygame.Rect(177, 591, FOODSIZE, FOODSIZE),
         pygame.Rect(337, 591, FOODSIZE, FOODSIZE),
         
         pygame.Rect(72, 620, FOODSIZE, FOODSIZE),
         pygame.Rect(97, 620, FOODSIZE, FOODSIZE),
         pygame.Rect(177, 620, FOODSIZE, FOODSIZE),
         pygame.Rect(203.5, 620, FOODSIZE, FOODSIZE),
         pygame.Rect(230, 620, FOODSIZE, FOODSIZE),
         pygame.Rect(256.5, 620, FOODSIZE, FOODSIZE),
         pygame.Rect(283, 620, FOODSIZE, FOODSIZE),
         pygame.Rect(310, 620, FOODSIZE, FOODSIZE),
         pygame.Rect(337, 620, FOODSIZE, FOODSIZE),
         
         pygame.Rect(98, 648.5, FOODSIZE, FOODSIZE),
         pygame.Rect(177, 648.5, FOODSIZE, FOODSIZE),
         pygame.Rect(256.5, 648.5, FOODSIZE, FOODSIZE),

         pygame.Rect(98.5, 677, FOODSIZE, FOODSIZE),
         pygame.Rect(177, 677, FOODSIZE, FOODSIZE),
         pygame.Rect(256.5, 677, FOODSIZE, FOODSIZE),

         pygame.Rect(47, 706, FOODSIZE, FOODSIZE),
         pygame.Rect(73, 706, FOODSIZE, FOODSIZE),
         pygame.Rect(99, 706, FOODSIZE, FOODSIZE),
         pygame.Rect(125, 706, FOODSIZE, FOODSIZE),
         pygame.Rect(151, 706, FOODSIZE, FOODSIZE),
         pygame.Rect(177, 706, FOODSIZE, FOODSIZE),
         pygame.Rect(256.5, 706, FOODSIZE, FOODSIZE),
         pygame.Rect(283, 706, FOODSIZE, FOODSIZE),
         pygame.Rect(310, 706, FOODSIZE, FOODSIZE),
         pygame.Rect(337, 706, FOODSIZE, FOODSIZE),

         pygame.Rect(47, 734, FOODSIZE, FOODSIZE),
         pygame.Rect(337, 734, FOODSIZE, FOODSIZE),
         pygame.Rect(47, 762, FOODSIZE, FOODSIZE),
         pygame.Rect(337, 762, FOODSIZE, FOODSIZE),
         
         pygame.Rect(47, 787, FOODSIZE, FOODSIZE),
         pygame.Rect(73, 787, FOODSIZE, FOODSIZE),
         pygame.Rect(99, 787, FOODSIZE, FOODSIZE),
         pygame.Rect(125, 787, FOODSIZE, FOODSIZE),
         pygame.Rect(151, 787, FOODSIZE, FOODSIZE),
         pygame.Rect(177, 787, FOODSIZE, FOODSIZE),
         pygame.Rect(203.5, 787, FOODSIZE, FOODSIZE),
         pygame.Rect(230, 787, FOODSIZE, FOODSIZE),         
         pygame.Rect(256.5, 787, FOODSIZE, FOODSIZE),
         pygame.Rect(283, 787, FOODSIZE, FOODSIZE),
         pygame.Rect(310, 787, FOODSIZE, FOODSIZE),
         pygame.Rect(337, 787, FOODSIZE, FOODSIZE),
         pygame.Rect(364, 787, FOODSIZE, FOODSIZE),
         ]
    foodsRIGHT = []
    for food in foods:
        X = windowWidth - (food.left) - FOODSIZE
        Y = food.top
        foodsRIGHT.append(pygame.Rect(X, Y, FOODSIZE, FOODSIZE))
    for food in foodsRIGHT:
        foods.append(food)
    return foods

def hitWall (walls, player):
    for wall in walls:
        if player.bottom > wall.top and player.left < wall.right and player.right > wall.left and player.top < wall.bottom:
            return True
    return False

def checkTeleport(character, windowWidth):
    if character.bottom <= 410 and character.top >= 360 and (character.left > windowWidth or character.right <= 0):
        if character.left >= windowWidth:
            character = pygame.Rect(-25, 370, 30, 30)
        if character.right <= 0:
            character = pygame.Rect(windowWidth-5, 370, 30, 30)
    return character

def loseLife(lives):
    lives -= 1
    return lives

def spinPacman (player, pacman, windowSurface, sounds):
    sounds['die'].play()
    truthness = True
    count = 0
    while truthness:
        windowSurface.fill(black)
        windowSurface.blit(pygame.transform.rotate(pacman[2], count*90), player)
        pygame.display.update()
        time.sleep(.05)
        count += 1
        if count >= 27:
            truthness = False

def WIN (player, pacman, windowSurface, walls, sounds, blue, textRect, text):
    time.sleep(sounds['win'].get_length())
    sounds['end'].play(loops = 500)
    showWalls = True
    count = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                if event.key == K_ESCAPE or event.key == K_SPACE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_RETURN:
                    return True       
        windowSurface.fill(black)
        windowSurface.blit(pacman[2], player)
        if showWalls:
            for wall in walls:
                pygame.draw.rect(windowSurface, blue, wall)
            time.sleep(.5)
            showWalls = False
        else:
            time.sleep(.5)
            showWalls = True
        count += 1
        if count == 80:
            pygame.quit()
            sys.exit()
        windowSurface.blit(text, textRect)
        pygame.display.update()
        

def checkCanGoUp(character, walls, speed):
    truthness = True
    for wall in walls:
        if character.top < wall.bottom +speed and character.right > wall.left and character.left < wall.right and character.bottom > wall.bottom:
            truthness = False
    return truthness

def checkCanGoDown(character, walls, speed):
    truthness = True
    for wall in walls:
        if character.bottom > wall.top -speed and character.right > wall.left and character.left < wall.right and character.top < wall.top:
            truthness = False
    return truthness

def checkCanGoRight(character, walls, speed):
    truthness = True
    for wall in walls:
        if character.right > wall.left -speed and character.bottom > wall.top and character.top < wall.bottom and character.left < wall.left:
            truthness = False
    return truthness

def checkCanGoLeft(character, walls, speed):
    truthness = True
    for wall in walls:
        if character.left < wall.right +speed and character.bottom > wall.top and character.top < wall.bottom and character.right > wall.right:
            truthness = False
    return truthness

def moveGhosts (ghosts, ghostNames, walls, player):
    #each mode makes the ghost move a different way
    for ghost in ghostNames:
        if ghosts[ghost]['form'] == 7:
            ghosts[ghost]['mode'] = 'return'
            ghosts[ghost]['speed'] = 5
        if ghosts[ghost]['vulnerable'] and ghosts[ghost]['mode'] != 'get out':
            ghosts[ghost]['speed'] = 3
        if not ghosts[ghost]['vulnerable']:
            ghosts[ghost]['speed'] = 5
        if ghosts[ghost]['mode'] == 'still':
            ghosts[ghost]['dir'] = 0
            

        if ghosts[ghost]['mode'] != 'bounce':
            direction = ghosts[ghost]['dir']
            if direction == DOWN:
                if checkCanGoDown(ghosts[ghost]['rect'], walls, ghosts[ghost]['speed']):
                    ghosts[ghost]['rect'].top += ghosts[ghost]['speed']
                    ghosts[ghost]['moving'] = True
                else:
                    ghosts[ghost]['moving'] = False
            if direction == UP:
                if checkCanGoUp(ghosts[ghost]['rect'], walls, ghosts[ghost]['speed']):
                    ghosts[ghost]['rect'].top -= ghosts[ghost]['speed']
                    ghosts[ghost]['moving'] = True
                else:
                    ghosts[ghost]['moving'] = False
            if direction == RIGHT:
                if checkCanGoRight(ghosts[ghost]['rect'], walls, ghosts[ghost]['speed']):
                    ghosts[ghost]['rect'].right += ghosts[ghost]['speed']
                    ghosts[ghost]['moving'] = True
                else:
                    ghosts[ghost]['moving'] = False
            if direction == LEFT:
                if checkCanGoLeft(ghosts[ghost]['rect'], walls, ghosts[ghost]['speed']):
                    ghosts[ghost]['rect'].left -= ghosts[ghost]['speed']
                    ghosts[ghost]['moving'] = True
                else:
                    ghosts[ghost]['moving'] = False 

        if ghosts[ghost]['mode'] == 'bounce':
            direction = ghosts[ghost]['dir']
            if direction == DOWN:
                ghosts[ghost]['rect'].top += ghosts[ghost]['speed']
                ghosts[ghost]['moving'] = True
                if hitWall(walls, ghosts[ghost]['rect']):
                    ghosts[ghost]['dir'] = UP
            if direction == UP and ghosts[ghost]['rect'].top > 0:
                ghosts[ghost]['rect'].top -= ghosts[ghost]['speed']
                ghosts[ghost]['moving'] = True
                if hitWall(walls, ghosts[ghost]['rect']):
                    ghosts[ghost]['dir'] = DOWN
            if direction == RIGHT:
                ghosts[ghost]['rect'].right += ghosts[ghost]['speed']
                ghosts[ghost]['moving'] = True
                if hitWall(walls, ghosts[ghost]['rect']):
                    ghosts[ghost]['dir'] = LEFT
            if direction == LEFT and ghosts[ghost]['rect'].left > 0:
                ghosts[ghost]['rect'].left -= ghosts[ghost]['speed']
                ghosts[ghost]['moving'] = True
                if hitWall(walls, ghosts[ghost]['rect']):
                    ghosts[ghost]['dir'] = RIGHT


        where = ''
        if ghosts[ghost]['mode'] == 'run away' or ghosts[ghost]['mode'] == 'attack': #makes the ghost avoid pacman
            if player.top > ghosts[ghost]['rect'].top:
                where += 'down'
            if player.top < ghosts[ghost]['rect'].top:
                where += 'up'
            if player.left > ghosts[ghost]['rect'].left:
                where += 'right'
            if player.left < ghosts[ghost]['rect'].left:
                where += 'left'
        if ghosts[ghost]['mode'] == 'run away':
            if where == 'downright':
                if checkCanGoUp(ghosts[ghost]['rect'], walls, ghosts[ghost]['speed']):
                    ghosts[ghost]['dir'] = UP
                elif checkCanGoLeft(ghosts[ghost]['rect'], walls, ghosts[ghost]['speed']):
                    ghosts[ghost]['dir'] = LEFT
                elif checkCanGoRight(ghosts[ghost]['rect'], walls, ghosts[ghost]['speed']):
                    ghosts[ghost]['dir'] = RIGHT
                else:
                    ghosts[ghost]['dir'] = DOWN
            if where == 'downleft':
                if checkCanGoUp(ghosts[ghost]['rect'], walls, ghosts[ghost]['speed']):
                    ghosts[ghost]['dir'] = UP
                elif checkCanGoRight(ghosts[ghost]['rect'], walls, ghosts[ghost]['speed']):
                    ghosts[ghost]['dir'] = RIGHT
                elif checkCanGoLeft(ghosts[ghost]['rect'], walls, ghosts[ghost]['speed']):
                    ghosts[ghost]['dir'] = LEFT
                else:
                    ghosts[ghost]['dir'] = DOWN
            if where == 'upright':
                if checkCanGoDown(ghosts[ghost]['rect'], walls, ghosts[ghost]['speed']):
                    ghosts[ghost]['dir'] = DOWN
                elif checkCanGoLeft(ghosts[ghost]['rect'], walls, ghosts[ghost]['speed']):
                    ghosts[ghost]['dir'] = LEFT
                elif checkCanGoRight(ghosts[ghost]['rect'], walls, ghosts[ghost]['speed']):
                    ghosts[ghost]['dir'] = RIGHT
                else:
                    ghosts[ghost]['dir'] = UP
            if where == 'upleft':
                if checkCanGoDown(ghosts[ghost]['rect'], walls, ghosts[ghost]['speed']):
                    ghosts[ghost]['dir'] = DOWN
                elif checkCanGoRight(ghosts[ghost]['rect'], walls, ghosts[ghost]['speed']):
                    ghosts[ghost]['dir'] = RIGHT
                elif checkCanGoLeft(ghosts[ghost]['rect'], walls, ghosts[ghost]['speed']):
                    ghosts[ghost]['dir'] = LEFT
                else:
                    ghosts[ghost]['dir'] = UP
                    
        if ghosts[ghost]['mode'] == 'return': #makes ghost go back to the little ghost box 
            if ghosts[ghost]['rect'].top > 370 and not (ghosts[ghost]['rect'].top >=300 and ghosts[ghost]['rect'].bottom <=400 and ghosts[ghost]['rect'].right <=520 and ghosts[ghost]['rect'].left >=240):
                if checkCanGoUp(ghosts[ghost]['rect'], walls, ghosts[ghost]['speed']):
                    ghosts[ghost]['dir'] = UP
                else:
                    if ghosts[ghost]['rect'].left <= 370:
                        ghosts[ghost]['dir'] = LEFT
                    if ghosts[ghost]['rect'].left > 370:
                        ghosts[ghost]['dir'] = RIGHT
                    if ghosts[ghost]['rect'].top <= 525 and ghosts[ghost]['rect'].left < 165:
                        ghosts[ghost]['dir'] = RIGHT
                    if ghosts[ghost]['rect'].top <= 695 and ghosts[ghost]['rect'].top >= 685 and ghosts[ghost]['rect'].left < 165:
                        ghosts[ghost]['dir'] = RIGHT
                    if ghosts[ghost]['rect'].top <= 525 and ghosts[ghost]['rect'].right > 595:
                        ghosts[ghost]['dir'] = LEFT
                    if ghosts[ghost]['rect'].top <= 695 and ghosts[ghost]['rect'].top >= 685 and ghosts[ghost]['rect'].left > 565:
                        ghosts[ghost]['dir'] = LEFT
                        
            if ghosts[ghost]['rect'].top < 360 and not (ghosts[ghost]['rect'].top >=300 and ghosts[ghost]['rect'].bottom <=400 and ghosts[ghost]['rect'].right <=520 and ghosts[ghost]['rect'].left >=240):
                if checkCanGoDown(ghosts[ghost]['rect'], walls, ghosts[ghost]['speed']):
                    ghosts[ghost]['dir'] = DOWN
                else:
                    if ghosts[ghost]['rect'].left <= 370:
                        ghosts[ghost]['dir'] = LEFT
                    if ghosts[ghost]['rect'].left > 370:
                        ghosts[ghost]['dir'] = RIGHT
                    if ghosts[ghost]['rect'].bottom >= 255 and ghosts[ghost]['rect'].left < 365:
                        ghosts[ghost]['dir'] = RIGHT
                    if ghosts[ghost]['rect'].bottom >= 255 and ghosts[ghost]['rect'].left > 365:
                        ghosts[ghost]['dir'] = LEFT
                
            if ghosts[ghost]['rect'].top <= 370 and ghosts[ghost]['rect'].top >=360:
                if ghosts[ghost]['rect'].left < 360:
                    ghosts[ghost]['dir'] = RIGHT
                    if ghosts[ghost]['rect'].right >= 275:
                        ghosts[ghost]['dir'] = UP

                if ghosts[ghost]['rect'].left > 370:
                    ghosts[ghost]['dir'] = LEFT
                    if ghosts[ghost]['rect'].left <= 485:
                        ghosts[ghost]['dir'] = UP
                            
            if ghosts[ghost]['rect'].top >=300 and ghosts[ghost]['rect'].bottom <=340 and ghosts[ghost]['rect'].right <=520 and ghosts[ghost]['rect'].left >=240:
                if ghosts[ghost]['rect'].left < 360:
                    ghosts[ghost]['dir'] = RIGHT
                if ghosts[ghost]['rect'].left > 370:
                    ghosts[ghost]['dir'] = LEFT
                if ghosts[ghost]['rect'].left >=360 and ghosts[ghost]['rect'].left <=370:
                    ghosts[ghost]['dir'] = DOWN

            if ghosts[ghost]['rect'].top >=350 and ghosts[ghost]['rect'].bottom <=400 and ghosts[ghost]['rect'].right <=480 and ghosts[ghost]['rect'].left >=320:
                ghosts[ghost]['mode'] = 'get out'
                ghosts[ghost]['vulnerable'] = False
                ghosts[ghost]['form'] = 0
                ghosts[ghost]['dir'] = UP
                                                               
        if ghosts[ghost]['mode'] == 'get out':
            if ghosts[ghost]['rect'].left >= 360 and ghosts[ghost]['rect'].right <= 400:
                ghosts[ghost]['dir'] = UP
            if ghosts[ghost]['rect'].top <= 305:
                if player.left > 350:
                    ghosts[ghost]['dir'] = RIGHT
                else:
                    ghosts[ghost]['dir'] = LEFT
                ghosts[ghost]['mode'] = 'random'

        if ghosts[ghost]['mode'] == 'random':
            if not ghosts[ghost]['moving']:
                number = ghosts[ghost]['dir']
                while ghosts[ghost]['dir'] == number:
                    ghosts[ghost]['dir'] = random.randint(1,4)
    return ghosts

#Set up window
windowWidth = 760
windowHeight = 840
windowSurface = pygame.display.set_mode((windowWidth, windowHeight), 0, 32)
pygame.display.set_caption('Pac-Man')
gameStart = False
gameOver = False
gameReset = False
gameOpening = True

#Colors
black = (0, 0, 0)
white = (255, 255, 255)
blue  = (0, 0, 255)
red   = (255, 0, 0)

#Set up text and stuff
textRect = pygame.Rect(280, 430, 200, 50)
readyIMG = pygame.image.load('images/ready.gif')
readyIMG = pygame.transform.scale(readyIMG, (200, 40))
gameOverIMG = pygame.image.load('images/gameover.gif')
gameOverIMG = pygame.transform.scale(gameOverIMG, (200, 50))
livesIMG = pygame.image.load('images/life.gif')
livesIMG = pygame.transform.scale(livesIMG, (20, 20))

basicFont = pygame.font.SysFont(None, 48)
WinTextRect = pygame.Rect(0,0,0,0)
WinTextRect.left = 150
WinTextRect.top = 430
text = basicFont.render('Press <ENTER> to play again!', True, white, black)

#Set up the SOUNDS!!!!
sounds = {}
sounds['intro'] = pygame.mixer.Sound('sounds/intro.wav')
sounds['die'] = pygame.mixer.Sound('sounds/die.wav')
sounds['gameOver'] = pygame.mixer.Sound('sounds/gameOver.wav')
sounds['eat1'] = pygame.mixer.Sound('sounds/pellet1.wav')
sounds['eat2'] = pygame.mixer.Sound('sounds/pellet2.wav')
sounds['eatGhost'] = pygame.mixer.Sound('sounds/eatGhost.wav')
sounds['eatFruit'] = pygame.mixer.Sound('sounds/eatFruit.wav')
sounds['power'] = pygame.mixer.Sound('sounds/powerpellet.wav')
sounds['win'] = pygame.mixer.Sound('sounds/victoryIntro.wav')
sounds['end'] = pygame.mixer.Sound('sounds/victoryLoop.wav')

#Set up pacman
player = pygame.Rect(365, 610, 30, 30)
form = 2
lives = 2
score = 0
NEXT = 'left'
pacmanIMG = []
for num in range(1,9):
    image = pygame.image.load('images/pacman'+str(num)+'.gif')
    pacmanIMG.append(pygame.transform.scale(image, (30, 30)))
pacman = []
for img in pacmanIMG:
    pacman.append(pygame.transform.rotate(img, 270))

#Set up Ghosts
ghosts = {'blinky':{}, 'inky':{}, 'pinky':{}, 'sue':{} }
ghosts['blinky'] = {'rect':pygame.Rect(360, 300, 30, 30), 'dir':4, 'moving':True, 'form':0, 'vulnerable':False, 'mode':'random', 'speed':5}
ghosts['inky']   = {'rect':pygame.Rect(300, 360, 30, 30), 'dir':1, 'moving':True, 'form':0, 'vulnerable':False, 'mode':'bounce', 'speed':5}
ghosts['pinky']  = {'rect':pygame.Rect(360, 360, 30, 30), 'dir':1, 'moving':True, 'form':0, 'vulnerable':False, 'mode':'still', 'speed':5}
ghosts['sue']    = {'rect':pygame.Rect(420, 360, 30, 30), 'dir':3, 'moving':True, 'form':0, 'vulnerable':False, 'mode':'bounce', 'speed':5}

ghostNames = ['blinky', 'inky', 'pinky', 'sue']
ghostIMG = {'blinky':[], 'inky':[], 'pinky':[], 'sue':[],
            'blue':pygame.transform.scale(pygame.image.load('images/ghost_blue.gif'), (30,30)),
            'white':pygame.transform.scale(pygame.image.load('images/ghost_white.gif'), (30,30))
            }
ghostEyes = pygame.image.load('images/ghost7.gif')
ghostEyes = pygame.transform.scale(ghostEyes, (30, 30))
ghostCounter = 0
nextGhost = 250
powerCounter = 0
powerTime = 400
for ghost in ghostNames:
    for num in range(1,7):
        image = pygame.image.load('images/'+ghost+str(num)+'.gif')
        ghostIMG[ghost].append(pygame.transform.scale(image, (30,30)))
                                                            #^^Ghost IMG dimensions

#set up the fruit!
fruits = [pygame.transform.scale(pygame.image.load('images/fruit1.gif'), (25,25)),
          pygame.transform.scale(pygame.image.load('images/fruit2.gif'), (25,25)),
          pygame.transform.scale(pygame.image.load('images/fruit3.gif'), (25,25)),
          pygame.transform.scale(pygame.image.load('images/fruit4.gif'), (25,25))          
          ]
fruitCounter = 0
newFruit = 900
fruitTime = 275
fruitBox = pygame.Rect(0, 431, 1, 1)#while a fruit is not being displayed, pacman won't be able to run into fruitBox
isFruit = False
fruitFlash = False
fruit = ''

# set up the pellet data structure
powerIMG = pygame.image.load('images/powerPellet.gif')
powerIMG = pygame.transform.scale(powerIMG, (21, 21))
foods = setFood()
nibble = 1
powerPellets = [pygame.Rect(39, 88, 21, 21),
                pygame.Rect(700, 88, 21, 21),
                pygame.Rect(39, 612, 21, 21),
                pygame.Rect(700, 612, 21, 21)
                ]

#Walls
walls = [pygame.Rect(0, 0, windowWidth, 30),#top
         pygame.Rect(0, windowHeight - 30, windowWidth, 30) , #bottom
         pygame.Rect(0, 0, 30, 360) , #left top
         pygame.Rect(windowWidth-30, 0, 30, 360) , #right top
         pygame.Rect(0, 410, 30, 430) , #left bottom
         pygame.Rect(windowWidth-30, 460, 30, 380) , #right bottom
         #The letter labeling in my comments below refer to a map I drew by hand, you can ignore them
         pygame.Rect(70,  70, 90, 60) , #a1
         pygame.Rect(600, 70, 90, 60) , #a2
         pygame.Rect(200, 70, 120, 60) , #b1
         pygame.Rect(440, 70, 120, 60) , #b2
         pygame.Rect(70,  170, 90, 40) , #d1
         pygame.Rect(600, 170, 90, 40) , #d2
         pygame.Rect(360, 0, 40, 130) , #c
         pygame.Rect(70,  170, 90, 40) , #d1
         pygame.Rect(600, 170, 90, 40) , #d2
         pygame.Rect(200, 170, 40, 190) , #e1
         pygame.Rect(520, 170, 40, 190) , #e2
         pygame.Rect(200, 260, 120, 40) , #f1
         pygame.Rect(440, 260, 120, 40) , #f2
         pygame.Rect(280, 170, 200, 40) , #g
         pygame.Rect(360, 170, 40, 130) , #h
         pygame.Rect(0, 260, 160, 100) , #i1
         pygame.Rect(windowWidth-160, 260, 160, 100),#i2
         pygame.Rect(0, 410, 160, 100),  #j1
         pygame.Rect(windowWidth-160, 410, 160, 100),#j2
         pygame.Rect(200, 410, 40, 100) , #k1
         pygame.Rect(520, 410, 40, 100),#k2
         pygame.Rect(280, 470, 200, 40) , #l1
         pygame.Rect(360, 480, 40, 120) , #l2
         pygame.Rect(70, 560, 90, 40) , #m1
         pygame.Rect(600, 560, 90, 40),#m2
         pygame.Rect(120, 560, 40, 130) , #n1
         pygame.Rect(600, 560, 40, 130) , #n2
         pygame.Rect(200, 560, 120, 40) , #o1
         pygame.Rect(440, 560, 120, 40) , #o2
         pygame.Rect(0, 650, 75, 40) , #p1
         pygame.Rect(685, 650, 75, 40) , #p2
         pygame.Rect(200, 650, 40, 120) , #q1
         pygame.Rect(520, 650, 40, 120) , #q2
         pygame.Rect(70, 730, 250, 40) , #r1
         pygame.Rect(440, 730, 250, 40) , #r2
         pygame.Rect(280, 650, 200, 40) , #s
         pygame.Rect(360, 650, 40, 120) , #t
         
         pygame.Rect(280, 340, 80, 10),
         pygame.Rect(400, 340, 80, 10),
         pygame.Rect(280, 340, 10, 80),
         pygame.Rect(470, 340, 10, 80),
         pygame.Rect(280, 420, 200, 10)
        ]


#Movement Variables
moveLeft = True
moveRight = False
moveUp = False
moveDown = False
MOVESPEED = 4
moving = True
UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4

while True:
    if gameOpening:
        windowSurface.fill(black)
        #Draw the food
        foods = setFood()
        for pellet in powerPellets:
            windowSurface.blit(powerIMG, pellet)
        for pellet in foods:
            pygame.draw.rect(windowSurface, white, pellet)
        
        #Draw the walls
        for wall in walls:
            pygame.draw.rect(windowSurface, blue, wall)
    
        #Draw Pacman
        windowSurface.blit(pacman[form], player)

        #Draw Ghosts
        for ghost in ghostNames:
            windowSurface.blit(ghostIMG[ghost][ghosts[ghost]['form']], ghosts[ghost]['rect'])

        windowSurface.blit(readyIMG, (280, 435))
        pygame.display.update()
        sounds['intro'].play(loops = 0)
        time.sleep(sounds['intro'].get_length())
        gameOpening = False
        
    if gameStart:
        windowSurface.blit(readyIMG, (280, 435))
        pygame.display.update()
        time.sleep(1)
        gameStart = False
        
    if gameReset:
        if gameOver:
            gameOpening = True
            sounds['gameOver'].stop()
        gameOver = False
        gameReset = False
        gameStart = False
        hitGhost = False
        lives = 2
        score = 0
        player = pygame.Rect(370, 610, 30, 30)
        pacman = []
        for img in pacmanIMG:
            pacman.append(pygame.transform.rotate(img, 270))
        form = 2
        NEXT = 'left'
        moving = True
        moveLeft = True
        moveRight = False
        moveDown = False
        moveUp = False
        ghosts['blinky'] = {'rect':pygame.Rect(360, 300, 30, 30), 'dir':4, 'moving':True, 'form':0, 'vulnerable':False, 'mode':'random', 'speed':5}
        ghosts['inky']   = {'rect':pygame.Rect(300, 360, 30, 30), 'dir':1, 'moving':True, 'form':0, 'vulnerable':False, 'mode':'bounce', 'speed':5}
        ghosts['pinky']  = {'rect':pygame.Rect(360, 360, 30, 30), 'dir':1, 'moving':True, 'form':0, 'vulnerable':False, 'mode':'still', 'speed':5}
        ghosts['sue']    = {'rect':pygame.Rect(420, 360, 30, 30), 'dir':3, 'moving':True, 'form':0, 'vulnerable':False, 'mode':'bounce', 'speed':5}
        ghostCounter = 0
        powerCounter = 0
        fruitCounter = 0
        isFruit = False
        fruit = ''
        fruitBox = pygame.Rect(0, 0, 1, 1)
        powerPellets = [pygame.Rect(39, 88, 21, 21),
                pygame.Rect(700, 88, 21, 21),
                pygame.Rect(39, 612, 21, 21),
                pygame.Rect(700, 612, 21, 21)
                ]
        foods = setFood()

    if not gameStart and not gameReset and not gameOpening:
        for event in pygame.event.get():
            if event.type == QUIT:
                print('SCORE:  '+str(score))
                pygame.quit()
                sys.exit()
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    print('SCORE:  '+str(score))
                    pygame.quit()
                    sys.exit()
                if event.key == K_LEFT:
                    NEXT = 'left'
                if event.key == K_RIGHT:
                    NEXT = 'right'
                if event.key == K_UP:
                    NEXT = 'up'
                if event.key == K_DOWN:
                    NEXT = 'down'

        #Let there be FRUIT!!!
        fruitCounter += 1
        if isFruit: #If there is already a fruit, the fruitCounter will tick to tell us when it dissapears
            if fruitCounter >= fruitTime:
                fruit = ''
                fruitBox = pygame.Rect(0, 440, 1, 1)
                fruitCounter = 0
                isFruit = False
            elif fruitCounter >= fruitTime - 30:#make the fruit flash before it dissapears
                if (fruitTime - fruitCounter) > 25:
                    fruitFlash = True
                elif (fruitTime - fruitCounter) > 20:
                    fruitFlash = False
                elif (fruitTime - fruitCounter) > 15:
                    fruitFlash = True
                elif (fruitTime - fruitCounter) > 10:
                    fruitFlash = False
                elif (fruitTime - fruitCounter) > 5:
                    fruitFlash = True
                else:
                    fruitFlash = False
        if not isFruit: #if there is no fruit then we make one!
            if fruitCounter > newFruit: 
                whichFruit = random.randint(0,3)
                fruitBox = pygame.Rect(370, 435, 30, 30)
                fruit = fruits[whichFruit]
                fruitCounter = 0
                isFruit = True
        
        #Release the ghosts
        ghostCounter += 1
        if ghostCounter >= nextGhost:
            if ghosts['pinky']['mode'] == 'still':
                ghosts['pinky']['dir'] = UP
                ghosts['pinky']['mode'] = 'get out'
            elif ghosts['inky']['mode'] == 'bounce':
                ghosts['inky']['mode'] = 'get out'
                ghosts['inky']['dir'] = RIGHT
            elif ghosts['sue']['mode'] == 'bounce':
                ghosts['sue']['mode'] = 'get out'
                ghosts['sue']['dir'] = LEFT
            ghostCounter = 0

        #Allow the ghosts to be vulnerable for only a short period of time
        truthness = False
        for ghost in ghostNames:
            if ghosts[ghost]['vulnerable']:
                truthness = True
        if truthness:
            powerCounter += 1
        if powerCounter >= powerTime:
            powerCounter = 0
            for ghost in ghostNames:
                if ghosts[ghost]['mode'] != 'return':
                    ghosts[ghost]['vulnerable'] = False
                    ghosts[ghost]['form'] = 0

        #The following if statements allow for a delay in pacman's movements...
        #The player can press the button before pacman is able to move in a direction
        #Once pacman can move in the direction, he will without the player having to press again
        if NEXT == 'left' and checkCanGoLeft (player, walls, 25):
            moveUp = False
            moveRight = False
            moveDown = False
            moveLeft = True
            pacman = []
            for img in pacmanIMG:
                pacman.append(pygame.transform.rotate(img, 270))
        if NEXT == 'right' and checkCanGoRight (player, walls, 25):
            moveUp = False
            moveRight = True
            moveDown = False
            moveLeft = False
            pacman = []
            for img in pacmanIMG:
                pacman.append(pygame.transform.rotate(img, 90))
        if NEXT == 'up' and checkCanGoUp (player, walls, 25):
            moveUp = True
            moveRight = False
            moveDown = False
            moveLeft = False
            pacman = []
            for img in pacmanIMG:
                pacman.append(pygame.transform.rotate(img, 180))
        if NEXT == 'down' and checkCanGoDown (player, walls, 25):
            moveUp = False
            moveRight = False
            moveDown = True
            moveLeft = False
            pacman = pacmanIMG
        
        if moveDown:
            player.top += MOVESPEED
            moving = True
            if hitWall(walls, player):
                player.top -= MOVESPEED
                moving = False
        if moveUp:
           player.top -= MOVESPEED
           moving = True
           if hitWall(walls, player):
               player.top += MOVESPEED
               moving = False
        if moveLeft:
            player.left -= MOVESPEED
            moving = True
            if hitWall(walls, player):
               player.left += MOVESPEED
               moving = False
        if moveRight:
            player.right += MOVESPEED
            moving = True
            if hitWall(walls, player):
               player.right -= MOVESPEED
               moving = False

        #Make Pac-man's mouth go CHOMP CHOMP CHOMP
        if moving:
            if form == 7:
                form = 0
            else:
                form += 1
        else:
            form = 2

        #Make the ghosts move 
        ghosts = moveGhosts(ghosts, ghostNames, walls, player)
                
        #Make the ghost's tentacle things wiggle
        for ghost in ghostNames:
            if ghosts[ghost]['form'] == 5:
                ghosts[ghost]['form'] = 0
            elif ghosts[ghost]['form'] == 7:
                ghosts[ghost]['form'] = 7
            else:
                ghosts[ghost]['form'] += 1

        # check if the player has intersected with any pellets
        for food in foods:
            if player.colliderect(food):
                sounds['eat'+str(nibble)].play(loops=0)
                if nibble == 1:
                    nibble = 2
                elif nibble == 2:
                    nibble = 1
                foods.remove(food)
                score += 10
        for pellet in powerPellets:
            if player.colliderect(pellet):
                sounds['power'].play(loops=0)
                powerCounter = 0
                powerPellets.remove(pellet)
                for ghost in ghostNames:
                    ghosts[ghost]['vulnerable'] = True

        #check if the player ATE SOME FRUIT (:
        if isFruit and player.colliderect(fruitBox):
            sounds['eatFruit'].play()
            score += 100
            isFruit = False
            fruitCounter = 0
            fruit = ''

        #check if the player has intersected with any ghosts; check if pacman eats it or loses a life
        hitGhost = False
        ateGhost = False
        for ghost in ghostNames:
            if ghosts[ghost]['rect'].colliderect(player):
                if ghosts[ghost]['vulnerable']:
                    ateGhost = True
                    ghosts[ghost]['form'] = 7
                elif ghosts[ghost]['form'] == 7:
                    ghosts[ghost]['form'] = 7
                else:
                    hitGhost = True
                ghosts[ghost]['vulnerable'] = False
        if ateGhost:
            sounds['eatGhost'].play(loops = 0)
            score += 200
        if hitGhost:
            spinPacman(player, pacman, windowSurface, sounds)
            lives = loseLife(lives)
            if lives >= 0:
                gameOver = False
                gameStart = True
                windowSurface.blit(readyIMG, (280, 430))
                player = pygame.Rect(370, 610, 30, 30)
                pacman = []
                for img in pacmanIMG:
                    pacman.append(pygame.transform.rotate(img, 270))
                form = 2
                NEXT = 'left'
                moving = True
                moveLeft = True
                moveRight = False
                moveDown = False
                moveUp = False
                ghosts['blinky'] = {'rect':pygame.Rect(360, 300, 30, 30), 'dir':4, 'moving':True, 'form':0, 'vulnerable':False, 'mode':'random', 'speed':5}
                ghosts['inky']   = {'rect':pygame.Rect(300, 360, 30, 30), 'dir':1, 'moving':True, 'form':0, 'vulnerable':False, 'mode':'bounce', 'speed':5}
                ghosts['pinky']  = {'rect':pygame.Rect(360, 360, 30, 30), 'dir':1, 'moving':True, 'form':0, 'vulnerable':False, 'mode':'still', 'speed':5}
                ghosts['sue']    = {'rect':pygame.Rect(420, 360, 30, 30), 'dir':3, 'moving':True, 'form':0, 'vulnerable':False, 'mode':'bounce', 'speed':5}
                ghostCounter = 0
                powerCounter = 0
                fruitCounter = 0
                isFruit = False
                fruit = ''
                fruitBox = pygame.Rect(0, 0, 1, 1)
            if lives < 0:
                gameOver = True
            
        if gameOver:
            sounds['gameOver'].play(loops=0)
            windowSurface.blit(gameOverIMG, textRect)
            pygame.display.update()
            print('SCORE:  '+str(score))
            truthness = True
            while truthness:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYUP:
                        if event.key == K_RETURN:
                            truthness = False
                            gameReset = True
                        if event.key == K_ESCAPE:
                            pygame.quit()
                            sys.exit()
                            
        #check if the player won!!
        if foods == [] and powerPellets == []:
            sounds['win'].play(loops = 0)
            print('YOU WON!!!!')
            print('SCORE:  ' + str(score))
            print()
            print('PAC-MAN is the intellectual property of NAMCO BANDAI GAMES')
            print('programmed by Evan Schirle')
            print('sounds from various youtube videos, Legend of Zelda: Ocarina of Time, and Pokemon Blue Version')
            print('Special thanks to Brad Lindemann, David Reilly, and Neal Schirle')
            print('PYGAME ROCKS YEAH WHOOO!!')
            gameReset = WIN(player, pacman, windowSurface, walls, sounds, blue, WinTextRect, text)
            gameOver = True
            sounds['end'].stop()
            

        #Check if a portal was entered
        for ghost in ghostNames:
            ghosts[ghost]['rect'] = checkTeleport(ghosts[ghost]['rect'], windowWidth)
        player = checkTeleport(player, windowWidth)
    
    
    #black background
    windowSurface.fill(black)
    
    #Draw the food
    for pellet in foods:
        pygame.draw.rect(windowSurface, white, pellet)
        
    for pellet in powerPellets:
        windowSurface.blit(powerIMG, pellet)

    #Draw the FRUIT!
    if isFruit and not fruitFlash:
        windowSurface.blit(fruit, fruitBox)
    
    #Draw the walls
    for wall in walls:
        pygame.draw.rect(windowSurface, blue, wall)
    
    #Draw Pacman
    windowSurface.blit(pacman[form], player)

    #Draw Ghosts
    for ghost in ghostNames:
        if ghosts[ghost]['vulnerable']:
            if powerCounter >= powerTime - 70 and powerCounter < powerTime: #make the ghost flash if it is about to stop being vulnerable
                if (powerTime - powerCounter)/10 > 6:
                    windowSurface.blit(ghostIMG['white'], ghosts[ghost]['rect'])
                elif(powerTime - powerCounter)/10 > 5:
                    windowSurface.blit(ghostIMG['blue'], ghosts[ghost]['rect'])
                elif (powerTime - powerCounter)/10 > 4:
                    windowSurface.blit(ghostIMG['white'], ghosts[ghost]['rect'])
                elif (powerTime - powerCounter)/10 > 3:
                    windowSurface.blit(ghostIMG['blue'], ghosts[ghost]['rect'])
                elif (powerTime - powerCounter)/10 > 2:
                    windowSurface.blit(ghostIMG['white'], ghosts[ghost]['rect'])
                elif (powerTime - powerCounter)/10 > 1:
                    windowSurface.blit(ghostIMG['blue'], ghosts[ghost]['rect'])
                else:
                    windowSurface.blit(ghostIMG['white'], ghosts[ghost]['rect'])
            else:
                windowSurface.blit(ghostIMG['blue'], ghosts[ghost]['rect'])
        elif ghosts[ghost]['form'] == 7:
            windowSurface.blit(ghostEyes, ghosts[ghost]['rect'])
        else:
            windowSurface.blit(ghostIMG[ghost][ghosts[ghost]['form']], ghosts[ghost]['rect'])

    #Draw extra lives
    i=0
    while i < lives:
        space = i*25
        windowSurface.blit(livesIMG, (20+space, 270))
        i+=1

    #Draw the window onto the screen
    pygame.display.update()
    mainClock.tick(40)

