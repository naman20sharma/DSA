from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # handle empty input defensively
        if not heights or not heights[0]:
            return []

        # grid dimensions
        rows = len(heights)
        cols = len(heights[0])

        # visited set for cells that can reach Pacific
        pacific_reachable = set()

        # visited set for cells that can reach Atlantic
        atlantic_reachable = set()

        def bfs(start_cells, visited):
            # initialize queue with all ocean border cells for this traversal
            queue = deque(start_cells)

            while queue:
                # pop the next cell to process
                row, col = queue.popleft()

                # explore the four directions
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for dr, dc in directions:
                    # compute neighbor coordinates
                    next_row = row + dr
                    next_col = col + dc

                    # skip if neighbor is outside the grid
                    if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols:
                        continue

                    # skip if we already visited this cell in the current ocean traversal
                    if (next_row, next_col) in visited:
                        continue

                    # in reverse traversal, we can only move to equal or higher height
                    if heights[next_row][next_col] < heights[row][col]:
                        continue

                    # mark the neighbor as reachable from this ocean
                    visited.add((next_row, next_col))

                    # add it to the queue so we can continue expanding from it
                    queue.append((next_row, next_col))

        # collect Pacific border cells, top row and left column
        pacific_start = []

        for col in range(cols):
            # top row touches Pacific
            pacific_start.append((0, col))
            pacific_reachable.add((0, col))

        for row in range(rows):
            # left column touches Pacific
            pacific_start.append((row, 0))
            pacific_reachable.add((row, 0))

        # collect Atlantic border cells, bottom row and right column
        atlantic_start = []

        for col in range(cols):
            # bottom row touches Atlantic
            atlantic_start.append((rows - 1, col))
            atlantic_reachable.add((rows - 1, col))

        for row in range(rows):
            # right column touches Atlantic
            atlantic_start.append((row, cols - 1))
            atlantic_reachable.add((row, cols - 1))

        # run BFS from Pacific border
        bfs(pacific_start, pacific_reachable)

        # run BFS from Atlantic border
        bfs(atlantic_start, atlantic_reachable)

        # collect cells that can reach both oceans
        result = []

        for row in range(rows):
            for col in range(cols):
                # a cell is valid if it appears in both reachable sets
                if (row, col) in pacific_reachable and (row, col) in atlantic_reachable:
                    result.append([row, col])

        return result
            
                