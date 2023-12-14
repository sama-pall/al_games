from curses import KEY_ENTER
import pygame, random, sys
from pygame.locals import *


WINDOWWIDTH = 600
WINDOWHEIGHT = 600
TEXTCOLOR = (0, 0, 0)
BACKGROUNDCOLOR = (255, 255, 255)
FPS = 40
BADDIEMINSIZE = 10
BADDIEMAXSIZE = 40
BADDIEMINSPEED = 1
BADDIEMAXSPEED = 6
ADDNEWBADDIERATE = 6
PLAYERMOVERATE = 5

def terminate():
    pygame.quit()
    sys.exit()

def wait_for_player_to_press_keys():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                elif event.key == K_KP_ENTER:# cycle goes infinitly unless Enter pressed
                    return 
            
def player_has_hit_baddie(player_rect, baddies):
    for b in baddies:
        if player_rect.colliderect(b['rect']):
            return True
    return False

def draw_text(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

       
# setting pygame, window and mouse
pygame.init()
main_clock = pygame.time.Clock()
window_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Ловкач')
pygame.mouse.set_visible(False)

# font setting
font = pygame.font.SysFont(None, 35)

# sounds setting
game_over_sound = pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('background.mp3')


# image setting
player_image = pygame.image.load('player.png')
player_rect = player_image.get_rect()
baddie_image = pygame.image.load('baddie.png')

# launching starting screen
window_surface.fill(BACKGROUNDCOLOR)
draw_text('Dodger', font, window_surface, (WINDOWWIDTH/10), (WINDOWHEIGHT/10))
draw_text('Press ENTER to start game', font, window_surface, (WINDOWWIDTH/5) - 30, (WINDOWHEIGHT/5) + 50)
draw_text('If you want to mute/unmute', font, window_surface, (WINDOWWIDTH/5) - 30, (WINDOWHEIGHT/5) + 100)
draw_text('background music press m', font, window_surface, (WINDOWWIDTH/5) - 30, (WINDOWHEIGHT/5) + 150)
draw_text('If you want to pause game press p', font, window_surface, (WINDOWWIDTH/5) - 30, (WINDOWHEIGHT/5) + 200)
pygame.display.update()
wait_for_player_to_press_keys()

top_score = 0
while True:
    # setting begining of game
    baddies = []
    score = 0
    player_rect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    move_left = move_right = move_up = move_down = False
    reverse_cheat = slow_cheat = False
    game_pause = False
    baddie_add_counter = 0
    pygame.mixer.music.play(-1, 0.0)

    music_mute = False
    

    while True: # game cycle is working while game is running
        score += 1
        # mute/unmute background music
        if music_mute:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

        while game_pause: # add game pause with infinit cycle while
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_p:
                            game_pause = not game_pause
                        if event.key == K_ESCAPE:
                            terminate()
                    if event.type == QUIT:
                        terminate()

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == K_z:
                    reverse_cheat = True
                if event.key == K_x:
                    slow_cheat = True
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
                # set game_pause to True so lauch infinite while
                if event.key == K_p:
                    game_pause = not game_pause
                # pause background music 
                if event.key == K_m:
                    music_mute = not music_mute
                   


            if event.type == KEYUP:
                if event.key == K_z:
                    reverse_cheat = False
                    score = 0
                if event.key == K_x:
                    slow_cheat = False
                    score = 0
                if event.key == K_ESCAPE:
                    terminate()

                if event.key == K_LEFT or event.key == K_a:
                    move_left = False
                if event.key == K_RIGHT or event.key == K_d:
                    move_right = False
                if event.key == K_UP or event.key == K_w:
                    move_up = False
                if event.key == K_DOWN or event.key == K_s:
                    move_down = False

            if event.type == MOUSEMOTION:
                # if mouse pointer is moving - move player to pointer
                player_rect.centerx = event. pos[0]
                player_rect.centery = event.pos[1]
        
        # if needed to add baddies at top side of screen
        if not reverse_cheat and not slow_cheat:
            baddie_add_counter += 1
        if baddie_add_counter == ADDNEWBADDIERATE:
            baddie_add_counter = 0
            baddie_size = random.randint(BADDIEMINSIZE, BADDIEMAXSIZE)
            new_baddie = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - baddie_size), 0 - baddie_size, baddie_size, baddie_size),
                          'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED), 
                          'surface': pygame.transform.scale(baddie_image, (baddie_size, baddie_size))}
            baddies.append(new_baddie)

        # player moves on screen
        if move_left and player_rect.left > 0:
            player_rect.move_ip(-1 * PLAYERMOVERATE, 0)
        if move_right and player_rect.right < WINDOWWIDTH:
            player_rect.move_ip(PLAYERMOVERATE, 0)
        if move_up and player_rect.top > 0:
            player_rect.move_ip(0, -1 *PLAYERMOVERATE)
        if move_down and player_rect.bottom < WINDOWHEIGHT:
            player_rect.move_ip(0, PLAYERMOVERATE)

        # baddies movement downwards
        for b in baddies:
            if not reverse_cheat and not slow_cheat:
                b['rect'].move_ip(0, b['speed'])
            elif reverse_cheat:
                b['rect'].move_ip(0, -5)
            elif slow_cheat:
                b['rect'].move_ip(0, 1)

        # removing baddies had fallen lower down line
        for b in baddies[:]:
            if b['rect'].top > WINDOWHEIGHT:
                baddies.remove(b)
        
        # displaying game world in game window
        window_surface.fill(BACKGROUNDCOLOR)

        # displaying score and best score
        draw_text('Score: %s' % (score), font, window_surface, 10, 0)
        draw_text('Top Score: %s' % (top_score), font, window_surface, 10, 40)

        # displaying player rect
        window_surface.blit(player_image, player_rect)

        # displaying every baddie
        for b in baddies:
            window_surface.blit(b['surface'], b['rect'])

        pygame.display.update()

        # check if any baddie got into player
        if player_has_hit_baddie(player_rect, baddies):
            if score > top_score:
                top_score = score # setting new record
            break
        main_clock.tick(FPS)

    # displaying game and str 'game over'
    pygame.mixer.music.stop()
    game_over_sound.play()

    draw_text('GAME OVER!', font, window_surface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
    draw_text('Press ENTER to start new game', font, window_surface, (WINDOWWIDTH / 3) - 120, (WINDOWHEIGHT / 3) + 50)
    pygame.display.update()
    wait_for_player_to_press_keys()

    game_over_sound.stop()


         
