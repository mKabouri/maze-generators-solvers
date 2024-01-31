import random
from solvers.base_solver import BaseSolver

class TremauxSolver(BaseSolver):
    def __init__(self, maze):
        super().__init__(maze)
        self.current_cell = maze.grid_cells[0]
        self.visited = set()
        self.path = []

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
        return cell.x == self.maze.cols - 1 and cell.y == self.maze.rows - 1
