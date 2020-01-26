import pygame, sys, random
from pygame.locals import *

import csv
import math
from random import seed
from random import randint


# seed random number generator
seed(1)

WINDOWWIDTH = 960
WINDOWHEIGHT = 620
FPS = 60

BASICFONTSIZE = 40
SMALLFONTSIZE = 20
SMALLERFONTSIZE = 15

DARK_WHITE = (5,5,5)
BLACK = (255,255,255)
YELLOW = pygame.Color("#47d4c4")
# YELLOW = pygame.Color("#737373")

# bgClr = pygame.Color('#ffe8e5')
bgClr = (255,255,255)

headerClr = pygame.Color("#737373")
# ALLCOMP = [{'Diamond': ['C',1]}, {'Salt': ['Na',1,'Cl',1]}, {'Glass': ['Si',1,'O',2]}, {'Sand': ['Si',1,'O',2]}, \
#             {'Water': ['H',2,'O',1]}, {'Ruby': ['Al',2,'O',3]}, {'Amethyst': ['Si',1,'O',2]}, \
#             {'Bleach': ['Na',1,'Cl',1,'O',1]}, {'Pearl': ['Ca',1,'C',1,'O',3]}, {'Carb': ['C',1,'H',2,'O',1]}, \
#             {'Natural Gas': ['C',1,'H',4]}, {'Baking soda':['Na',1,'H',1,'C',1,'O',3]}, \
#             {'Vinegar':['C',2,'H',4,'O',2]}, {'Alcohol':['C',2,'H',6,'O',1]}, \
#             {'Nailpaint remover': ['C',3,'H',6,'O',1]}, {'Glycerin': ['C',3,'H',8,'O',3]}, \
#             {'MSG': ['C',5,'H',8,'Na',1,'N',1,'O',4]}, {'Tylenol': ['C',8,'H',9,'N',1,'O',2]}, \
#             {'Vitamin C': ['C',6,'H',8,'O',6]}, {'TNT':['C',7,'H',5,'N',3,'O',6]}, {'Aspirin': ['C',9,'H',8,'O',4]}, \
#             {'Dopamine':['C',8,'H',11,'N',1,'O',2]}, {'Caffeine': ['C',8,'H',10,'N',4,'O',2]}]
            
ALLCOMP = {'Diamond':['C',1], 'Salt':['Na',1,'Cl',1], 'Glass': ['Si',1,'O',2], 'Sand': ['Si',1,'O',2], \
            'Water':['H',2,'O',1], 'Ruby': ['Al',2,'O',3], 'Amethyst': ['Si',1,'O',2], \
            'Bleach': ['Na',1,'Cl',1,'O',1], 'Pearl': ['Ca',1,'C',1,'O',3], 'Carb': ['C',1,'H',2,'O',1], \
            'Natural Gas': ['C',1,'H',4], 'Baking soda':['Na',1,'H',1,'C',1,'O',3], \
            'Vinegar':['C',2,'H',4,'O',2], 'Alcohol':['C',2,'H',6,'O',1], \
            'Nailpaint remover': ['C',3,'H',6,'O',1], 'Glycerin': ['C',3,'H',8,'O',3], \
            'MSG': ['C',5,'H',8,'Na',1,'N',1,'O',4], 'Tylenol': ['C',8,'H',9,'N',1,'O',2], \
            'Vitamin C': ['C',6,'H',8,'O',6], 'TNT':['C',7,'H',5,'N',3,'O',6], 'Aspirin': ['C',9,'H',8,'O',4], \
            'Dopamine':['C',8,'H',11,'N',1,'O',2], 'Caffeine': ['C',8,'H',10,'N',4,'O',2]}

# ALLCOMP = {'Diamond':['C',1], 'Salt':['Na',1,'Cl',1],'Glass': ['Si',1,'O',2],'Natural Gas': ['C',1,'H',4]}
CREATED = []
start_butt_width = 200
start_butt_height = 100
end_round_delay = 300
vPlayer = 5
enermies_max_speed = 3



