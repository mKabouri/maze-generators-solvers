import pygame
from maze import Maze
from dfs_gen import DFSGenerator
import config

if __name__ == "__main__":
    maze_width, maze_height = 500, 500
    tile_size = 50
    screen = pygame.display.set_mode((maze_width, maze_height))

    maze = Maze(maze_height, maze_width, tile_size, screen)
    generator = DFSGenerator(maze)
    generator.display_maze()
