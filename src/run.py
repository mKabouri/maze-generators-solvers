import pygame
from maze import Maze
from generators.dfs_gen import DFSGenerator
from generators.wilson import WilsonGenerator
from solvers.a_star import AStarSolver
from solvers.tremaux import TremauxSolver
from solvers.routing import RoutingSolver
import config

if __name__ == "__main__":
    maze_width, maze_height = config.WIDTH, config.HEIGHT
    tile_size = config.TILE_SIZE
    screen = pygame.display.set_mode((maze_width, maze_height))

    maze = Maze(maze_height, maze_width, tile_size, screen)
    generator = WilsonGenerator(maze)
    generator.display_solve_maze(TremauxSolver, gif=False)
