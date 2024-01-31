import pygame
import random

class TremauxSolver:
    def __init__(self, maze):
        self.maze = maze
        self.current_cell = maze.grid_cells[0]  # Start at the first cell
        self.visited = set()  # Set to store visited cells
        self.path = []  # Stack to store the path taken

    def solve(self):
        self.visited.add(self.current_cell)
        self.path.append(self.current_cell)
        while not self.is_exit(self.current_cell):
            unvisited_neighbors = self.get_unvisited_neighbors(self.current_cell)
            if unvisited_neighbors:
                # If there are unvisited neighbors, choose one and move to it
                next_cell = random.choice(unvisited_neighbors)
                self.visited.add(next_cell)
                self.path.append(next_cell)
                self.current_cell = next_cell
            else:
                # Backtrack if no unvisited neighbors
                self.path.pop()
                if not self.path:
                    raise ValueError("No path found")
                self.current_cell = self.path[-1]
        return self.path

    def get_unvisited_neighbors(self, cell):
        neighbors = self.maze.get_valid_neighbors(cell)
        return [n for n in neighbors if n not in self.visited]

    def is_exit(self, cell):
        # Define your exit condition, for example, the bottom-right cell
        return cell.x == self.maze.cols - 1 and cell.y == self.maze.rows - 1

    def draw_path(self):
        path = self.solve()
        for cell in path:
            x, y = cell.x * self.maze.tile_size, cell.y * self.maze.tile_size
            pygame.draw.circle(
                self.maze.screen,
                (0, 120, 120),
                (x + self.maze.tile_size//2, y+self.maze.tile_size//2),
                self.maze.tile_size//2-2
            )
        pygame.display.flip()