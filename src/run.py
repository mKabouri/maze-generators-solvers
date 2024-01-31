import pygame
from maze import Maze
from dfs_gen import DFSGenerator
from a_star import AStarSolver
from tremaux import TremauxSolver
import config

if __name__ == "__main__":
    maze_width, maze_height = config.WIDTH, config.HEIGHT
    tile_size = config.TILE_SIZE
    screen = pygame.display.set_mode((maze_width, maze_height))

    maze = Maze(maze_height, maze_width, tile_size, screen)
    generator = DFSGenerator(maze)
    generator.display_solve_maze(AStarSolver, gif=False)
