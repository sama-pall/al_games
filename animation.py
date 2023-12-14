import pygame
import sys
import time
from pygame.locals import *

# setting pygame
pygame.init()

# window setting
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
window_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Анимация')

# dimensional variables setting
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

M_SPD = 1

# color setting
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# creating data block structure
b1 = {'rect': pygame.Rect(300, 80, 50, 100), 'color': RED, 'dir': UPRIGHT}
b2 = {'rect': pygame.Rect(200, 210, 23, 20), 'color': GREEN, 'dir': UPLEFT}
b3 = {'rect': pygame.Rect(100, 150, 60, 60), 'color': BLUE, 'dir': DOWNLEFT}
boxes = [b1, b2, b3]

# game cycle launch
while True:
    # quit check 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # create white background
    window_surface.fill(WHITE)

    for b in boxes:
        # moving data block 
        if b['dir'] == DOWNLEFT:
            b['rect'].left -= M_SPD
            b['rect'].top += M_SPD
        if b['dir'] == DOWNRIGHT:
            b['rect'].left += M_SPD
            b['rect'].top += M_SPD
        if b['dir'] == UPLEFT:
            b['rect'].left -= M_SPD
            b['rect'].top -= M_SPD
        if b['dir'] == UPRIGHT:
            b['rect'].left += M_SPD
            b['rect'].top -= M_SPD

        # check if block is out of window
        if b['rect'].top < 0:
            # out of upper boundary
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT
        if b['rect'].bottom > WINDOWHEIGHT:
            # out of down boundary
            if b['dir'] == DOWNLEFT:
                b['dir'] = UPLEFT
            if b['dir'] == DOWNRIGHT:
                b['dir'] = UPRIGHT
        if b['rect'].left < 0:
            # out of left boundary
            if b['dir'] == DOWNLEFT:
                b['dir'] = DOWNRIGHT
            if b['dir'] == UPLEFT:
                b['dir'] = UPRIGHT
        if b['rect'].right > WINDOWWIDTH:
            # out of right boundary
            if b['dir'] == DOWNRIGHT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = UPLEFT

        # create block on surface
        pygame.draw.rect(window_surface, b['color'], b['rect'])

    # output to screen
    pygame.display.update()
    time.sleep(0.01)
