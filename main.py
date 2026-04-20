# modules used
import pygame, sys
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event

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
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable) # add player class to its related groups
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # create player object

    Asteroid.containers = (asteroids, updatable, drawable) # add asteroid class to its related groups
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField() # create asteroid field object

    Shot.containers = (shots, updatable, drawable)
    
    while True: # start an infinite loop
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black") # creates a empty window
        updatable.update(dt) # draw the player and asteriods

        for asteroid in asteroids: # check for collision between asteroids and the player
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            # check for collision between shots and the asteroids
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

        for obj in drawable: # 'draws' the sprites
            obj.draw(screen)
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
