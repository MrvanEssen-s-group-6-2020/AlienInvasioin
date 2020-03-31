
import sys
import pygame

class AleanInvasion:
    """Overall class to manage bahavior"""

    def __init__ (self):
        """Initialize the game and create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 900))
        pygame.display.set_caption("Alien Invasion")

        self.fKey = False

        # Set the background colour
        self.bgcolour = (100, 100, 180)
        
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            #watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if pygame.key.get_pressed()[102] and not self.fKey: 
                    
                    if self.bgcolour == (0, 0, 90):
                        self.bgcolour = (100, 100, 180)
                    else:
                        self.bgcolour = (0, 0, 90)
                    
                    self.fKey == True
                    
                else:
                    self.fKey = False

            # Redraw the screen during each pass through the loop
            self.screen.fill(self.bgcolour)

            # Make the most recently drawn screen visible                
            pygame.display.flip()

if __name__ == "__main__":
    # Make an instance and run the game

    ai = AleanInvasion()
    ai.run_game()

   