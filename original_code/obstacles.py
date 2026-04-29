import pygame
import random


# Subtask II.A: Obstacle Class

class Obstacle:
    def __init__(self, road_x, road_width):
        self.width = 85
        self.height = 100
        self.speed = 3
        # self.x = random.randint(road_x, road_x + road_width - self.width)

        lane_width = road_width // 3
        lane_number = random.randint(0, 2)

        # center the obstacle inside one of the 3 lanes
        self.x = road_x + lane_number * lane_width + (lane_width - self.width) // 2
        self.y = -self.height


        self.image = pygame.image.load("../image/obstacle001.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))


    def move(self):
        self.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    # Check if off screen
    def is_off_screen(self, screen_height):
        return self.y > screen_height
