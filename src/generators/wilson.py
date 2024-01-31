from ..maze import Maze
from generators.base_maze_generator import MazeGenerator

class WilsonGenerator(MazeGenerator):
    def __init__(self, maze: Maze):
        super().__init__(maze)
    
    def run_algorithm(self):
        pass
