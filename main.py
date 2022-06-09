import pygame
import os
pygame.font.init()
pygame.mixer.init()

#גודל החלון
WIDTH, HEIGHT = 900, 500
# הגדרת החלון
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPACESHIPS!")

#צבעים
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

#גבול אמצע
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

#הגדרת צלילים
BULLET_HIT_SOUND = pygame.mixer.Sound('Assets/Grenade+1.mp3')
BULLET_FIRE_SOUND = pygame.mixer.Sound('Assets/Gun+Silencer.mp3')

#הגדרת פונטים
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

FPS = 60 # Frame Per Second -  מהירות
VEL = 5 # size of spaceship movement - גודל התנועה של חלילית
BULLET_VEL = 7 #size of bullet movement - גודל התנועה של כדור
MAX_BULLETS = 3 # max bullets can shoot - מספר הכדורים שחללית יכולה לירות במקביל
HEALTH = 10
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40 # size of spaceship - גודל של החללית


YELLOW_HIT = pygame.USEREVENT + 1 
RED_HIT = pygame.USEREVENT + 2

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))


def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    # draw SPACE
    # draw BORDER
    # draw health red
    # draw health yellow
    # draw YELLOW_SPACESHIP
    # draw RED_SPACESHIP
    # draw red_bullets
    # draw yellow_bullets
    pygame.display.update()


def yellow_handle_movement(keys_pressed, yellow):
    pass
    # if LEFT: check the WIDTH
    # if RIGHT: check the BORDER
    # if UP : > 0 
    # if DOWN: check the HEIGHT


def red_handle_movement(keys_pressed, red):
    pass
    # if LEFT: check the BORDER
    # if RIGHT: check the WIDTH 
    # if UP : > 0 
    # if DOWN: check the HEIGHT



def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    pass
    # move yellow_bullets
    # check if yellow bullet hit the red - if yes remove and create an event
    # check if yellow bullet > WIDTH - if yes remove
    
    # move red_bullets
    # check if red bullet hit the yellow - if yes remove and create an event
    # check if red bullet < 0 - if yes remove
    

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                         2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    red = pygame.Rect(WIDTH/9*7, HEIGHT/2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(WIDTH/9, HEIGHT/2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    red_bullets = []
    yellow_bullets = []

    red_health = HEALTH
    yellow_health = HEALTH

    clock = pygame.time.Clock()
    run = True
    while run:
        pass

    main()


if __name__ == "__main__":
    main()
