import pygame
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    # inform the user the game is about to start loading a the size of the window that will open
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # initialise pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # create groups for the sprites
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable) # add player class to the groups
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # define the player start position
    
    while True: # start an infinite loop
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # creates a empty window
        screen.fill("black")
        # draw the player
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
