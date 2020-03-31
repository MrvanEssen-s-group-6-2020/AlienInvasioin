
from datetime import timedelta

class Settings:
    "A class to store all settings for alen invasion."

    def __init__ (self):
        """initialize the game's settings"""

        #version
        self.version = "1.0.1 (2020.03.30)"
        
        #screen settings
        self.screen_width = 1080
        self.screen_height = 720
        self.bg_colour = (10, 3, 7) 

        #ship settings
        self.max_ship_speed = 1.9
        self.max_ship_acceleration = .02

        #bullet settings
        self.bullet_speed = 1.9
        self.bullet_width = 4
        self.bullet_height = 20
        self.bullet_colour = ((20, 200, 20),(20, 200, 20),
            (90, 200, 20),(90, 200, 20),(200, 200, 20),(200, 200, 20),
            (200, 150, 60),(200, 150, 60),(255, 90, 20),(255, 90, 20),
            (200, 00, 00),(200, 00, 00))
        self.bullets_allowed = 10
        self.max_bullet_acceleration = 0.005
        self.max_blaster_temp = 12
        self.heat_penalty = timedelta(seconds=1.8)
        self.shot_cooldown = timedelta(seconds=0.3)
        self.cooldown_time = timedelta(seconds=0.15)
