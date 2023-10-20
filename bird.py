import pygame
import os

class Base:
    images = [pygame.transform.scale2x(pygame.image.load(os.path.join("assets","bird" + str(x) + ".png"))) for x in range(1,4)]
    max_rotation = 25
    velocity_rotation = 20
    animation_time = 5

    def __init__(self, x, y):
        """
        Initializes the bird class
        where x and y represents position of bird in
        cartesian finding
        """

        self.x = x
        self.y = y
        self.tilt = 0 
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.images[0]