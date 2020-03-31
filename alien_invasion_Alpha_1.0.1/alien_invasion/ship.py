import pygame

class Ship:
    """A class to manage the ship.."""

    def __init__(self, ai_game):
        """Initalize the ship and set it's starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get it's rect()
        self.image = pygame.image.load("assets/ship.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store value for the ship's horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Create a value for the ship's velocity
        self.speed_x = 0.0
        self.speed_left = 0.0
        self.speed_right = 0.0
        self.speed_y = 0.0
        self.speed_up = 0.0
        self.speed_down = 0.0

        # Movment flag
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        
        #Update the ship's value not the rect
        self._get_x()


        # Update the rect object from self.x.
        self.rect.x = self.x


    def _get_x(self):
        """Manages the ship's movement along the X-axis"""
        
        #Handles movement to the RIGHT
        if self.moving_right:
            if self.speed_right < self.settings.max_ship_speed:
                self.speed_right += self.settings.max_ship_acceleration
        elif self.speed_right > 0:
            self.speed_right -= self.settings.max_ship_acceleration

        # Handles movement to the LEFT
        if self.moving_left:
            if self.speed_left < self.settings.max_ship_speed:
                self.speed_left += self.settings.max_ship_acceleration
        elif self.speed_left > 0:
            self.speed_left -= self.settings.max_ship_acceleration

        self.speed_x = self.speed_right - self.speed_left

        # Prevents the ship from leaving the viewable window
        if (self.speed_x > 0 
        and not self.rect.right < self.screen_rect.right):
            self.speed_x = 0
        elif self.speed_x < 0 and not self.rect.left > 0:
            self.speed_x = 0

        #change the ships possition based off the speed
        self.x += self.speed_x

    def _get_y(self):
        """Manages the ship's movement along the y-axis"""
        
        # Handles the DOWN movement
        if self.moving_down:
            if self.speed_down < self.settings.max_ship_speed:
                self.speed_down += self.settings.max_ship_acceleration
        elif self.speed_down > 0:
            self.speed_down -= self.settings.max_ship_acceleration


        # Handles the UP movement
        if self.moving_up:
            if self.speed_up < self.settings.max_ship_speed:
                self.speed_up += self.settings.max_ship_acceleration
        elif self.speed_up > 0:
            self.speed_up -= self.settings.max_ship_acceleration


        self.speed_y = self.speed_down - self.speed_up

        # Prevents the ship from leaving the viewable window
        if (self.speed_y > 0 
        and not self.rect.bottom < self.screen_rect.bottom):
            self.speed_y = 0
        elif self.speed_y < 0 and not self.rect.top > 0:
            self.speed_y = 0

        #change the ships possition based off the speed
        self.y += self.speed_y

    def blitme(self):
        """Draw the ship at it's current location."""
        self.screen.blit(self.image, self.rect)

class Bean(Ship):
    """A class to manage the ship.."""

    def __init__(self, ai_game):

        super().__init__(ai_game)

        # Changes the image to a picture of Mr. van Essen
        self.image = pygame.image.load("assets/bean.bmp")
        self.rect = self.image.get_rect()
        

    def update(self):
        """Update the ship's position based on the movement flag."""
        
        #Update the ship's value not the rect
        self._get_x()
        self._get_y()

        # Update the rect object from self.x.
        self.rect.x = self.x
        self.rect.y = self.y