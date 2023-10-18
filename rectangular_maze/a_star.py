from .cell import Cell
from .settings import WIDTH_CELL_COUNT, HEIGHT_CELL_COUNT

def a_star(grid, start, end):
    """
    Implements A* algorithm to find the shortest path from the start cell to the end cell.

    Parameters:
    grid (list): The 2D grid representing the maze.
    start (Cell): The starting cell of the path.
    end (Cell): The ending cell of the path.

    Returns:
    path (list): The list of cells from the start cell to the end cell, or None if no path is found.
    """
    
    # Initialize the open list with the start cell
    open_list = [start]
    start.g = 0  # The cost from start to start is 0
    start.calculate_h(end)  # Calculate the heuristic cost from the start to the end cell

    while open_list:
        # Get the cell with the lowest total cost (f) in the open list
        current = min(open_list, key=lambda cell: cell.f)

        # If the current cell is the end cell, then we have found a solution
        if current is end:
            path = []
            # Traverse back to the start cell through each cell's parent and append each cell to the path
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            return path[::-1]  # Reverse the path to get the correct order from start to end

        # Remove the current cell from the open list
        open_list.remove(current)

        # Check each of the current cell's neighbors (right, left, down, up)
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x, y = current.x + dx, current.y + dy
            # Ensure that the neighbor's coordinates are within the grid
            if 0 <= x < WIDTH_CELL_COUNT and 0 <= y < HEIGHT_CELL_COUNT:
                neighbor = grid[y][x]

                # Skip the neighbor if there is a wall between it and the current cell
                if dx == 1:  # right
                    if current.walls['right'] or neighbor.walls['left']:
                        continue
                elif dx == -1:  # left
                    if current.walls['left'] or neighbor.walls['right']:
                        continue
                elif dy == 1:  # down
                    if current.walls['bottom'] or neighbor.walls['top']:
                        continue
                elif dy == -1:  # up
                    if current.walls['top'] or neighbor.walls['bottom']:
                        continue

                # Calculate the cost (g) from the start cell to the neighbor through the current cell
                g = current.g + 1

                # If this path is shorter (in terms of cost g) than any previous path found to the neighbor,
                # then this is a new best path and we should record it
                if g < neighbor.g:
                    neighbor.g = g
                    neighbor.calculate_h(end)  # Recalculate the heuristic cost for the neighbor
                    neighbor.parent = current  # Set the current cell as the neighbor's parent
                    if neighbor not in open_list:
                        # If the neighbor is not in the open list, add it
                        open_list.append(neighbor)

    # If we have checked all possible cells and didn't find a path, then there is no solution
    return None
