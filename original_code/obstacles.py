import pygame
import random



# Subtask II.A: Obstacle Class

class Obstacle:
    def __init__(self, road_x, road_width):
        # II.A.1: Random horizontal position
        self.width = 50
        self.height = 90
        self.x = random.randint(road_x, road_x + road_width - self.width)
        self.y = -self.height

        self.speed = 3

        self.image = pygame.image.load("../image/obstacle1.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))


    def move(self):
        self.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    # Check if off screen
    def is_off_screen(self, screen_height):
        return self.y > screen_height
