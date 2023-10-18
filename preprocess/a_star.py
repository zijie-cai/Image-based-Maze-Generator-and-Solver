import pygame
from .settings import FPS, DELAY, BLACK, RED, WHITE, GREEN, BLUE, YELLOW, PURPLE, color_dict
from .cell import Cell

def a_star_visualization(grid, start, end, width_cell_count, height_cell_count, cell_size):
    """
    Visualize the A* algorithm on the Pygame screen.

    Parameters:
    grid (list): The 2D grid representing the maze.
    start (Cell): The starting cell of the path.
    end (Cell): The ending cell of the path.
    cell_size (int): The size of each cell in pixels.
    """
    if not grid or start == end:
        return None
    
    pygame.init()
    
    width, height = width_cell_count * cell_size, height_cell_count * cell_size
    
    # Create a Pygame screen with the size of the maze image
    screen = pygame.display.set_mode((width, height))
    
    # Define a Pygame clock for controlling the frame rate
    clock = pygame.time.Clock()
    
    open_list = [start]
    start.g = 0
    start.calculate_h(end)
    path = []

    while open_list:          
        current = min(open_list, key=lambda cell: cell.f)

        # Update the screen
        screen.fill(WHITE)
        for row in grid:
            for cell in row:
                cell.draw(screen, color_dict, cell_size)
        pygame.display.update()
        pygame.time.wait(DELAY)

        if current == end:
            current.status = 'end'
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            
            # Update the screen
            screen.fill(WHITE)
            for row in grid:
                for cell in row:
                    if cell != start and cell != end:
                        cell.status = 'default'    
                        cell.draw(screen, color_dict, cell_size)
                    else:
                        cell.draw(screen, color_dict, cell_size)
            
            # Draw the shortest path solution if one was provided
            if path:
                for i in range(len(path) - 1):  # we subtract 1 to avoid Index Error in the loop
                    cell = path[i]
                    next_cell = path[i + 1]  # get the next cell in the path

                    # Calculate the center coordinates of the current cell and the next cell
                    x1 = cell.x * cell_size + cell_size // 2  # add an additional cell_size for the cell's top-left corner position
                    y1 = cell.y * cell_size + cell_size // 2
                    x2 = next_cell.x * cell_size + cell_size // 2
                    y2 = next_cell.y * cell_size + cell_size // 2

                    pygame.draw.line(screen, RED, (x1, y1), (x2, y2), 1)  # draw a line between the two centers

            pygame.display.update()
            pygame.time.wait(DELAY)
            break  # Added break here to exit from the while open_list loop.
        
        open_list.remove(current)
        if current != start and current != end: 
            current.status = 'closed'

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x, y = current.x + dx, current.y + dy
            if 0 <= x < width_cell_count and 0 <= y < height_cell_count:
                neighbor = grid[y][x]
                if dx == 1 and (current.walls['right'] or neighbor.walls['left']) or \
                   dx == -1 and (current.walls['left'] or neighbor.walls['right']) or \
                   dy == 1 and (current.walls['bottom'] or neighbor.walls['top']) or \
                   dy == -1 and (current.walls['top'] or neighbor.walls['bottom']):
                    continue

                g = current.g + 1
                if g < neighbor.g:
                    neighbor.g = g
                    neighbor.calculate_h(end)
                    neighbor.parent = current
                    if neighbor not in open_list:
                        neighbor.status = 'open'
                        open_list.append(neighbor)
        
        clock.tick(FPS)  # Limit the frame rate to make the visualization smoother

        # Handle the event of closing the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
                        
    # Loop to keep the Pygame window open.
    finished = False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
        clock.tick(FPS)

    pygame.quit()

    return path[::-1] if path else None
