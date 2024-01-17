import pygame
from cell import Cell
import random

class Maze:
    def __init__(self, height, width, tile_size, screen):
        self.height = height
        self.width = width
        self.tile_size = tile_size
        self.screen = screen

        self.rows, self.cols = self.height//self.tile_size, self.width//self.tile_size
        self.grid_cells = [
            Cell(row, col, self.screen) for row in range(self.rows) for col in range(self.cols)
        ]
        self.current_cell = self.grid_cells[0]
        self.current_cell.visited = True
        self.visited_stack = [self.current_cell]

    def draw_current_cell(self):
        cur_x = self.current_cell.x*self.tile_size
        cur_y = self.current_cell.y*self.tile_size
        pygame.draw.rect(
            self.screen,
            (255, 128, 0),
            (cur_x, cur_y, self.tile_size, self.tile_size)
        )

    def draw_cell_in_coord(self, cell, color):
        coord_x = cell.x*self.maze.tile_size
        coord_y = cell.y*self.maze.tile_size
        pygame.draw.rect(
            self.maze.screen,
            color,
            (coord_x, coord_y, self.maze.tile_size, self.maze.tile_size)
        )

    def draw_maze(self):
        for cell in self.grid_cells:
            cell.draw_cell()

    def get_unvisited_neighbors(self, cell):
        col, row = cell.x, cell.y
        def get_cell(x, y):
            if 0 <= x < self.cols and 0 <= y < self.rows:
                return self.grid_cells[x+y*self.cols]
            return False
        neighbors = [get_cell(row, col-1), get_cell(row+1, col), get_cell(row, col+1), get_cell(row-1, col)]
        neighbors = [neighbor for neighbor in neighbors if neighbor]
        return neighbors
    
    def get_valid_neighbors(self, cell):
        col, row = cell.x, cell.y

        def get_cell(x, y):
            if 0 <= x < self.cols and 0 <= y < self.rows:
                return self.grid_cells[x + y * self.cols]
            return None

        def valid_neighbor(neighbor):
            # checks if there is no wall between cell and neighbor
            if neighbor.y == row-1:
                return not cell.walls['top']
            if neighbor.x == col+1:
                return not cell.walls['right']
            if neighbor.y == row+1:
                return not cell.walls['bottom']
            if neighbor.x == col-1:
                return not cell.walls['left']
            return False

        neighbors = [get_cell(row-1, col), get_cell(row, col+1), get_cell(row+1, col), get_cell(row, col-1)]
        return [neighbor for neighbor in neighbors if neighbor and valid_neighbor(neighbor)]

    def choose_next_cell(self):
        neighbors = self.get_unvisited_neighbors(self.current_cell)
        neighbors = [neighbor for neighbor in neighbors if not neighbor.visited]
        return random.choice(neighbors) if neighbors else False
