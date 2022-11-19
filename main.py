# #!/usr/bin/python3.4
# --------- Import Modules --------- # 

import sys, os 

from SaveLoadManager import SaveLoadSystem #SaveLoad Archive
import pygame, sys
from pygame import mixer

import time
from time import sleep
from random import randint
from pathlib import Path

# --------- Global Constants --------- # 
altura = 1067
largura = 600

# --------- Config Pyinstaller (to launch EXE file) --------- # 
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# --------- Loading External Modules With VirtualEnv --------- # 
file_path = 'lib/site-packages/'
sys.path.append(os.path.dirname(file_path))

# --------- SETUP PYGAME (Window) --------- # 
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
mixer.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500),0,32)

font = pygame.font.SysFont(None, 20)
    
window = pygame.display.set_mode((altura, largura))
pygame.display.set_caption("Farm Clicker")
running = True

HERE = Path(__file__).parent #PATH do jogo

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False


# --------- Game Menu --------- # 
def main_menu():
    while True:
        background = pygame.image.load(HERE / 'assets/background.png')
        window.blit(background, (0, 0))

        font = pygame.font.SysFont(None, 45)

        rect = pygame.Surface((largura/2.5,altura), pygame.SRCALPHA, 32)
        rect.fill((0, 0, 0, 80))
        screen.blit(rect, (largura/19, 0))
        draw_text('Main Menu', font, (0, 0, 0), screen, largura/19+35, 40)
        


        mx, my = pygame.mouse.get_pos()

        #buttons and black rect
        button_start = pygame.image.load(HERE / 'assets/start.png')
        button_start = pygame.transform.scale(button_start, (256,168))
        window.blit(button_start, (20, 40))
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_settings = pygame.image.load(HERE / 'assets/settings.png')
        button_settings = pygame.transform.scale(button_settings, (256,168))
        window.blit(button_settings, (20, 140))
        button_2 = pygame.Rect(50, 200, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()

        #Buttons Location rect
        #pygame.draw.rect(screen, (255, 0, 0), button_1)
        #pygame.draw.rect(screen, (255, 0, 0), button_2)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

# --------- Game Running --------- # 
def game():
    cooldown = True
    farmer = 0
    woodcutter = 0
    contador = 0
    new_contador = str(0)
    font = pygame.font.SysFont(None, 45)
    dinheiro_interface = font.render("Dinheiro: " + new_contador, True, (0, 255,0))
    farmers = font.render("Farmers: " + str(farmer), True, (0, 0,0))
    woodcutters = font.render("Woodcutters: " + str(woodcutter), True, (0, 255,0))
    buy1 = font.render('Farmer $500', True, (0,0,0))
    buy2 = font.render('Woodcutter $5000', True, (0,0,0))
    running = True
    while running:
        #SaveLoad - Load variables
        contador = saveloadmanager.Load_game_data(["money"], [[]])
        new_contador = str(contador)
        dinheiro_interface = font.render("Dinheiro: " + new_contador, True, (0, 255,0))

        # Background Game Loading
        class fundo(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.ImagemCrops1 = pygame.image.load(HERE / 'assets/inverno.png')
                self.ImagemCrops2 = pygame.image.load(HERE / 'assets/primavera.png')
                self.ImagemCrops3 = pygame.image.load(HERE / 'assets/verao.png')
                self.ImagemCrops4 = pygame.image.load(HERE / 'assets/outono.png')
                
                self.ListaImagens = [self.ImagemCrops1, self.ImagemCrops2, self.ImagemCrops3, self.ImagemCrops4]
                self.posImagem = 0
                self.ImagemFundo = self.ListaImagens[self.posImagem]

                self.rect = self.ImagemFundo.get_rect()
                self.rect.centerx = largura -67
                self.rect.centery = altura -767

                self.configTempo = 1

            # Accountant to change seasons
            def comportamento (self, tempo):
                if self.configTempo == tempo:
                    self.posImagem += 1
                    self.configTempo += 10
                    if self.posImagem > len(self.ListaImagens)-1:
                        self.posImagem = 0
                    
            # Change Seasons
            def colocar(self, superficie):
                self.ImagemFundo = self.ListaImagens[self.posImagem]
                superficie.blit(self.ImagemFundo, self.rect)
                window.blit(dinheiro_interface,
                (500 - dinheiro_interface.get_width() // 2, 100 - dinheiro_interface.get_height() // 2))
                window.blit(buy1, (45, 60))
                window.blit(dinheiro_interface,
                (5000 - dinheiro_interface.get_width() // 2, 100 - dinheiro_interface.get_height() // 2))
                window.blit(buy2, (45, 120))

                window.blit(farmers,
                (5000 - dinheiro_interface.get_width() // 2, 100 - dinheiro_interface.get_height() // 2))
                window.blit(farmers, (750, 60))

                window.blit(woodcutters,
                (5000 - dinheiro_interface.get_width() // 2, 100 - dinheiro_interface.get_height() // 2))
                window.blit(woodcutters, (750, 120))

        # Image Crops Loading
        class crops1(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.ImagemCrops1 = pygame.image.load(HERE / 'assets/crop1.png')
                self.ImagemCrops2 = pygame.image.load(HERE / 'assets/crop2.png')
                self.ImagemCrops3 = pygame.image.load(HERE / 'assets/crop3.png')
                self.ImagemCrops4 = pygame.image.load(HERE / 'assets/crop4.png')

                self.ListaImagens = [self.ImagemCrops1, self.ImagemCrops2, self.ImagemCrops3, self.ImagemCrops4]
                self.posImagem = 0
                self.ImagemCrops = self.ListaImagens[self.posImagem]

                self.rect = self.ImagemCrops.get_rect()
                self.rect.centerx = largura +10
                self.rect.centery = altura -740

                self.configTempo = 10

            # Accountant to change crops
            def comportamento (self, tempo):
                if self.configTempo == tempo:
                    self.posImagem += 1
                    self.configTempo += 10
                    if self.posImagem > len(self.ListaImagens)-1:
                        self.posImagem = 0
                    
            # Change Crops
            def colocar(self, superficie):
                self.ImagemCrops = self.ListaImagens[self.posImagem]
                superficie.blit(self.ImagemCrops, self.rect)

        # Image Crops Loading 2
        class crops2(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.ImagemCrops1 = pygame.image.load(HERE / 'assets/crop1.png')
                self.ImagemCrops2 = pygame.image.load(HERE / 'assets/crop2.png')
                self.ImagemCrops3 = pygame.image.load(HERE / 'assets/crop3.png')
                self.ImagemCrops4 = pygame.image.load(HERE / 'assets/crop4.png')
                
                self.ListaImagens = [self.ImagemCrops1, self.ImagemCrops2, self.ImagemCrops3, self.ImagemCrops4]
                self.posImagem = 0
                self.ImagemCrops = self.ListaImagens[self.posImagem]

                # Accountant to change crops 2
                self.rect = self.ImagemCrops.get_rect()
                self.rect.centerx = largura + 160
                self.rect.centery = altura - 740

                self.configTempo = 10
                
            # Image Crops Loading 2
            def comportamento (self, tempo):
                if self.configTempo == tempo:
                    self.posImagem += 1
                    self.configTempo += 10
                    if self.posImagem > len(self.ListaImagens)-1:
                        self.posImagem = 0
                    

            def colocar(self, superficie):
                self.ImagemCrops = self.ListaImagens[self.posImagem]
                superficie.blit(self.ImagemCrops, self.rect)

        # FUNCTION IMAGES OPERATION
        fundo = fundo()
        crop1 = crops1()
        crop2 = crops2()
        pygame.display.update()

                    
        # --------- MAIN LOOP --------- # 
        while running:
            if cooldown is False:
                timing += 1
                if timing > 30:
                    cooldown = True
            tempo = int(pygame.time.get_ticks()/1000)
            Rectplace = pygame.draw.rect(window, (0, 255, 0),(560, 280, 100, 100))
            Rectplace2 = pygame.draw.rect(window, (0, 255, 0),(710, 280, 100, 100))
            Rectplace3 = pygame.draw.rect(window, (0, 255, 0),(55, 40, 100, 100))
            Rectplace4 = pygame.draw.rect(window, (0, 255, 0),(55, 70, 100, 100))
            dinheiro_interface = font.render("Dinheiro: " + new_contador, True, (0, 255,0))
            farmers = font.render("Farmers: " + str(farmer), True, (0, 255,0))
            woodcutters = font.render("Woodcutters: " + str(woodcutter), True, (0, 255,0))

            # Mouse position and button clicking.
            pos = pygame.mouse.get_pos()
            pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
            fundo.colocar(window)
            fundo.comportamento(tempo)
            crop1.colocar(window)
            crop1.comportamento(tempo)
            crop2.colocar(window)
            crop2.comportamento(tempo)
            pygame.display.update()
            
            # Check if the rect collided with the mouse pos
            # and if the left mouse button was pressed.
            if Rectplace.collidepoint(pos) and pressed1:
                if cooldown is True:
                    contador = contador+(randint(30,50))
                    new_contador = str(contador)
                    dinheiro_interface = font.render("Dinheiro: " + new_contador, True, (0, 255,0))
                    pygame.mixer.music.load(HERE / 'sons/click.ogg')
                    mixer.music.play()
                    print("Dinheiro:",contador)
                    cooldown = False
                    timing = 0
                    
                    for i in range(1):
                        t0 = time.time()
                        i = i+1
                        Rectplace = pygame.draw.rect(window, (0, 0, 0),(560, 280, 100, 100))
                        #ADICIONAR EFEITO DE CORTE
                        pygame.display.update()
                        t1 = time.time()
                        total = t1-t0
                        print('Você demorou',int(total)+2,'minutos para colher')
                        print(i)
                        if i == 10:
                            print('coroio')

            if Rectplace2.collidepoint(pos) and pressed1:
                if cooldown is True:
                    contador = contador+(randint(150,350))
                    new_contador = str(contador)
                    dinheiro_interface = font.render("Dinheiro: " + new_contador, True, (0, 255,0))
                    pygame.mixer.music.load(HERE / 'sons/click.ogg')
                    mixer.music.play()
                    print("Dinheiro:",contador)
                    cooldown = False
                    timing = -60
                    print(type(contador))

                    for i in range(1):
                        t0 = time.time()
                        i = i+1
                        Rectplace2 = pygame.draw.rect(window, (0, 0, 0),(710, 280, 100, 100))
                        pygame.display.update()
                        t1 = time.time()
                        total = t1-t0
                        print('Você demorou',int(total)+6,'minutos para colher')
                        if i > 10:
                            print('batata')

            if Rectplace3.collidepoint(pos) and pressed1:
                if contador > 500:
                    contador = contador - 500
                    new_contador = str(contador)
                    dinheiro_interface = font.render("Dinheiro: " + new_contador, True, (0, 255,0))
                    farmer += 1
                    pygame.mixer.music.load(HERE / 'sons/click.ogg')
                    mixer.music.play()
                    farmers = font.render("Farmers: " + str(farmer), True, (0, 255,0))

            if Rectplace4.collidepoint(pos) and pressed1:
                if contador > 5000:
                    contador = contador - 5000
                    new_contador = str(contador)
                    dinheiro_interface = font.render("Dinheiro: " + new_contador, True, (0, 255,0))
                    woodcutter += 1
                    pygame.mixer.music.load(HERE / 'sons/click.ogg')
                    mixer.music.play()
                    woodcutters = font.render("Woodcutters: " + str(farmer), True, (0, 255,0))

            while farmer > 0:
                contador = contador + int(farmer*1)
                new_contador = str(contador)
                dinheiro_interface = font.render("Dinheiro: " + new_contador, True, (0, 255,0))
                break

            while woodcutter > 0:
                contador = contador + int(woodcutter*5)
                new_contador = str(contador)
                dinheiro_interface = font.render("Dinheiro: " + new_contador, True, (0, 255,0))
                break
                      
            #QUIT ESC
            for event in pygame.event.get():
                if event.type == QUIT:
                    saveloadmanager.save_game_data([contador], ["money"])
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        saveloadmanager.save_game_data([contador], ["money"])
                        running = False
        
        pygame.display.update()
        mainClock.tick(60)

# --------- Game Settings Menu --------- # 
def options():
    running = True
    while running:
        #from Settings import settings_menu 
        background_settings = pygame.image.load(HERE / 'assets/background_settings.png')
        window.blit(background_settings, (0, 0))

        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

# --------- Run Game --------- # 
saveloadmanager = SaveLoadSystem(".save","save_data")
main_menu()
