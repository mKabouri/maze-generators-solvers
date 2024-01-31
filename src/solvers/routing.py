from solvers.base_solver import BaseSolver

class RoutingSolver(BaseSolver):
    def __init__(self, maze):
        super().__init__(maze)
        self.cur = self.start

    def heuristic(self, cell):
        return abs(cell.x - self.end.x) + abs(cell.y - self.end.y)

    def solve(self):
        path = []
        MD_best = self.heuristic(self.start)
        self.cur = self.start
        while self.cur != self.end:
            path.append(self.cur)
            productive_path = self.find_productive_path()
            if productive_path:
                self.cur = productive_path
            else:
                MD_best = self.heuristic(self.cur)
                self.take_first_path(MD_best)
                while self.heuristic(self.cur) != MD_best or not self.find_productive_path():
                    self.follow_hand_rule()
        path.append(self.end)
        return path

    def find_productive_path(self):
        valid_neighbors = self.maze.get_valid_neighbors(self.cur)
        for neighbor in valid_neighbors:
            if self.heuristic(neighbor) < self.heuristic(self.cur):
                return neighbor
        return None

    def take_first_path(self, MD_best):
        valid_neighbors = self.maze.get_valid_neighbors(self.cur)
        if valid_neighbors:
            self.cur = valid_neighbors[0]

    def follow_hand_rule(self):
        valid_neighbors = self.maze.get_valid_neighbors(self.cur)
        if valid_neighbors:
            self.cur = valid_neighbors[0]
