import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE 


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        # Exit loop when user closes the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        # Refresh screen
        pygame.display.flip()

        # limit the frame rate to 60 FPS
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
