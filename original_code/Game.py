import pygame
from playercar import PlayerCar
from obstacles import Obstacle


class Game:
    def __init__(self):
        pygame.init()

        self.spawn_timer = 0
        self.spawn_delay = 80
        self.difficulty_timer = 0
        self.obstacle_speed = 3

        self.width = 600
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Car Dodge Game")

        self.clock = pygame.time.Clock()
        self.running = True

        self.road_width = 300
        self.road_x = (self.width - self.road_width) // 2
        lane_width = self.road_width // 3

        # place car in middle lane
        car_x = self.road_x + lane_width + (lane_width - 50) // 2
        car_y = self.height - 120

        self.player = PlayerCar(car_x, car_y)

        self.obstacles = []

        self.obstacle_speed = 3
        self.difficulty_timer = 0

        self.score = 0
        self.font = pygame.font.SysFont("ComicSans", 20)

    def draw_road(self):
        road_width = self.road_width
        road_x = self.road_x

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
        self.difficulty_timer += 1

        # Increase difficulty over time
        if self.difficulty_timer > 300:
            self.obstacle_speed += 1
            self.difficulty_timer = 0

            if self.spawn_delay > 20:
                self.spawn_delay -= 5  # spawn faster over time

        # Spawn obstacles
        if self.spawn_timer > self.spawn_delay:
            new_obstacle = Obstacle(self.road_x, self.road_width)
            new_obstacle.speed = self.obstacle_speed
            self.obstacles.append(new_obstacle)
            self.spawn_timer = 0

        # Move obstacles
        for obstacle in self.obstacles:
            obstacle.move()

        # Remove off-screen
        self.obstacles = [
            obs for obs in self.obstacles
            if not obs.is_off_screen(self.height)
        ]


    def draw(self):
        # background (grass color)
        self.screen.fill((34, 139, 34))

        # draw road
        self.draw_road()

        self.draw_score()

        #Draw the obstacles
        for obstacle in self.obstacles:
            obstacle.draw(self.screen)

        #Draw car
        self.player.draw(self.screen)

        pygame.display.update()

    # Record the score and update
    def update_score(self):
        self.score += 1

    def draw_score(self):
        score_text = self.font.render("Score: " + str(self.score), True, "white")
        self.screen.blit(score_text, (20, 20))

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

            if self.player.rect.left < self.road_x:
                self.player.rect.left = self.road_x

            right_edge = self.road_x + self.road_width

            if self.player.rect.right > right_edge:
                self.player.rect.right = right_edge

            for obstacle in self.obstacles:
                if self.player.get_collision_rect().colliderect(obstacle.get_collision_rect()):
                    font = pygame.font.SysFont("ComicSans", 36)
                    txt = font.render("Game Over!", True, "red")
                    text_rect = txt.get_rect(center=(self.width // 2, self.height // 2))

                    self.screen.blit(txt, text_rect)
                    pygame.display.update()
                    pygame.time.delay(10000)

                    self.running = False

            self.update_obstacles()
            self.update_score()
            self.draw()


        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()