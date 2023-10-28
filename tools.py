from settings import *
from pygame import Vector2
import math 

class Vertex:
    def __init__(self, position: Vector2):
        self.position = position
        self.original_position = Vector2(position.x, position.y)

        self.velocity = Vector2(0,0)
        self.force = Vector2(0,0)

        self.pressure = 0

    def distance_to(self, b) -> float: 
        return self.position.distance_to(b.position)

def calculate_area(vertices: list[Vertex]) -> float:
    n = len(vertices)
    if n < 3:  # Not a polygon
        return 0
    
    area = 0
    for i in range(n):
        x1, y1 = vertices[i].position.x, vertices[i].position.y
        x2, y2 = vertices[(i + 1) % n].position.x, vertices[(i + 1) % n].position.y
        area += (x1 * y2) - (x2 * y1)
    
    return abs(area) / 2.0

def calculate_center(vertices: list[Vertex]) -> Vector2:
    n = len(vertices)
    if n == 0:
        return Vector2(0, 0)

    sum = Vector2(0,0)
    for vertex in vertices:
        sum += vertex.position

    return Vector2(sum.x / n, sum.y / n)

def point_at_distance_from_center(center, target, distance):
    delta = target - center

    angle_radians = math.atan2(delta.y, delta.x)

    x = center.x + (distance * math.cos(angle_radians))
    y = center.y + (distance * math.sin(angle_radians))

    return Vector2(x, y)