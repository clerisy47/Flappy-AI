import pygame
import os

class Base:
    """
    Represnts the moving floor of the game
    """
    

    def __init__(self, y):
        """
        Initialize the object
        :param y: int
        :return: None
        """
        self.VEL = 5
        base_img = pygame.transform.scale2x(pygame.image.load(os.path.join("assets","base.png")).convert_alpha())
        self.WIDTH = base_img.get_width()
        self.IMG = base_img
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):
        """
        move floor so it looks like its scrolling
        :return: None
        """
        self.x1 -= self.VEL
        self.x2 -= self.VEL
        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        """
        Draw the floor. This is two images that move together.
        :param win: the pygame surface/window
        :return: None
        """
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))