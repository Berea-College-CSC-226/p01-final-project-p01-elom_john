import pygame


class PlayerCar(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.width = 40
        self.height = 70
        self.speed = 6

        # correct path to image
        self.image = pygame.image.load("../image/car_image.png")

        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)


    #Car movement
    def move_left(self):
        self.rect.move_ip(-self.speed, 0)

    def move_right(self):
        self.rect.move_ip(self.speed, 0)

    def draw(self, screen):
        screen.blit(self.image, self.rect)