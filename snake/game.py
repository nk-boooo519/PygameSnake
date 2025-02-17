from snake import Snake
import pygame


def game(screen):
    # todo: (сделать окно) make window
    # todo: доделать змейку
    snake = Snake("Змея")
    running = True
    while running:
         for event in pygame.event.get():
         # закрытие окна
             if event.type == pygame.QUIT:
                 running = False
         snake.draw(screen,5,1)
         pygame.display.flip()
