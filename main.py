import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE
from player import Player 


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    while True:
        # Exit loop when user closes the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # create black background
        screen.fill("black")

        # Draw the player
        player.draw(screen)

        # Refresh screen
        pygame.display.flip()

        # limit the frame rate to 60 FPS
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()
