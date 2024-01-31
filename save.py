import pygame
from maze import Maze
from generators.dfs_gen import DFSGenerator
from solvers.a_star import AStarSolver
from solvers.tremaux import TremauxSolver
from solvers.routing import RoutingSolver
import argparse
import config

def main():
    parser = argparse.ArgumentParser(description="Maze Solver")
    parser.add_argument("--solver", choices=["astar", "tremaux", "routing"], default="astar", help="Solver algorithm to use (default: A*)")
    args = parser.parse_args()

    maze_width, maze_height = config.WIDTH, config.HEIGHT
    tile_size = config.TILE_SIZE
    screen = pygame.display.set_mode((maze_width, maze_height))

    maze = Maze(maze_height, maze_width, tile_size, screen)
    generator = DFSGenerator(maze)

    if args.solver == "astar":
        solver_class = AStarSolver
    elif args.solver == "tremaux":
        solver_class = TremauxSolver
    elif args.solver == "routing":
        solver_class = RoutingSolver

    generator.display_solve_maze(solver_class, gif=False)

if __name__ == "__main__":
    main()
