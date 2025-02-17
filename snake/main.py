from turtledemo.penrose import start

import pygame
import pygame_menu
from pygame.event import event_name

import game

# todo: доделать меню
pygame.init()

vi = pygame.display.Info()
permission = (vi.current_w, vi.current_h)
screen = pygame.display.set_mode(permission)


def set_difficulty(value, difficulty):
    # Do the job here !
    pass



menu = pygame_menu.Menu('Welcome', 400, 400, theme=pygame_menu.themes.THEME_BLUE)
menu.add.text_input('Name :', default='John Doe')
menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Play', game.game(screen))
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(screen)

