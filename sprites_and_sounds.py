import pygame
import sys, random, time
from pygame.locals import *

# PyGame setting
pygame.init()
main_clock = pygame.time.Clock()

# window setting
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
window_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Спрайты и звуки')

# Color setting
WHITE = (255, 255, 255)

# creating user's sturctures and 'food'
food_counter = 0
NEWFOOD = 40
player = pygame.Rect(300, 100, 40, 40)
player_image = pygame.image.load('player.png')
player_stretched_image = pygame.transform.scale(player_image, (40, 40))
food_image = pygame.image.load('cherry.png')
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 20), random.randint(0, WINDOWHEIGHT - 20), 20, 20))

# creation movement variables
move_left = False
move_right = False
move_up = False
move_down = False

MOVESPEED = 6

# music setting
pick_up_sound = pygame.mixer.Sound('pickup.wav')
pygame.mixer.music.load('fioletovoe.mp3')
pygame.mixer.music.play(-1, 0.0)
music_playing = True

# gamecycle initialization
while True:
    # check conditions
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # change of keyboard variables
            if event.key == K_LEFT or event.key == K_a:
                move_right = False
                move_left = True

            if event.key == K_RIGHT or event.key == K_d:
                move_left = False
                move_right = True
            if event.key == K_UP or event.key == K_w:
                move_down = False
                move_up = True
            if event.key == K_DOWN or event.key == K_s:
                move_up = False
                move_down = True

        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                move_left = False
            if event.key == K_RIGHT or event.key == K_d:
                move_right = False
            if event.key == K_UP or event.key == K_w:
                move_up = False
            if event.key == K_DOWN or event.key == K_s:
                move_down = False
            if event.key == K_x:
                player.top = random.randint(0, WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH - player.width)
            if event.key == K_m:
                if music_playing:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                music_playing = not music_playing

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0], event.pos[1], 20, 20))
    
    food_counter += 1
    if food_counter >= NEWFOOD:
        # adding new food
        food_counter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 20), random.randint(0, WINDOWHEIGHT - 20), 20, 20))        

    # creating white background
    window_surface.fill(WHITE)        

    # player movement
    if move_down and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if move_up and player.top > 0:
        player.top -= MOVESPEED
    if move_left and player.left > 0:
        player.left -= MOVESPEED
    if move_right and player.right < WINDOWWIDTH:
        player.right += MOVESPEED

    # Displaying player on surface 
    window_surface.blit(player_stretched_image, player)
    
    # check if player intersect with 'food'
    for food in foods[:]: # make quick copy of list food 
        if player.colliderect(food):
            foods.remove(food)
            player = pygame.Rect(player.left, player.top, player.width, player.height)
#            player_stretched_image = pygame.transform.scale(player_image, (player.width, player.height))
            if music_playing:
                pick_up_sound.play()
                
    # displaying food
    for food in foods:
        window_surface.blit(food_image, food)

    # displaying window on the screen
    pygame.display.update()
    main_clock.tick(40)

