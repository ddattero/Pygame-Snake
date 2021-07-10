import pygame
import time

pygame.init()

HEIGHT, WIDTH = 600, 600

scr = pygame.display.set_mode((HEIGHT, WIDTH))

SNAKE_DIMS = 20

snake = []

head_dir = "right"

def start():
	print("add first seg")
	add_seg()

	run = True

	while run:
		print("draw")
		draw()
		move()
		time.sleep(.1)


def add_seg():
	if len(snake) == 0:
		snake.append([0, 0])
	else:
		temp = snake[len(snake - 1)]
		move()
		snake.append(temp)

def move():
	
	if len(snake) > 1:
		for i in range(1, len(snake)):
			snake[len(snake) - i].x = snake[len(snake) - i - 1].x
			snake[len(snake) - i].y = snake[len(snake) - i - 1].y
	print((snake[0].x, snake[0].y, snake))
	if dir == "left":
		snake[0].move(90)
		snake[0].x = snake[0].x - SNAKE_DIMS
	elif dir == "right":
		snake[0].x = snake[0].x + SNAKE_DIMS
	elif dir == "up":
		snake[0].y = snake[0].y + SNAKE_DIMS
	elif dir == "down":
		snake[0].y = snake[0].y - SNAKE_DIMS

def draw():
	scr.fill("Black")
	for i in snake:
		pygame.draw.rect(scr, (255, 0, 0 ), i)
	
	pygame.display.update()



if __name__ == '__main__':
	start()