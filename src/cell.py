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
        if self.visited:
            # If a cell is visited it becomes black
            pygame.draw.rect(
                self.screen,
                (0, 0, 0),
                (pos_x, pos_y, config.TILE_SIZE, config.TILE_SIZE)
            )

        wall_color = (255, 255, 255)
        wall_thickness = 2
        if self.walls['top'] == True:
            pygame.draw.line(
                self.screen,
                wall_color,
                (pos_x, pos_y),
                (pos_x+config.TILE_SIZE, pos_y),
                wall_thickness
            )
        if self.walls['right'] == True:
            pygame.draw.line(
                self.screen,
                wall_color,
                (pos_x+config.TILE_SIZE, pos_y),
                (pos_x+config.TILE_SIZE, pos_y+config.TILE_SIZE),
                wall_thickness
            )
        if self.walls['bottom'] == True:
            pygame.draw.line(
                self.screen,
                wall_color,
                (pos_x+config.TILE_SIZE, pos_y+config.TILE_SIZE),
                (pos_x, pos_y+config.TILE_SIZE),
                wall_thickness
            )
        if self.walls['left'] == True:
            pygame.draw.line(
                self.screen,
                wall_color,
                (pos_x, pos_y+config.TILE_SIZE),
                (pos_x, pos_y),
                wall_thickness
            )
