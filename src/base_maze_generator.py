from abc import ABC, abstractmethod
import pygame
from maze import Maze
from cell import Cell

class MazeGenerator(ABC):
    def __init__(self, maze: Maze):
        self.maze = maze

    def remove_walls(self, current_cell: Cell, next_cell: Cell):
        dx = current_cell.x - next_cell.x
        if dx == 1:
            current_cell.walls['left'] = False
            next_cell.walls['right'] = False
        if dx == -1:
            current_cell.walls['right'] = False
            next_cell.walls['left'] = False
        dy = current_cell.y - next_cell.y
        if dy == 1:
            current_cell.walls['top'] = False
            next_cell.walls['bottom'] = False
        if dy == -1:
            current_cell.walls['bottom'] = False
            next_cell.walls['top'] = False

    def display_maze(self):
        pygame.init()

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
            self.run_algorithm()

            #####
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()

    @abstractmethod
    def run_algorithm(self):
        pass
