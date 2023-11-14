# This file was created by: Chris Cozort
# Content from Chris Bradfield; Kids Can Code
# KidsCanCode - Game Development with Pygame video series
# Video link: https://youtu.be/OmlQ0XCvIn0 

# game settings 
WIDTH = 1000
HEIGHT = 800
FPS = 30

# player settings
PLAYER_JUMP = 30
PLAYER_GRAV = 1.5
PLAYER_FRIC = 0.2

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0 , 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)




Ground = (0, HEIGHT - 40, WIDTH, 40, "normal")


PLATFORM_LIST = [
                 (0, HEIGHT - 40, WIDTH + 200, 40, "normal"),
                 (WIDTH / 2 - 50, HEIGHT * 7 / 8, 100, 20,"normal"),
                 (125, HEIGHT - 350, 100, 20, "moving"),
                 (222, 200, 100, 20, "moving"),
                 (175, 100, 50, 20, "normal")]

'''MONSTER_LIST = [
                (200, 185, 25, 25, "move"),
                (135, 250, 25, 25, "move"),
                (300, 350, 25, 25, "move"),
                (50, 450, 25, 25, "move")]'''



'''Water_LIST = [
                (100, 185, 25, 25, "move"),
                (135, 250, 25, 25, "move"),
                (200, 230, 25, 25, "move"),
                (160, 150, 25, 25, "move")]'''
#for i in range: (0,10 )

