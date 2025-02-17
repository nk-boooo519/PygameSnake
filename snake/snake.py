import pygame, const



class Snake:
    def __init__(self, name):
        self.name = name
        self.size = 2  # with head
        self.score = 0

    def draw(self, screen, qx, qy):
        #pygame.draw.circle()
        pygame.draw.rect(screen, const.BLUE, (const.cord_size['x'], const.cord_size['y'], const.cord_size['w']* qx, const.cord_size['h']* qy))
        """ draw head """

    def eat(self):
        self.size += 1
        self.score += 1
