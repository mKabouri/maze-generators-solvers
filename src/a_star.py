import heapq
import pygame

class AStarSolver:
    def __init__(self, maze):
        self.maze = maze
        self.start = self.maze.grid_cells[0]
        self.end = self.maze.grid_cells[-1]

    def heuristic(self, cell):
        # Manhattan distance as a heuristic
        return abs(cell.x - self.end.x) + abs(cell.y - self.end.y)

    def solve(self):
        open_set = []
        # Priority queue
        heapq.heappush(open_set, (0, self.start.x, self.start.y))
        came_from = {}
        g_score = {cell: float("inf") for cell in self.maze.grid_cells}
        g_score[self.start] = 0

        f_score = {cell: float("inf") for cell in self.maze.grid_cells}
        f_score[self.start] = self.heuristic(self.start)


        while open_set:
            _, current_x, current_y = heapq.heappop(open_set)
            current = self.maze.grid_cells[current_x+current_y*self.maze.cols]
            if current == self.end:
                return self.reconstruct_path(came_from, current)

            for neighbor in self.maze.get_neighbors(current):
                tentative_g_score = g_score[current] + 1

                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor)

                    if neighbor not in [i[1:] for i in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor.x, neighbor.y))
        return []

    def reconstruct_path(self, came_from, current):
        total_path = [current]
        while current in came_from:
            current = came_from[current]
            total_path.append(current)
        return total_path[::-1]

    def draw_path(self):
        path = self.solve()
        for cell in path:
            x, y = cell.x * self.maze.tile_size, cell.y * self.maze.tile_size
            pygame.draw.rect(self.maze.screen, (0, 120, 120), (x, y, self.maze.tile_size, self.maze.tile_size))
        pygame.display.flip()
