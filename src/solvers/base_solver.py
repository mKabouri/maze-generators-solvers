import pygame
from abc import ABC, abstractmethod

class BaseSolver(ABC):
    def __init__(self, maze):
        self.maze = maze
        self.start = maze.grid_cells[0]
        self.end = maze.grid_cells[-1]
        self.solve_time = None

    @abstractmethod
    def solve(self):
        pass

    def draw_path(self):
        path = self.solve()
        for cell in path:
            x, y = cell.x*self.maze.tile_size, cell.y*self.maze.tile_size
            pygame.draw.circle(
                self.maze.screen,
                (0, 120, 120),
                (x+self.maze.tile_size//2, y+self.maze.tile_size//2),
                self.maze.tile_size//2-2
            )
        for i in range(len(path)-1):
            current_cell = path[i]
            next_cell = path[i+1]
            current_x, current_y = current_cell.x*self.maze.tile_size+self.maze.tile_size//2, current_cell.y*self.maze.tile_size+self.maze.tile_size//2
            next_x, next_y = next_cell.x*self.maze.tile_size+self.maze.tile_size//2, next_cell.y*self.maze.tile_size+self.maze.tile_size//2
            pygame.draw.line(
                self.maze.screen, 
                (0, 255, 255),
                (current_x, current_y), 
                (next_x, next_y), 
                2
            )
        pygame.display.flip()
