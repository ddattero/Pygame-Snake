import pygame
from time import sleep

pygame.init()

WIDTH = 500
HEIGHT = 500

#size of each seg
SIZE = 10

SEG_COLOR = (255, 0, 0)

FOOD_COLOR = (0, 255, 0)

BG_COLOR = (0, 0, 0)

FPS = 5

clock = pygame.time.Clock()

scr = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Snake')

#snake is a list of rects and the direction of the head

#0 = up, 90 = right, 180 = down, 270 = left
dir = 90

segs = []

def start():
    segs.append(pygame.Rect(WIDTH / 2, HEIGHT / 2, SIZE, SIZE))

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dir = 270
                if event.key == pygame.K_RIGHT:
                    dir = 90
                if event.key == pygame.K_UP:
                    dir = 0
                if event.key == pygame.K_DOWN:
                    dir = 180

        
        move()
        draw()
        clock.tick(FPS)
        

    

def draw():
    scr.fill(BG_COLOR)

    for s in segs:
        pygame.draw.rect(scr, SEG_COLOR, s)
    
    pygame.display.flip()

def move():
    print(dir)
    if dir == 90:
        segs[0] = segs[0].move(10, 0)
    elif dir == 270:
        segs[0] = segs[0].move(-10, 0)
    elif dir == 0:
        segs[0] = segs[0].move(0, -10)
    elif dir == 180:
        segs[0] = segs[0].move(0, 10)










































start()



