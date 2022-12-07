import pygame
import time
import sys, os
from pathlib import Path

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


HERE = Path(__file__).parent #PATH do jogo

pygame.init()

class Efeito_sonoro():

    pygame.mixer.pre_init(44100, -16, 3, 10)
    pygame.mixer.set_num_channels(1)
    pygame.mixer.set_num_channels(2)
    pygame.mixer.set_num_channels(3)
    pygame.mixer.set_num_channels(4)

    def theme_1():
        s = pygame.mixer.Sound(HERE / 'sons/theme.ogg')
        s.play()

    def click_1():
        s1 = pygame.mixer.Sound(HERE / 'sons/click.ogg')
        s1.play()

    def click_2():
        s2 = pygame.mixer.Sound(HERE / 'sons/click2.ogg')
        s2.play()

    def desliga_1():
        s3 = pygame.mixer.Sound(HERE / 'sons/desliga.ogg')
        s3.play()