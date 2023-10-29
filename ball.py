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

        self.mass = BALL_MASS
        vertex_count: float = resolution

        for i in range(0, resolution):    
            ang = i*2*math.pi/resolution - math.pi/2
            x = radius*math.cos(ang)
            y = -radius*math.sin(ang)

            position = Vector2(x, y)
            vertex = Vertex(position)
            vertex.mass = self.mass / vertex_count
            
            vertices.append(vertex)

        super().__init__(vertices)