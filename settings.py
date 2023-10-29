import pygame
from enum import Enum

TICK = 60

class Positioning(Enum):
    MOVE_ALL_VERTICES = 1
    APPLY_VELOCITY = 2

DEBUG_DRAW_SHAPE = True
DEBUG_DRAW_LINES_TO_CENTER = True
DEBUG_DRAW_FORCES = True
DEBUG_DRAW_PRESSURE = True

BALL_RESOLUTION = 10
BALL_RADIUS = 100
BALL_MASS = 1

MOVE_SETTING = Positioning.MOVE_ALL_VERTICES

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

DAMPING = 0.98
GRAVITY = 9.81
RESTITUTION = 1

SCALE = 100

GROUND = 600


pygame.init()
clock = pygame.time.Clock()
screen_width, screen_height = 1200, 800  # Set the dimensions of the window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Blank Screen")