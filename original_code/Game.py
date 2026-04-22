import pygame


class Game:
    def __init__(self):
        pygame.init()

        self.width = 700
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Car Dodge Game")

        self.clock = pygame.time.Clock()
        self.running = True

    def draw_road(self):
        road_width = 300
        road_x = (self.width - road_width) // 2

        # draw road
        pygame.draw.rect(self.screen, (50, 50, 50), (road_x, 0, road_width, self.height))

        # lane lines
        lane_color = (255, 255, 255)
        lane_width = 5
        dash_height = 20
        gap = 20

        middle_x = self.width // 2

        for y in range(0, self.height, dash_height + gap):
            pygame.draw.rect(
                self.screen,
                lane_color,
                (middle_x - lane_width // 2, y, lane_width, dash_height)
            )

    def draw(self):
        # background (grass)
        self.screen.fill((34, 139, 34))

        # draw road
        self.draw_road()

        pygame.display.update()

    def run(self):
        while self.running:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()