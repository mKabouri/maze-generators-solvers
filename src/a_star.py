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

    def draw_path(self):
        path = self.solve()
        # Draw circles on top of the lines
        for cell in path:
            x, y = cell.x * self.maze.tile_size, cell.y * self.maze.tile_size
            pygame.draw.circle(
                self.maze.screen,
                (0, 120, 120),
                (x + self.maze.tile_size // 2, y + self.maze.tile_size // 2),
                self.maze.tile_size // 2 - 2
            )

        for i in range(len(path) - 1):
            current_cell = path[i]
            next_cell = path[i + 1]

            # Coordinates for the current cell's center
            current_x, current_y = current_cell.x * self.maze.tile_size + self.maze.tile_size // 2, current_cell.y * self.maze.tile_size + self.maze.tile_size // 2

            # Coordinates for the next cell's center
            next_x, next_y = next_cell.x * self.maze.tile_size + self.maze.tile_size // 2, next_cell.y * self.maze.tile_size + self.maze.tile_size // 2

            # Draw line between centers
            pygame.draw.line(
                self.maze.screen, 
                (0, 255, 255),  # Line color (same as circle color)
                (current_x, current_y), 
                (next_x, next_y), 
                2  # Line thickness
            )

        pygame.display.flip()

