import pygame
from playercar import PlayerCar
from obstacles import Obstacle


class Game:
    def __init__(self):
        pygame.init()

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

        self.obstacles = []
        self.spawn_timer = 0

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


    def update_obstacles(self):
        self.spawn_timer += 1

        if self.spawn_timer > 50:
            self.obstacles.append(Obstacle(self.road_x, self.road_width))
            self.spawn_timer = 0

        for obstacle in self.obstacles:
            obstacle.move()

        self.obstacles = [
            obstacle for obstacle in self.obstacles
            if not obstacle.is_off_screen(self.height)
        ]

    def draw(self):
        # background (grass color)
        self.screen.fill((34, 139, 34))

        # draw road
        self.draw_road()

        #Draw the obstacles
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

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                self.player.move_left()

            if keys[pygame.K_RIGHT]:
                self.player.move_right()

            if self.player.x < self.road_x:
                self.player.x = self.road_x

            right_edge = self.road_x + self.road_width - self.player.width

            if self.player.x > right_edge:
                self.player.x = right_edge

            self.update_obstacles()
            self.draw()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()