def main():
    global FPSCLOCK, screen, BASICFONT, SMALLFONT, SMALLERFONT, score, from_csv

    from_csv = fromCsv()
    pygame.init()
    FPSCLOCK = pygame.time.Clock()

    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    score = 0
    pygame.display.set_caption('Chem_game')

    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)
    SMALLFONT = pygame.font.Font('freesansbold.ttf', SMALLFONTSIZE)
    SMALLERFONT = pygame.font.Font('freesansbold.ttf', SMALLERFONTSIZE)

    screen.fill(DARK_WHITE)
    # pygame.draw.rect(screen, WHITE, ((WINDOWWIDTH-start_butt_width)/2, (WINDOWWIDTH-start_butt_width)/2, start_butt_width, start_butt_height), 4)
    intro_font = pygame.font.Font('freesansbold.ttf', 70)
    introSurf, introRect = makeText(intro_font, "Chemistry Around Us", bgClr, DARK_WHITE, WINDOWWIDTH/2, WINDOWHEIGHT/2)
    introRect.center = (WINDOWWIDTH/2, WINDOWHEIGHT/2-90)
    startSurf, startRect = makeText(BASICFONT, "Start", bgClr, DARK_WHITE, WINDOWWIDTH/2, WINDOWHEIGHT/2)
    startRect.center = (WINDOWWIDTH/2, WINDOWHEIGHT/2)
    pressSurf, pressRect = makeText(SMALLFONT, "Press Enter to Start", DARK_WHITE, bgClr, WINDOWWIDTH/2+30, WINDOWHEIGHT/2+40)
    pressRect.center = (WINDOWWIDTH/2, WINDOWHEIGHT/2 + 100)
    screen.blit(introSurf, introRect)
    # screen.blit(startSurf, startRect)
    screen.blit(pressSurf, pressRect)

    

    # print('HERE')
    # for key, val in from_csv.items():
    #     hex_val = '#' + str(from_csv[key][4])
    #     print(key, hex_val)
    # print('END')
    
    while True:
        checkForQuit()
        win = False
        lose = False
        hintBool = False
        pause = False
        for event in pygame.event.get():
            # if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            #     pygame.quit()
            #     sys.exit()
            # pause = False
            if event.type == MOUSEBUTTONDOWN or (event.type == KEYUP and event.key == K_RETURN):
                # if (event.type == KEYDOWN and event.key == K)

                comp_name, f_ele, e_ele = setRound()                
                p = Player(WINDOWWIDTH/2, WINDOWHEIGHT/2, 1, 1)
                # for e in f_ele:
                #     p.name_dict[e.name] += 1
                all_ele = f_ele + e_ele
                # all_ele.append(p)
                all_ele_unique = []
                text = []
                f_dict = {}
                for e in all_ele:
                    if e.name not in f_dict.keys():
                        f_dict[e.name] = 1
                        # f_dict[e.name] = 1
                    else:
                        f_dict[e.name] += 1
                    if e.name not in text: 
                        text.append(e.name)
                        all_ele_unique.append(e)
                # all_ele_unique.append(p)
                # print('SET')
                # for e in all_ele_unique:
                #     print(e.name)
                # all_ele = f_ele + e_ele
                # all_ele.append(p)
                # print('F_DICT')
                # print(f_dict)
                lastEle = None
                while not lose:
                    # pause = checkForPause(pause)
                    # if pause:
                    #     displayPause()
                    #     continue

                    checkForQuit()
                    setBackground(comp_name)
                    showHint(comp_name, hintBool)
                    
                    # pause(pauseBool)
                    for event in pygame.event.get():
                        if event.type == KEYUP:
                            # keys = pygame.key.get_pressed()
                            if event.key == pygame.K_LEFT:
                                p.updateDir(-vPlayer,0)
                            elif event.key == pygame.K_RIGHT: #keys[K_RIGHT]:
                                p.updateDir(vPlayer,0)
                            elif event.key == pygame.K_UP: #keys[K_UP]:
                                p.updateDir(0,-vPlayer)
                            elif event.key == pygame.K_DOWN: #keys[K_DOWN]:
                                p.updateDir(0,vPlayer)   
                            elif event.key == pygame.K_h: #keys[K_H]:
                                hintBool = False
                            # elif event.key == pygame.K_q: #keys[K_H]:
                            #     pause = False
                        elif event.type == KEYDOWN:
                            if event.key == pygame.K_h:
                                hintBool = True
                            if event.key == K_p:
                                pause = not pause
                            # elif event.key == pygame.K_q: #keys[K_H]:
                            #     pause = True
                    if pause:
                        displayPause()
                        continue   
                    # all_ele = f_ele + e_ele + p
                    
                    # all_ele.append(p)

                    p.move()
                    # displayPlayer(p)

                    for e in all_ele_unique:
                        e.move()
                        
                    displayEle(all_ele_unique, p)
                    if lastEle:
                        ele_info(lastEle)

                    # print('F_ELE')
                    # for each in f_ele:
                    #     print(each.name)

                    for e in all_ele_unique:
                        if collide(p, e):                        
                            if e in e_ele:
                                lose = True
                                p.generateName()
                                displayEle(all_ele_unique, p)
                                # displayPlayer(p)
                                # pygame.time.delay(end_round_delay)
                                # loseGame()
                                break
                            else:
                                for i in range (len(f_ele)):
                                    if e.name == f_ele[i].name:
                                        lastEle = e.name
                                        f_ele.pop(i)
                                        break
                                        
                                ele_info(e.name)
                                p.updateDict(e.name)
                                p.generateName()
                                e.setRandom()
                                # print('Collide friend')

                                e_max = ALLCOMP[comp_name][ALLCOMP[comp_name].index(e.name)+1]
                                print(e.name + str(e_max))
                                if p.name_dict[e.name] > e_max:
                                # if p.name_dict[e.name] < 0:
                                    p.generateName()
                                    # displayPlayer(p)
                                    displayEle(all_ele_unique, p)
                                    # pygame.time.delay(end_round_delay)
                                    lose = True
                                    # loseGame()
                                    break
                            # elif e not in f_ele:
                            #     lose = True                                
                            #     loseGame()
                    if len(f_ele) == 0:
                        p.generateName()
                        # displayPlayer(p)
                        displayEle(all_ele_unique, p)
                        # pygame.time.delay(end_round_delay)
                        score += 1
                        CREATED.append(comp_name)
                        win = True
                        pygame.display.update()
                        FPSCLOCK.tick(FPS)
                        winGame(comp_name, win)
                        break
                                
                # displayEle(all_ele_unique, p)
                
                    pygame.display.update()
                    FPSCLOCK.tick(FPS)

                    winGame(comp_name, win)
                    loseGame(lose)
            
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def ele_info(name):
    hex_val = '#' + str(from_csv[name][4])
    # clr = pygame.Color(hex_val)
    clr = headerClr
    print(hex_val)
    pygame.draw.rect(screen, clr, (WINDOWWIDTH-160, 10, 140, 170), 4)

    sym_font = pygame.font.Font('freesansbold.ttf', 60)
    sym_surf, sym_rect = makeText(sym_font, name, clr, bgClr, WINDOWWIDTH-100, 90)

    name_font = pygame.font.Font('freesansbold.ttf', 30)
    name_surf, name_rect = makeText(name_font, from_csv[name][2], clr, bgClr, WINDOWWIDTH-85, 135)

    z_font = pygame.font.Font('freesansbold.ttf', 25)
    z_surf, z_rect = makeText(z_font, from_csv[name][0], clr, bgClr, WINDOWWIDTH-155, 20)

    mass_font = pygame.font.Font('freesansbold.ttf', 18)
    mass_surf, mass_rect = makeText(mass_font, str(round(float(from_csv[name][3])*100)/100), clr, bgClr, WINDOWWIDTH-140, 160)

    screen.blit(sym_surf, sym_rect)
    screen.blit(name_surf, name_rect)
    screen.blit(z_surf, z_rect)
    screen.blit(mass_surf, mass_rect)

    # pygame.display.update()
    # FPSCLOCK.tick(FPS)

