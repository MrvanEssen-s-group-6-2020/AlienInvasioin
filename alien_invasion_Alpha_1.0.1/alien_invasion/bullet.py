import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game, leftSide, blaster_temperature):
        """Create a bullet object at the ship's current position"""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.colour = self.settings.bullet_colour[blaster_temperature]

        #create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        if leftSide:
            self.rect.midtop = (ai_game.ship.rect.midtop[0] + -27,
                ai_game.ship.rect.midtop[1] + 30)
        else:
            self.rect.midtop = (ai_game.ship.rect.midtop[0] + 27,
                ai_game.ship.rect.midtop[1] + 30)

        #uses the velocity of the ship to effect the bullet's trajectory 
        self.speed_x = ai_game.ship.speed_x
        self.inherited_y_speed = ai_game.ship.speed_y

        if self.inherited_y_speed > 0:
            self.inherited_y_speed = 0

        #store the bullet's position as a decimal value
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet up the screen."""
        #update the decimal position of the bullet.
        self._get_x()
        self.y -= self.settings.bullet_speed - self.inherited_y_speed

        # Update the rect position.
        self.rect.x = self.x
        self.rect.y = self.y

    def _get_x(self):
        """Manages the bullet's left and right factors"""
        if self.speed_x > 0:
            self.speed_x -= self.settings.max_bullet_acceleration
            # Rounds off math errors caused by adding floats
            self.speed_x = round(self.speed_x, 3)
        elif self.speed_x < 0:
            self.speed_x += self.settings.max_bullet_acceleration
            # Rounds off math errors caused by adding floats
            self.speed_x = round(self.speed_x, 3)

        self.x += self.speed_x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.colour, self.rect)
