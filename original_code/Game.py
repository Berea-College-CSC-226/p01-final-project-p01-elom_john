import pygame
import random
from playercar import PlayerCar



class Obstacle:
    def __init__(self, screen_width):
        self.width = 50
        self.height = 80
        # Random horizontal position
        road_width = 300
        road_x = (screen_width - road_width) // 2

        self.x = random.randint(road_x, road_x + road_width - self.width)
        # Start near top
        self.y = -self.height
        #Load Image
        images = [
            pygame.image.load("../image/Obstacle1.jpg"),
            pygame.image.load("../image/Obstacle2.jpg"),
            pygame.image.load("../image/Obstacle3.jpg")
        ]
        self.image = random.choice(images)
        self.image = pygame.transform.scale(self.image, (50, 80))
        # Appearance
        self.speed = 2

    # Move obstacle downward
    def move(self):
        self.y += self.speed  # II.B.1

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))



    # Check if off-screen
    def is_off_screen(self, screen_height):
        return self.y > screen_height




class Game:
    def __init__(self):
        pygame.init()

        self.obstacles = []
        self.spawn_timer = 0
        self.width = 600
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Car Dodge Game")

        self.clock = pygame.time.Clock()
        self.running = True

        road_width = 300
        road_x = (self.width - road_width) // 2
        lane_width = road_width // 3

        # place car in middle lane
        car_x = road_x + lane_width + (lane_width - 50) // 2
        car_y = self.height - 120

        self.player = PlayerCar(car_x, car_y)

    def draw_road(self):
        road_width = 300
        road_x = (self.width - road_width) // 2

        # draw road
        pygame.draw.rect(self.screen, (50, 50, 50), (road_x, 0, road_width, self.height))

        # lane settings
        lane_color = (255, 255, 255)
        lane_width = 5
        dash_height = 20
        gap = 20

        # 3 lanes means 2 divider lines
        lane_size = road_width // 3
        line1_x = road_x + lane_size
        line2_x = road_x + 2 * lane_size

        for y in range(0, self.height, dash_height + gap):
            pygame.draw.rect(
                self.screen,
                lane_color,
                (line1_x - lane_width // 2, y, lane_width, dash_height)
            )
            pygame.draw.rect(
                self.screen,
                lane_color,
                (line2_x - lane_width // 2, y, lane_width, dash_height)
            )



    def draw(self):

        #Draw background
        self.screen.fill((34, 139, 34))

        #Draw road
        self.draw_road()

        #Draw obstacles
        for obstacle in self.obstacles:
                obstacle.draw(self.screen)

        #Draw car
        self.player.draw(self.screen)

        pygame.display.update()

    def run(self):
        while self.running:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.spawn_timer += 1
            if self.spawn_timer > 50:
                self.obstacles.append(Obstacle(self.width))
                self.spawn_timer = 0

            for obstacle in self.obstacles:
                obstacle.move()

            self.obstacles = [obs for obs in self.obstacles if not obs.is_off_screen(self.height)]

            self.draw()


        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()