def showHint(comp_name, status):
    if status:
        nameStr = ""
        # print(ALLCOMP[comp_name])
        for char in ALLCOMP[comp_name]:
            if char != 1:
                nameStr += str(char)
            # print(nameStr)
        hint_surf, hint_rect = makeText(SMALLFONT, nameStr, pygame.Color('#262626'), bgClr, 200, WINDOWHEIGHT-25)
        screen.blit(hint_surf, hint_rect)
        # pygame.display.update()
        # FPSCLOCK.tick(FPS)
    else:
        return

def loseGame(lose):
    if lose:
        screen.fill(DARK_WHITE)
        text_surf, text_rect = makeText(BASICFONT, 'YOU LOSE', bgClr, DARK_WHITE, WINDOWWIDTH/2, WINDOWHEIGHT/2)
        screen.blit(text_surf, text_rect)
        p_surf, p_rect = makeText(SMALLFONT, 'Press any key to retry', bgClr, DARK_WHITE, WINDOWWIDTH/2+50, WINDOWHEIGHT/2+30)
        screen.blit(p_surf, p_rect)
        lose = not lose
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return lose

def winGame(comp_name, win):
    if win:
        screen.fill(DARK_WHITE)
        con_surf, con_rect = makeText(BASICFONT, "CONGRATULATION!!! ", bgClr, DARK_WHITE, 80, WINDOWHEIGHT/2)
        # con_surf, con_rect = makeText(BASICFONT, "CONGRATULATION!!! ", bgClr, DARK_WHITE, 25, WINDOWHEIGHT/2)
        con_rect.center = (WINDOWWIDTH/2, 150)

        text_surf, text_rect = makeText(SMALLFONT, "You've made "+comp_name.upper(), bgClr, DARK_WHITE, WINDOWWIDTH/2, WINDOWHEIGHT/2)
        # text_surf, text_rect = makeText(SMALLFONT, "You've made "+comp_name.upper(), bgClr, DARK_WHITE, 35, WINDOWHEIGHT/2)
        chem_list = ALLCOMP[comp_name]

        chem_form = ''
        
        for i in range (0,len(chem_list),2):
            chem_form += str(chem_list[i])
            if chem_list[i+1] > 1:
                chem_form += str(chem_list[i+1])
                
        img = pygame.image.load(comp_name.lower()+'.png')
        img_small = pygame.transform.scale(img, (120, 120))
        screen.blit(img_small, (WINDOWWIDTH/2-60, WINDOWHEIGHT/2+120))
        p_surf, p_rect = makeText(SMALLFONT, 'Press any key to continue', bgClr, DARK_WHITE, WINDOWWIDTH/2, WINDOWHEIGHT-50)
        c_surf, c_rect = makeText(BASICFONT, chem_form, pygame.Color('#ff00ff'), DARK_WHITE, WINDOWWIDTH/2, WINDOWHEIGHT/2+50)
        screen.blit(con_surf, con_rect)
        screen.blit(c_surf, c_rect)
        screen.blit(p_surf, p_rect)
        screen.blit(text_surf, text_rect)
        win = not win
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return win
    
