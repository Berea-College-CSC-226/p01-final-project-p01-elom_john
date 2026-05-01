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
        self.rect = pygame.Rect(road_x, lane_width * lane_number, self.width, self.height)
        #self.rect = self.image.get_rect()
        #self.rect.move_ip(self.x, self.y)

        # center the obstacle inside one of the 3 lanes
        x = road_x + lane_number * lane_width + (lane_width - self.width) // 2
        y = -self.height


        self.image = pygame.image.load("../image/obstacle001.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # self.rect.inflate(-20, -25)

    def get_collision_rect(self):
        return self.rect.inflate(-30, -35)

    def move(self):
        self.rect.move_ip(0, self.speed)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # Check if off screen
    def is_off_screen(self, screen_height):
        return self.rect.top > screen_height
