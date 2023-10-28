from physics_body import PhysicsBody
from tools import *
from settings import *
from pygame import Vector2
import math

class Ball(PhysicsBody):
    def __init__(self, resolution, radius):
        self.radius = radius
        self.resolution = resolution
        vertices = []

        for i in range(0, resolution):    
            ang = i*2*math.pi/resolution - math.pi/2
            x = radius*math.cos(ang)
            y = -radius*math.sin(ang)

            position = Vector2(x, y)
            point = Vertex(position)
            vertices.append(point)

        super().__init__(vertices)