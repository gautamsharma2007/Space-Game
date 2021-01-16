import pygame
import os
pygame.font.init()
pygame.mixer.init()

red_hit=pygame.USEREVENT+1
yellow_hit=pygame.USEREVENT+2

HEALTH_FONT = pygame.font.SysFont('comicsans',40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

width=900
height=500
white=(255,255,255)
black=(0,0,0)
yellowcolor=(255,255,0)
redcolor=(255,0,0)
fps=32
bullet_vel=7
vel=5
spaceshipwidth=55
spaceshipheight=40
max_bullet=3
red_bullets=[]
yellow_bullets=[]
border=pygame.Rect(width//2,0,10,height)

win=pygame.display.set_mode((width,height))
pygame.display.set_caption("Space Game")

yellowspaceship=pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
redspaceship=pygame.image.load(os.path.join('Assets','spaceship_red.png'))
yellowspaceimage=pygame.transform.rotate( pygame.transform.scale(yellowspaceship,(spaceshipwidth,spaceshipheight)),90 )
redspaceimage=pygame.transform.rotate( pygame.transform.scale(redspaceship,(spaceshipwidth,spaceshipheight)),270 )
space= pygame.transform.scale(pygame.image.load(os.path.join('Assets','space.png')),(width,height))

def window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health):
    win.fill(white)
    win.blit(space,(0,0))
    win.blit(yellowspaceimage,(yellow.x,yellow.y))
    win.blit(redspaceimage,(red.x,red.y))
    red_health_text = HEALTH_FONT.render(
        "Health: " + str(red_health), 1, white)
    yellow_health_text = HEALTH_FONT.render(
        "Health: " + str(yellow_health), 1, white)
    win.blit(red_health_text, (width - red_health_text.get_width() - 10, 10))
    win.blit(yellow_health_text, (10, 10))
    pygame.draw.rect(win,black,border)
    for bullet in red_bullets:
        pygame.draw.rect(win,redcolor,bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(win,yellowcolor,bullet)
    pygame.display.update()
def handle_bullets(red_bullets,yellow_bullets,red,yellow):
    for bullet in yellow_bullets:
        bullet.x+=bullet_vel
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(red_hit))
            yellow_bullets.remove(bullet)
        if bullet.x >width:
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x-=bullet_vel
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(yellow_hit))
            red_bullets.remove(bullet)
        if bullet.x <0:
            red_bullets.remove(bullet)
def yellow_movement(key_pressed,yellow):
    if key_pressed[pygame.constants.K_a] and yellow.x-vel>0:
        yellow.x-=vel
    if key_pressed[pygame.constants.K_d] and yellow.x+vel+spaceshipwidth<border.x:
        yellow.x+=vel
    if key_pressed[pygame.constants.K_w] and yellow.y-vel>0:
        yellow.y-=vel
    if key_pressed[pygame.constants.K_s] and yellow.y+vel+spaceshipheight<height:
        yellow.y+=vel
def red_movement(key_pressed,red):
    if key_pressed[pygame.constants.K_LEFT] and red.x-vel>border.x+10:
        red.x-=vel
    if key_pressed[pygame.constants.K_RIGHT] and red.x+vel+spaceshipwidth<width:
        red.x+=vel
    if key_pressed[pygame.constants.K_UP]and red.y-vel>0:
        red.y-=vel
    if key_pressed[pygame.constants.K_DOWN] and red.y+vel+spaceshipheight<height:
        red.y+=vel
def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, white)
    win.blit(draw_text, (width/2 - draw_text.get_width() /
                         2, height/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)
def main():
    red = pygame.Rect(700, 300, spaceshipwidth,spaceshipheight)
    yellow = pygame.Rect(100, 300, spaceshipwidth,spaceshipheight)
    red_health = 10
    yellow_health = 10
    run=True
    clock=pygame.time.Clock()
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                 run=False
            if event.type==pygame.KEYDOWN:
                if event.key== pygame.constants.K_LCTRL and len(yellow_bullets)<max_bullet:
                    bullet=pygame.Rect(yellow.x+yellow.width,yellow.y+spaceshipheight//2,10,5)
                    yellow_bullets.append(bullet)
                if event.key== pygame.constants.K_RCTRL and len(red_bullets)<max_bullet:
                    bullet=pygame.Rect(red.x,red.y+red.height//2,10,5)
                    red_bullets.append(bullet)
            if event.type == red_hit:
                red_health -= 1
                #BULLET_HIT_SOUND.play()

            if event.type == yellow_hit:
                yellow_health -= 1
                #BULLET_HIT_SOUND.play()

        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins!"

        if yellow_health <= 0:
            winner_text = "Red Wins!"

        if winner_text != "":
            draw_winner(winner_text)
            break

        key_pressed=pygame.key.get_pressed()
        handle_bullets(red_bullets,yellow_bullets,red,yellow)
        yellow_movement(key_pressed,yellow)
        red_movement(key_pressed,red)
        window(red,yellow,red_bullets,yellow_bullets,red_health,yellow_health)
        
    pygame.quit()


if __name__ == "__main__":
    main()
