from solvers.base_solver import BaseSolver
import time

class RoutingSolver(BaseSolver):
    def __init__(self, maze):
        super().__init__(maze)
        self.cur = self.start

    def heuristic(self, cell):
        return abs(cell.x - self.end.x) + abs(cell.y - self.end.y)

    def solve(self):
        start_time = time.time()
        path = []
        visited = set()
        self.cur = self.start
        while self.cur != self.end:
            path.append(self.cur)
            visited.add(self.cur)
            productive_path = self.find_productive_path(visited)
            if productive_path:
                self.cur = productive_path
            else:
                self.take_first_path(visited)
        path.append(self.end)
        end_time = time.time()
        self.solve_time = end_time - start_time
        return path

    def find_productive_path(self, visited):
        valid_neighbors = self.maze.get_valid_neighbors(self.cur)
        for neighbor in valid_neighbors:
            if self.heuristic(neighbor) < self.heuristic(self.cur) and neighbor not in visited:
                return neighbor
        return None

    def take_first_path(self, visited):
        valid_neighbors = [n for n in self.maze.get_valid_neighbors(self.cur) if n not in visited]
        if valid_neighbors:
            self.cur = valid_neighbors[0]

    def follow_hand_rule(self, visited):
        valid_neighbors = [n for n in self.maze.get_valid_neighbors(self.cur) if n not in visited]
        if valid_neighbors:
            self.cur = valid_neighbors[0]
