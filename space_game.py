import pygame
import os


width=900
height=500
white=(255,255,255)
fps=32
vel=5
spaceshipwidth=55
spaceshipheight=40

win=pygame.display.set_mode((width,height))
pygame.display.set_caption("Space Game")

yellowspaceship=pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
redspaceship=pygame.image.load(os.path.join('Assets','spaceship_red.png'))
yellowspaceimage=pygame.transform.rotate( pygame.transform.scale(yellowspaceship,(spaceshipwidth,spaceshipheight)),90 )
redspaceimage=pygame.transform.rotate( pygame.transform.scale(redspaceship,(spaceshipwidth,spaceshipheight)),270 )

def window(red,yellow):
    win.fill(white)
    win.blit(yellowspaceimage,(yellow.x,yellow.y))
    win.blit(redspaceimage,(red.x,red.y))
    pygame.display.update()

def main():
    red = pygame.Rect(700, 300, spaceshipwidth,spaceshipheight)
    yellow = pygame.Rect(100, 300, spaceshipwidth,spaceshipheight)

    run=True
    clock=pygame.time.Clock()
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                 run=False

        key_pressed=pygame.key.get_pressed()
        if key_pressed[pygame.constants.K_a]:
            yellow.x-=vel
        if key_pressed[pygame.constants.K_d]:
            yellow.x+=vel
        if key_pressed[pygame.constants.K_w]:
            yellow.y-=vel
        if key_pressed[pygame.constants.K_s]:
            yellow.y+=vel

        window(red,yellow)
        
    pygame.quit()


if __name__ == "__main__":
    main()
