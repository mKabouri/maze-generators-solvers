import heapq
import time
from solvers.base_solver import BaseSolver

class AStarSolver(BaseSolver):
    def __init__(self, maze):
        super().__init__(maze)
        self.maze = maze
        self.start = self.maze.grid_cells[0]
        self.end = self.maze.grid_cells[-1]

    def heuristic(self, cell):
        # Manhattan distance as a heuristic
        return abs(cell.x - self.end.x) + abs(cell.y - self.end.y)

    def solve(self):
        start_time = time.time()
        open_set = []
        # Priority queue
        heapq.heappush(open_set, (0, self.start.y, self.start.x))
        came_from = {}

        g_score = {cell: float("inf") for cell in self.maze.grid_cells}
        g_score[self.start] = 0

        f_score = {cell: float("inf") for cell in self.maze.grid_cells}
        f_score[self.start] = self.heuristic(self.start)

        while open_set:
            _, current_x, current_y = heapq.heappop(open_set)
            current = self.maze.grid_cells[current_x+current_y*self.maze.cols]
            if current == self.end:
                self.solve_time = time.time() - start_time
                return self.reconstruct_path(came_from, current)
            # print("### NEXT ITER ###")
            for neighbor in self.maze.get_valid_neighbors(current):
                # print(current.x, current.y)
                # print(neighbor.x, neighbor.y)
                # print("NEXT NEIGHBOR")

                tentative_g_score = g_score[current] + 1

                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor)

                    if neighbor not in [i[1:] for i in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor.y, neighbor.x))
        return []

    def reconstruct_path(self, came_from, current):
        total_path = [current]
        while current in came_from:
            current = came_from[current]
            total_path.append(current)
        return total_path[::-1]