def displayEle(ele,player):
    for p in ele:
        hex_val = '#' + str(from_csv[p.name][4])
        print(from_csv[p.name])
        print(from_csv[p.name][4])
        print(hex_val)
        p_surf, p_rect = makeText(SMALLFONT, p.name, bgClr, pygame.Color(hex_val), p.x, p.y)
        pygame.draw.circle(screen, pygame.Color(hex_val), p_rect.center, 25)
        screen.blit(p_surf, p_rect)
    
    displayPlayer(player)
    # ele_info(ele)
    
    # pygame.display.update()
    # FPSCLOCK.tick(FPS)

def displayPlayer(p):
    player_font = pygame.font.Font('freesansbold.ttf', 35)
    p_surf, p_rect = makeText(player_font, p.name, YELLOW, bgClr, p.x, p.y)
    screen.blit(p_surf, p_rect)

    # pygame.display.update()
    # FPSCLOCK.tick(FPS)

def makeText(font, text, color, bgcolor, width, height):
    # create the Surface and Rect objects for some text.
    textSurf = font.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect.center = (width, height)
    return (textSurf, textRect)

def setRound():
    comp_name, f_chem_list = random.choice(list(ALLCOMP.items()))    
    while comp_name in CREATED:
        comp_name, f_chem_list = random.choice(list(ALLCOMP.items()))         
    # CREATED.append(comp_name)

    f_list = []
    for i in range (0, len(f_chem_list), 2):
        for j in range(f_chem_list[i+1]):
            f_list.append(f_chem_list[i])

    f_ele = []
    # f_dict = {}
    for name in f_list:
        new_ele = Element(name)
        # f_dict[name] += 1
        f_ele.append(new_ele)

    e_list = Enemy_list()
    e_list.populate_list(f_list)
    e_ele = []
    for name in e_list.enemy_list:
        new_ele = Element(name)
        e_ele.append(new_ele)
        
    # screen.fill(BLACK)
    baseSurf = screen.copy()
    for i in range(0, WINDOWWIDTH//2, 20):
        # animate the tile sliding over
        checkForQuit()
        screen.blit(baseSurf, (0, 0))
        pygame.draw.rect(screen, bgClr, (WINDOWWIDTH//2-i,0,2*i,WINDOWHEIGHT))

        pygame.display.update()
        FPSCLOCK.tick(FPS)

    # compound_text_surf, compound_text_rect = makeText(BASICFONT, 'Make '+comp_name+'!', DARK_WHITE, bgClr, WINDOWWIDTH/2, WINDOWHEIGHT/2)
    compound_text_surf, compound_text_rect = makeText(BASICFONT, 'Make '+comp_name+'!', headerClr, bgClr, WINDOWWIDTH/2, WINDOWHEIGHT/2)

    screen.blit(compound_text_surf, compound_text_rect)
    
    # pygame.display.update()
    # FPSCLOCK.tick(FPS)
 
    setBackground(comp_name)

    return [comp_name, f_ele, e_ele]

def setBackground(comp_name):
    screen.fill(BLACK)

    # score_surf, score_rect = makeText(SMALLFONT, 'Score: '+str(score), DARK_WHITE, bgClr, 40, 20)
    score_surf, score_rect = makeText(SMALLFONT, 'Score: '+str(score), headerClr, bgClr, 40, 20)
    comp_surf, comp_rect = makeText(BASICFONT, 'Make '+comp_name+'!', headerClr, bgClr, WINDOWWIDTH/2, 20)
    h_font = pygame.font.Font('freesansbold.ttf', 15)
    h_surf, h_rect = makeText(h_font, 'Hold H to see hint ', pygame.Color("#262626"), bgClr, 70, WINDOWHEIGHT-25)

    # h_rect.center = WINDOWWIDTH/2, 40`

    screen.blit(h_surf, h_rect)
    screen.blit(score_surf, score_rect)
    screen.blit(comp_surf, comp_rect)
    # pygame.display.update()
    # FPSCLOCK.tick(FPS)

def terminate():
    pygame.quit()
    sys.exit()
    
def checkForPause(pause):
    for event in pygame.event.get(KEYUP):
        # if event.type == KEYDOWN and event.key == K_p:
        if event.key == K_p:
            pause = not pause
    return pause
    
    # pygame.event.post(event)
    # return False

def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        # if event.key == K_q:
        #     pause()
    # for event in pygame.event.get(KEYDOWN): # get all the KEYUP events
    #     if event.key == K_q:
    #         pause() # termina
        pygame.event.post(event) # put the other KEYUP event objects back

def displayPause():
    # screen.fill((255,255,255,10))
    s = pygame.Surface((1000,750), pygame.SRCALPHA)   # per-pixel alpha
    s.fill((160,0,200,100))                         # notice the alpha value in the color
    screen.blit(s, (0,0))
    # screen.fill((220,0,220, 50))
    p_surf, p_rect = makeText(BASICFONT, 'PAUSE', DARK_WHITE, None, WINDOWWIDTH/2, 30)
    p_rect.center = (WINDOWWIDTH/2, 30)

    press_surf, press_rect = makeText(SMALLERFONT, 'Press P to resume', DARK_WHITE, None, WINDOWWIDTH/2,60)
    press_rect.center = (WINDOWWIDTH/2, 60)
    screen.blit(press_surf, press_rect)

    start_height = WINDOWHEIGHT/2-60+30
    i = 0

    press_surf, press_rect = makeText(SMALLFONT, "You've created ", DARK_WHITE, None, WINDOWWIDTH/2,80)
    press_rect.center = (WINDOWWIDTH/2, WINDOWHEIGHT/2-60)
    screen.blit(press_surf, press_rect)

    for ele in CREATED:
        ele_font = pygame.font.Font('freesansbold.ttf', 15)
        p_surf, p_rect = makeText(ele_font, ele, DARK_WHITE, None, WINDOWWIDTH/2, start_height + i*30)
        i += 1
        p_rect.center = (WINDOWWIDTH/2, start_height + i*30)
        # img = pygame.image.load(ele.lower()+'.png')
        # img_small = pygame.transform.scale(img, (30, 30))
        # screen.blit(img_small, (WINDOWWIDTH/2+30, start_height + i*30))
        screen.blit(p_surf, p_rect)
    
    # # once = False
    # for i in range(0, WINDOWWIDTH, 15):
    #     # animate the tile sliding over
    #     checkForQuit()
    #     screen.blit(baseSurf, (0, 0))
    #     pygame.draw.rect(screen, (220,220,220), (0,100,i,300))

    #     pygame.display.update()
    #     FPSCLOCK.tick(FPS)

    pygame.display.update()
    FPSCLOCK.tick(FPS)

def collide(p, e):
    if abs(p.x - e.x) <= 30 and abs(p.y - e.y) <= 30:
        return True
    else:
        return False

def fromCsv():
    all_elements = {}
    with open('all_elements.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV)
        for row in readCSV:
            all_elements[row[1]] = row
    # print(all_elements)
    return all_elements
    
class Player:
    def __init__(self, x, y, vX, vY):
        self.x = x
        self.y = y
        self.vX = 1
        self.vY = 0
        self.name_dict = {'Na':0,'Ca':0,'Al':0,'Si':0,'C':0,'H':0,'Cl':0,'O':0,'N':0}
        self.name = '#'

    def move(self):
        self.x += self.vX
        self.y += self.vY
        self.x = min(WINDOWWIDTH - 40, self.x)
        self.x = max(40, self.x)
        self.y = min(WINDOWHEIGHT - 40, self.y)
        self.y = max(90, self.y)

    def updateDir(self, v_X, v_Y):
        self.vX = v_X
        self.vY = v_Y
    
    def updateDict(self, e_name):
        self.name_dict[e_name] += 1

    def generateName(self):
        self.name = ''
        for ele, num in self.name_dict.items():
            if num == 1:
                self.name += ele
            elif num > 1:
                self.name += ele
                self.name += str(num)

class Element:
    def __init__(self, name):
        self.x = randint(40, WINDOWWIDTH - 40)
        self.y = randint(40, WINDOWHEIGHT - 40)
        while self.x >= WINDOWWIDTH / 2 - 50 and self.x <= WINDOWWIDTH / 2 + 50:
            self.x = randint(40, WINDOWWIDTH - 40)
        while self.y >= WINDOWHEIGHT / 2 - 50 and self.y <= WINDOWHEIGHT / 2 + 50:
            self.y = randint(40, WINDOWHEIGHT - 40)
        self.angle = randint(-180, 180)
        self.vX = round(math.cos(math.radians(self.angle))) * randint(1, enermies_max_speed)
        self.vY = round(math.sin(math.radians(self.angle))) * randint(1, enermies_max_speed)
        self.name = name

    def move(self):
        self.x += self.vX
        self.y += self.vY
        if (self.x >= WINDOWWIDTH - 40 or self.x <= 40):
            self.vX = -self.vX
        if (self.y >= WINDOWHEIGHT - 40 or self.y <= 40):
            self.vY = -self.vY
    
    def setRandom(self):
        self.x = randint(40, WINDOWWIDTH - 40)
        self.y = randint(40, WINDOWHEIGHT - 40)

class Enemy_list:
    def __init__(self):
        self.element = {'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', \
        'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', \
        'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', \
        'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', \
        'Ba', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', \
        'At', 'Rn', 'Fr', 'Ra', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', \
        'Fl', 'Mc', 'Lv', 'Ts', 'Og', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', \
        'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', \
        'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr'}
        self.enemy_list = []
    def populate_list(self, f_list):
        no_dup = self.element.copy()
        for e in f_list:
            # print(e)
            if e in no_dup:
                no_dup.remove(e)
        self.enemy_list = random.sample(no_dup, 6)



if __name__ == '__main__':
    main()
