import pygame, constants
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y, radius=constants.PLAYER_RADIUS):
        super().__init__(x, y, radius)
        self.rotation = 0

    def triangle(self): # create the player
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen): # draw the player
        self.screen = pygame.draw.polygon(screen, "white", self.triangle(), constants.LINE_WIDTH)
    
    def rotate(self, dt): # rotates the player
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * constants.PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def update(self, dt): # update player position
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]: # when W pressed
            self.move(dt)
        if keys[pygame.K_a]: # when A pressed
            self.rotate(-dt)
        if keys[pygame.K_s]: # when S pressed
            self.move(-dt)
        if keys[pygame.K_d]: # when D pressed
            self.rotate(dt)