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
        base_img = pygame.transform.scale2x(pygame.image.load(os.path.join("assets","base.png")).convert_alpha())
        self.vel = 5
        self.width = base_img.get_width()
        self.img = base_img
        self.y = y
        self.x1 = 0
        self.x2 = self.width

    def move(self):
        """
        move floor so it looks like its scrolling
        :return: None
        """
        self.x1 -= self.vel
        self.x2 -= self.vel
        if self.x1 + self.width < 0:
            self.x1 = self.x2 + self.width

        if self.x2 + self.width < 0:
            self.x2 = self.x1 + self.width

    def draw(self, win):
        """
        Draw the floor. This is two images that move together.
        :param win: the pygame surface/window
        :return: None
        """
        win.blit(self.img, (self.x1, self.y))
        win.blit(self.img, (self.x2, self.y))