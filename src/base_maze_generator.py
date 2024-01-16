from abc import ABC, abstractmethod
import pygame
from maze import Maze
from cell import Cell

class MazeGenerator(ABC):
    def __init__(self, maze: Maze):
        self.maze = maze

    def remove_walls(self, current_cell: Cell, next_cell: Cell):
        dx = current_cell.x - next_cell.x
        dy = current_cell.y - next_cell.y
        if dx == 1:
            current_cell.walls['left'] = False
            next_cell.walls['right'] = False
        elif dx == -1:
            current_cell.walls['right'] = False
            next_cell.walls['left'] = False
        if dy == 1:
            current_cell.walls['top'] = False
            next_cell.walls['bottom'] = False
        elif dy == -1:
            current_cell.walls['bottom'] = False
            next_cell.walls['top'] = False

    def display_solve_maze(self, maze_solver):
        pygame.init()
        solver = maze_solver(self.maze)
        pygame.display.set_caption("Maze Visualization")
        
        clock = pygame.time.Clock()
        running = True

        while running:
            self.maze.screen.fill((135, 156, 144))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Exiting")
                    running = False
                # Quit if we click on "q"
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        print("Exiting")
                        running = False

            # Maze part
            ret = self.run_algorithm()

            # Solution part
            if ret:
                solver.draw_path()

            #####
            # Restart and start solve buttons

            pygame.display.flip()
            clock.tick(60)
        pygame.quit()

    @abstractmethod
    def run_algorithm(self):
        """
        Returns True if the maze is generated, False in all other cases.
        """
        pass
