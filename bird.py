"""
The classic game of flappy bird. Make with python
and pygame. Features pixel perfect collision using masks :o

Date Modified:  Jul 30, 2019
Author: Tech With Tim
Estimated Work Time: 5 hours (1 just for that damn collision)
"""
import pygame
import os




bird_images = [pygame.transform.scale2x(pygame.image.load(os.path.join("assets","bird" + str(x) + ".png"))) for x in range(1,4)]
max_rotation = 25
imgs = bird_images
rot_velocity = 20
animation_time = 5


class Bird:
    """
    Bird class representing the flappy bird
    """
    def __init__(self, x, y):
        """
        Initialize the object
        :param x: starting x pos (int)
        :param y: starting y pos (int)
        :return: None
        """
        self.x = x
        self.y = y
        self.tilt = 0 
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = imgs[0]

    def jump(self):
        """
        make the bird jump
        :return: None
        """
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        """
        make the bird move
        :return: None
        """
        self.tick_count += 1

        displacement = self.vel*(self.tick_count) + 0.5*(3)*(self.tick_count)**2  # calculate displacement

        if displacement >= 16:
            displacement = (displacement/abs(displacement)) * 16

        if displacement < 0:
            displacement -= 2

        self.y = self.y + displacement

        if displacement < 0 or self.y < self.height + 50:
            if self.tilt < max_rotation:
                self.tilt = max_rotation
        else:  
            if self.tilt > -90:
                self.tilt -= rot_velocity

    def blitRotateCenter(self, surf, image, topleft, angle):
        """
        Rotate a surface and blit it to the window
        :param surf: the surface to blit to
        :param image: the image surface to rotate
        :param topLeft: the top left position of the image
        :param angle: a float value for angle
        :return: None
        """
        rotated_image = pygame.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

        surf.blit(rotated_image, new_rect.topleft)

    def draw(self, win):
        """
        draw the bird
        :param win: pygame window or surface
        :return: None
        """
        self.img_count += 1

        if self.img_count <= animation_time:
            self.img = imgs[0]
        elif self.img_count <= animation_time*2:
            self.img = imgs[1]
        elif self.img_count <= animation_time*3:
            self.img = imgs[2]
        elif self.img_count <= animation_time*4:
            self.img = imgs[1]
        elif self.img_count == animation_time*4 + 1:
            self.img = imgs[0]
            self.img_count = 0

        if self.tilt <= -80:
            self.img = imgs[1]
            self.img_count = animation_time*2

        self.blitRotateCenter(win, self.img, (self.x, self.y), self.tilt)

    def get_mask(self):
        """
        gets the mask for the current image of the bird
        :return: None
        """
        return pygame.mask.from_surface(self.img)



