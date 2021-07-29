import pygame
from random import randint
from time import sleep

pygame.init()

WIDTH = 500
HEIGHT = 500

#size of each seg
SIZE = 10

SEG_COLOR = (255, 0, 0)

FOOD_COLOR = (0, 255, 0)

BG_COLOR = (0, 0, 0)

FPS = 60

clock = pygame.time.Clock()

scr = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Welcome to Snake')

#snake is a list of rects and the direction of the head

#0 = up, 90 = right, 180 = down, 270 = left
dir = 90

segs = []

food = []

AMT_FOOD = 1

def start():
    global dir
    global segs
    global food
    segs.append(pygame.Rect(WIDTH / 2, HEIGHT / 2, SIZE, SIZE))    
    add_food()
    frames = 0
    run = True
    rep = True

    while run:
        frames += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                rep = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if dir != 90:
                        dir = 270
                if event.key == pygame.K_RIGHT:
                    if dir != 270:    
                        dir = 90
                if event.key == pygame.K_UP:
                    if dir != 180:
                        dir = 0
                if event.key == pygame.K_DOWN:
                    if dir != 0:
                        dir = 180
                if event.key == pygame.K_a:
                    add_seg()
                if event.key == pygame.K_ESCAPE:
                    run = False
                    rep = False
        print("")
        if frames == 10:        
            frames = 1
            pygame.display.set_caption("Score: " + str(len(segs)))    
            eat()
            add_food()
            move() 
            draw()
            if run == True:
                run = not(game_over())
        clock.tick(FPS)

    pygame.display.set_caption("Score: " + str(len(segs)) + ". Press ENTER to play again, ESC to exit.") 



    while rep:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    segs = []
                    food = []
                    dir = 90
                    start()
                    rep = False
                if event.key == pygame.K_ESCAPE:
                    rep = False
 

    

def draw():
    scr.fill(BG_COLOR)

    for f in food:
        pygame.draw.rect(scr, FOOD_COLOR, f)

    for s in segs:
        pygame.draw.rect(scr, SEG_COLOR, s) 
    
    pygame.display.flip()

def move():

    prevx = segs[0].x
    prevy = segs[0].y

    if dir == 90:
        segs[0] = segs[0].move(10, 0)
    elif dir == 270:
        segs[0] = segs[0].move(-10, 0)
    elif dir == 0:
        segs[0] = segs[0].move(0, -10)
    elif dir == 180:
        segs[0] = segs[0].move(0, 10)

    if len(segs) > 1:
        for i in range(1, len(segs)):
            x = prevx
            y = prevy
            prevx = segs[i].x
            prevy = segs[i].y
            segs[i] = segs[i].move(x - prevx, y - prevy)

def add_seg():
    segs.append(segs[len(segs) - 1].copy())

def game_over():
    for i in segs:
        for j in segs:
            if not(i is j) and ((i.x == j.x) and (i.y == j.y)):
                print("seg collision")
                return True

    if segs[0].x > WIDTH or segs[0].x < 0 or segs[0].y > HEIGHT or segs[0].y < 0:
        print("out of bounds")
        return True

def add_food():
    if len(food) < AMT_FOOD:
        x = randint(0, WIDTH/SIZE - 1)
        y = randint(0, HEIGHT/SIZE - 1)

        food.append(pygame.Rect(x*SIZE, y*SIZE, SIZE, SIZE))

def eat():
    for f in food:
        if (f.x == segs[0].x) and (f.y == segs[0].y):
            food.remove(f)
            add_seg() 


















start()



