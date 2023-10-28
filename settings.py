import pygame
from enum import Enum

class Positioning(Enum):
    MOVE_ALL_VERTICES = 1
    APPLY_VELOCITY = 2


DEBUG_DRAW_SHAPE = True
DEBUG_DRAW_LINES_TO_CENTER = True
DEBUG_DRAW_FORCES = True

MOVE_SETTING = Positioning.APPLY_VELOCITY

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

DAMPING = 0.9
GRAVITY = 0.9

GROUND = 600

pygame.init()
clock = pygame.time.Clock()
screen_width, screen_height = 1200, 800  # Set the dimensions of the window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Blank Screen")