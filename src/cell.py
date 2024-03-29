import pygame
import config as config

class Cell:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.walls = {
            "top": True,
            "right": True,
            "bottom": True,
            "left": True
        }
        self.visited = False
        self.screen = screen

    def draw_cell(self):
        pos_x, pos_y = self.x*config.TILE_SIZE, self.y*config.TILE_SIZE
        endpoint = (self.x == (config.WIDTH//config.TILE_SIZE)-1) and (self.y == (config.HEIGHT//config.TILE_SIZE)-1)

        if endpoint:
            cell_color = (0, 255, 0)  # Green color for the endpoint
        if endpoint:
            cell_color = (0, 255, 0)  # Green color for the endpoint
        elif self.visited:
            cell_color = (0, 0, 0)  # Black color for visited cells
        else:
            cell_color = (255, 255, 255)  # Default color for unvisited cells

        pygame.draw.rect(
            self.screen,
            cell_color,
            (pos_x, pos_y, config.TILE_SIZE, config.TILE_SIZE)
        )
        wall_color = (255, 255, 255)
        wall_thickness = 2
        if self.walls['top']:
            pygame.draw.line(
                self.screen,
                wall_color,
                (pos_x, pos_y),
                (pos_x+config.TILE_SIZE, pos_y),
                wall_thickness
            )
        if self.walls['right']:
            pygame.draw.line(
                self.screen,
                wall_color,
                (pos_x+config.TILE_SIZE, pos_y),
                (pos_x+config.TILE_SIZE, pos_y+config.TILE_SIZE),
                wall_thickness
            )
        if self.walls['bottom']:
            pygame.draw.line(
                self.screen,
                wall_color,
                (pos_x+config.TILE_SIZE, pos_y+config.TILE_SIZE),
                (pos_x, pos_y+config.TILE_SIZE),
                wall_thickness
            )
        if self.walls['left']:
            pygame.draw.line(
                self.screen,
                wall_color,
                (pos_x, pos_y+config.TILE_SIZE),
                (pos_x, pos_y),
                wall_thickness
            )
