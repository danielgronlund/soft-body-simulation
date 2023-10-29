from settings import *
import pygame
from pygame import Vector2

from ball import Ball

ball = Ball(resolution=BALL_RESOLUTION, radius=BALL_RADIUS)

def simulate():
    ball.update(1/60)
    

def main():
    running = True
    mouse_position = Vector2(0,0)
    mouse_is_down = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_is_down = True
                    x, y = event.pos

                    mouse_position = Vector2(x, y)
            elif event.type == pygame.MOUSEMOTION:
                if mouse_is_down:
                    x, y = event.pos
                    mouse_position = Vector2(x, y)

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_is_down = False

        if mouse_is_down:  # Left mouse button
            for vertex in ball.vertices:
                if MOVE_SETTING == Positioning.MOVE_ALL_VERTICES:
                    vertex.position = mouse_position + vertex.original_position
                    vertex.velocity = Vector2()
                    ball.velocity = Vector2()
                elif MOVE_SETTING == Positioning.APPLY_VELOCITY:
                    vertex.velocity += (mouse_position - vertex.position) / 10

            ball.position = mouse_position

        # Clear the screen
        screen.fill((0, 0, 0))
        pygame.draw.line(screen, (100, 100, 100), Vector2(0, GROUND), Vector2(SCREEN_WIDTH, GROUND))

        simulate()
        pygame.display.flip()
        
        clock.tick(TICK)
    pygame.quit()

if __name__ == "__main__":
    main()
