import pygame, sys, random
from pygame.locals import *

WINDOWWIDTH = 1024
WINDOWHEIGHT = 768
FPS = 30

BASICFONTSIZE = 40
SMALLFONTSIZE = 20

BLACK = (0,0,0)
WHITE = (255,255,255)

start_butt_width = 200
start_butt_height = 100

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, SMALLFONT        

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Chem_game')
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)
    SMALLFONT = pygame.font.Font('freesansbold.ttf', SMALLFONTSIZE)
    getStartBoard()

    while True:

        p = Player()
        while True:
            friend_list = setRound()
            won = false
            while True:
                checkForQuit()
                for event in pygame.event.get(): # event handling loop
                    if event.type == KEYUP:
                        #todo



        pygame.display.update()
        FPSCLOCK.tick(FPS)

def getStartBoard():
    screen.fill(BLACK)
    # pygame.draw.rect(screen, WHITE, ((WINDOWWIDTH-start_butt_width)/2, (WINDOWWIDTH-start_butt_width)/2, start_butt_width, start_butt_height), 4)
    startSurf, startRect = makeText(BASICFONT, "Start", BLACK, WHITE, WINDOWWIDTH/2-50, WINDOWHEIGHT/2-30)
    pressSurf, pressRect = makeText(SMALLFONT, "Press Enter to Start", BLACK, WHITE, WINDOWWIDTH/2, WINDOWHEIGHT/2+20)
    screen.blit(startSurf, startRect)
    screen.blit(pressSurf, pressRect)

def makeText(font, text, color, bgcolor, top, left):
    # create the Surface and Rect objects for some text.
    textSurf = font.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return (textSurf, textRect)

def setRound():
    friend_list = ['Na', 'Cl']
    return friend_list
    
def terminate():
    pygame.quit()
    sys.exit()

def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back


if __name__ == '__main__':
    main()

    
class Player:
  def __init__(self, x, y, vX, vY):
    self.x = x
    self.y = y
    self.vX = 1
    self.vY = 0

  def updateDir():
    print("Hello my name is " + self.name)
