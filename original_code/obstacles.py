import pygame
import sys
import random


    # def move(self, keys):
    #     if keys[pygame.K_LEFT]:
    #         self.x -= self.speed
    #     if keys[pygame.K_RIGHT]:
    #         self.x += self.speed




# Subtask II.A: Obstacle Class

class Obstacle:
    def __init__(self, screen_width):
        # II.A.1: Random horizontal position
        self.width = 15
        self.height = 15
        self.x = random.randint(0, screen_width - self.width)

        # II.A.2: Start near top
        self.y = -self.height

        # II.A.3: Appearance

        self.speed = 2

    # II.B: Move obstacle downward
    def move(self):
        self.y += self.speed  # II.B.1

    def draw(self, screen):
        ob1 = pygame.image.load("../image/Obstacle1")
        ob2 = pygame.image.load("../image/Obstacle2")
        ob3 = pygame.image.load("../image/Obstacle3")
        screen.blit(ob1, (self.x, self.y))



    # II.C.1: Check if off screen
    def is_off_screen(self, screen_height):
        return self.y > screen_height


# =========================
# Main Function
# =========================
def main():
    pygame.init()

    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Falling Obstacles")

    clock = pygame.time.Clock()


    # List to store obstacles
    obstacles = []

    spawn_timer = 0

    running = True
    while running:
        clock.tick(60)

        # Quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()



        spawn_timer += 1

        if spawn_timer > 50:  # II.D.1: timing decision
            obstacles.append(Obstacle(WIDTH))  # II.D.2: add obstacle
            spawn_timer = 0


        for obstacle in obstacles:
            obstacle.move()


        obstacles = [obs for obs in obstacles if not obs.is_off_screen(HEIGHT)]  # II.C.2


        screen.fill((255, 255, 255))


        for obstacle in obstacles:
            obstacle.draw(screen)

        pygame.display.update()

    pygame.quit()
    sys.exit()


# Run the game
if __name__ == "__main__":
    main()