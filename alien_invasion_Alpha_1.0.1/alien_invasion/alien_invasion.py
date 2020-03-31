import sys
import pygame
import time
from settings import Settings
from ship import Ship, Bean
from bullet import Bullet
from datetime import datetime, timedelta



class AleanInvasion:
    """Overall class to manage bahavior"""

    def __init__ (self):
        """Initialize the game and create game resources"""
        pygame.init()
        self.settings = Settings()

        #Sets the dimentions and caption of the window.
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion project"+
        f" by Andrew George [Version: {self.settings.version}]")
        pygame.display.set_icon(pygame.image.load("assets/icon.bmp"))


        #Create an instance of ship
        self.ship = Ship(self)
       
        self.bullets = pygame.sprite.Group()

        #Keeps track of which blaster the next bullet will fire out of
        self.leftSide = True

        #Keeps track of when the guns were last fired and their tempature
        self.blasterTemp = 0
        self.lastFired = datetime.now()
        self.lastCooldown = datetime.now()

        #secret bean tool
        self.bean_b = False
        self.bean_e = False
        self.bean_a = False
        self.bean_n = False
        self.bean_mode = False
        
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._check_for_bean()
            self._manage_gun_temp()
            self.update_bullets()
            self._update_screen()
    
    def update_bullets(self):
        """Updates the movement of bullets and 
        limits the number of bullets allowed"""
        self.bullets.update()

        #Get rid of bullets that have dissappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_events(self):
        """Responds to keypress and mouse events"""
        
        #watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)

    def _check_keydown(self, event):
        """Responds to key down"""
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            # Move the ship RIGHT
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            # Move the ship LEFT
            self.ship.moving_left = True
            self.bean_a = True
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            #stops the ship going up
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            # Stops the ship going DOWN
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    #bean stuff
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_b:
            self.bean_b = True
        elif event.key == pygame.K_e:
            self.bean_e = True
        elif event.key == pygame.K_a:
            self.bean_a = True
        elif event.key == pygame.K_n:
            self.bean_n = True
        elif event.key == pygame.K_s:
            self.bean_s = True
 
    def _check_keyup(self, event):            
        """Responds to key up"""
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            # Stops the ship going RIGHT
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            # Stops the ship going LEFT
            self.ship.moving_left = False
            self.bean_a = False
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            #stops the ship going up
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            # Stops the ship going DOWN
            self.ship.moving_down = False
    #bean stuff    
        elif event.key == pygame.K_b:
            self.bean_b = False
        elif event.key == pygame.K_e:
            self.bean_e = False
        elif event.key == pygame.K_n:
            self.bean_n = False
        elif event.key == pygame.K_s:
            self.bean_s = False

    def _manage_gun_temp(self):
        """Causes the blaster to cool down over time"""
        
        #checks to see how much time has gone by since the last shot
        #cools the gun over time
        if self.blasterTemp < self.settings.max_blaster_temp:
            if (self.blasterTemp > 0 
            and self._check_time(
            self.lastFired, self.settings.shot_cooldown)
            and self._check_time(
            self.lastFired, self.settings.cooldown_time)):
                self.blasterTemp -= 1 
                self.lastCooldown = datetime.now()
        elif (self.settings.heat_penalty <
         datetime.now() - self.lastFired):
                self.blasterTemp = 0

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        
        if self.blasterTemp < self.settings.max_blaster_temp:    
            
            #creates a new bullet
            new_bullet = Bullet(self, self.leftSide, self.blasterTemp)
            self.bullets.add(new_bullet)
            
            #increases blaster temperature
            self.lastFired = datetime.now()
            self.blasterTemp += 1

            if self.leftSide:
                self.leftSide = False
            else:
                self.leftSide = True 

    def _check_time(self, start, limit):
        if datetime.now() - start > limit:
            return True
        else:
            return False


    def _check_for_bean(self):
        if self.bean_a and self.bean_b and self.bean_e and self.bean_n:
            
            if not self.bean_mode:
                self.bean_mode = True
                self.ship = Bean(self)
                print("BEANS")

    def _update_screen(self):
        """Update images on the screen and flip to the new screen"""
        
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Make the most recently drawn screen visible                
        pygame.display.flip()

if __name__ == "__main__":
    # Make an instance and run the game

    ai = AleanInvasion()
    ai.run_game()

            
