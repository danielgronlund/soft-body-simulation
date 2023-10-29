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
        self.force = Vector2()
        self.pressure = 0.0

    def update(self, delta_time):
        self.simulate(delta_time)
        self.render()

    def simulate(self, delta_time):
        self.force = Vector2()

        bounce_direction = Vector2()
        self.impulse = Vector2()
        number_of_bouncy_vertices = 0
        for vertex in self.vertices:
            vertex.force = Vector2()
            distance = self.position.distance_to(vertex.position)
            e = self.original_position.distance_to(vertex.original_position)

            p = 1.0 - (distance / e)
            vertex.pressure = p

            ideal_position = (vertex.original_position - self.original_position) + self.position
            
            direction = ideal_position - vertex.position

            pressure_direction = point_at_distance_from_center(self.position, ideal_position, e) - self.position

            direction += ((pressure_direction * vertex.pressure) + (pressure_direction * self.pressure)) / 2

            if DEBUG_DRAW_PRESSURE:
                pygame.draw.line(screen, (0,255,0), vertex.position, vertex.position + direction)
                
            vertex.force += direction * delta_time

            acceleration = (vertex.force / vertex.mass)
            vertex.velocity += acceleration * delta_time
            vertex.velocity *= DAMPING
            vertex.velocity += (direction - vertex.velocity) / 5
            vertex.position += (vertex.velocity * SCALE) * delta_time

            if vertex.position.y > GROUND:
                
                vertex.position.y = GROUND
                if ideal_position.y > GROUND:
                    _d = ideal_position - vertex.position
                    bounce_direction += _d
                    vertex.velocity.y = 0
                    number_of_bouncy_vertices += 1
        
        if number_of_bouncy_vertices > 0:
            self.impulse += ((bounce_direction / number_of_bouncy_vertices) * RESTITUTION)

        if DEBUG_DRAW_PRESSURE:
            pygame.draw.line(screen, (0,255,0), self.position, self.position + self.impulse)

        self.impulse = self.impulse * delta_time
        change_in_velocity = self.impulse / self.mass
        self.velocity -= change_in_velocity

        self.velocity.y += GRAVITY * delta_time

        self.velocity *= DAMPING
        self.position += (self.velocity * SCALE) * delta_time

        if DEBUG_DRAW_FORCES:
            pygame.draw.line(screen, (0,0,255), self.position, self.position + self.velocity)

        for vertex in self.vertices:
            vertex.velocity += (self.impulse / len(self.vertices)) * delta_time
            vertex.velocity.y += GRAVITY * delta_time
        
        self.pressure = max(0, 1.0 - calculate_area(self.vertices) / self.area)

    def render(self):
        i = 0

        if DEBUG_DRAW_SHAPE:
            pygame.draw.circle(screen, (100, 100, 100), self.position, 5)
        
        if DEBUG_DRAW_FORCES:
            pygame.draw.line(screen, (255, 0, 0), self.position, self.position + self.velocity)

        for vertex in self.vertices:
            i += 1
            if i >= len(self.vertices):
                i = 0

            next = self.vertices[i]

            if DEBUG_DRAW_SHAPE:
                pygame.draw.line(screen, (100, 100, 100), vertex.position, next.position)

            if DEBUG_DRAW_LINES_TO_CENTER:
                pygame.draw.line(screen, (100, 100, 100), self.position, vertex.position)

            if DEBUG_DRAW_FORCES:
                pygame.draw.line(screen, (255, 0, 0), vertex.position, vertex.position + vertex.velocity)
