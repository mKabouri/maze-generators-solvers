from base_maze_generator import MazeGenerator
import pygame

class DFSGenerator(MazeGenerator):
    def __init__(
            self,
            maze
        ):
        super().__init__(maze)

    def run_algorithm(self):
        self.maze.draw_maze()
        self.maze.draw_current_cell()
        next_cell = self.maze.choose_next_cell()
        if next_cell:
            next_cell.visited = True
            self.maze.visited_stack.append(next_cell)
            self.remove_walls(self.maze.current_cell, next_cell)
            self.maze.current_cell = next_cell
        elif self.maze.visited_stack:
            self.maze.current_cell = self.maze.visited_stack.pop()



