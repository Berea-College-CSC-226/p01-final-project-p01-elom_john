import pygame


class PlayerCar:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 90
        self.speed = 6

        # correct path to image
        self.image = pygame.image.load("../image/car_image.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))