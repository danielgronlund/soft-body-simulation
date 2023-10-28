from settings import *
from tools import *

import pygame
from pygame import Vector2
import math

class PhysicsBody:
    def __init__(self, vertices):
        self.vertices = vertices
        self.area = calculate_area(vertices)
        self.position = calculate_center(vertices)
        self.original_position = self.position
        self.velocity = Vector2()

    def update(self, delta_time):
        self.simulate(delta_time)
        self.render()

    def simulate(self, delta_time):
        self.pressure = 1.0 - calculate_area(self.vertices) / self.area
        self.position = calculate_center(self.vertices)
        
        i = 0
        for vertex in self.vertices:
            vertex.force = Vector2()

            distance = self.position.distance_to(vertex.position)
            e = self.original_position.distance_to(vertex.original_position)

            p = 1.0 - (distance / e)
            vertex.pressure = p

            ideal_position = (vertex.original_position - self.original_position) + self.position
            
            direction = ideal_position - vertex.position

            pressure_direction = point_at_distance_from_center(self.original_position, ideal_position - self.position, e)
            vertex.force += (direction * 3) + (pressure_direction * self.pressure * 3)
            
            vertex.velocity += vertex.force * delta_time
            vertex.velocity.y += GRAVITY
            vertex.velocity *= DAMPING

            vertex.position += vertex.velocity 

            if DEBUG_DRAW_FORCES:
                pygame.draw.line(screen, (255, 0, 0), vertex.position, vertex.position + vertex.velocity)

            i += 1

        self.position += self.velocity

        if self.position.y > GROUND:
            self.position.y = GROUND

        for vertex in self.vertices:
            if vertex.position.y > GROUND:
                vertex.force = Vector2()
                vertex.velocity = Vector2()
                vertex.position.y = GROUND

    def render(self):
        i = 0

        if DEBUG_DRAW_SHAPE:
            pygame.draw.circle(screen, (100, 100, 100), self.position, 5)
        
        for vertex in self.vertices:
            i += 1
            if i >= len(self.vertices):
                i = 0

            next = self.vertices[i]

            if DEBUG_DRAW_SHAPE:
                pygame.draw.line(screen, (100, 100, 100), vertex.position, next.position)

            if DEBUG_DRAW_LINES_TO_CENTER:
                pygame.draw.line(screen, (100, 100, 100), self.position, vertex.position)
