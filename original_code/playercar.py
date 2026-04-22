import pygame

class PlayerCar:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # load your image
        self.image = pygame.image.load("image/car_image.png")
        self.image = pygame.transform.scale(self.image, (50, 100))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))