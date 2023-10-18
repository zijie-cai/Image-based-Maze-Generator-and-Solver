import pygame
import random
import os
from .cell import Cell
from .settings import screen, clock, DELAY, WHITE, BLACK, FPS, WIDTH_CELL_COUNT, HEIGHT_CELL_COUNT

def generate_maze(WIDTH_CELL_COUNT, HEIGHT_CELL_COUNT, CELL_SIZE):
    """
    Generate a maze using the Depth-First Search algorithm. The function also saves each frame of the maze 
    generation process as an image. The entrance and exit are created after the entire maze has been generated.

    Parameters:
    WIDTH_CELL_COUNT (int): The number of cells horizontally in the maze.
    HEIGHT_CELL_COUNT (int): The number of cells vertically in the maze.
    CELL_SIZE (int): The size of each cell.

    Returns:
    grid (2D list of Cell): The maze as a 2D list of cells.
    frames (list of str): A list of file paths to the frames of the maze generation process.
    start (Cell): The starting point (entrance) of the maze.
    end (Cell): The ending point (exit) of the maze.
    """

    # Initialize an empty list to store file paths of each image frame during the maze generation
    frames = [] 

    # Initialize a 2D grid with instances of the Cell class, which represents the maze
    grid = [[Cell(x, y) for x in range(WIDTH_CELL_COUNT)] for y in range(HEIGHT_CELL_COUNT)]
    
    # Initialize an empty stack to keep track of the cells that are being visited
    stack = []  

    # Randomly select a starting cell for the maze. The DFS algorithm starts from this cell
    start_x = random.randint(0, HEIGHT_CELL_COUNT - 1)
    start_y = random.randint(0, WIDTH_CELL_COUNT - 1)
    current_cell = grid[start_x][start_y]
    current_cell.visited = True # Mark the starting cell as visited
    stack.append(current_cell)  # Add the starting cell to the stack

    # Continue running as long as there are unvisited cells
    running = True
    while running:
        clock.tick(FPS)  # Limit the frame rate to make the visualization smoother

        # Handle the event of closing the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if stack:  # Check if there are still cells in the stack
            # Continue visiting the current cell and check for unvisited neighbours
            current_cell.current = False
            current_cell = stack[-1]
            current_cell.current = True
            current_cell.visited = True

            # Check for unvisited neighbours
            next_cell = current_cell.check_neighbors(grid, WIDTH_CELL_COUNT, HEIGHT_CELL_COUNT)

            if next_cell:  # If there is an unvisited neighbour
                stack.append(next_cell)  # Add the unvisited neighbour to the stack
                remove_walls(current_cell, next_cell)  # Remove the wall between the current cell and its neighbour
            else:
                # No unvisited neighbours left, backtrack and remove the cell from the stack
                current_cell.backtracked = True
                stack.pop()

            pygame.time.delay(DELAY)  # Add a delay to visualize the maze generation process

        else: 
            running = False  # Stop running if all cells have been visited
            # Reset the state of the final cell
            current_cell.current = False
            current_cell.visited = False
            current_cell.backtracked = True

        screen.fill(BLACK)  # Fill the screen with black color

        # Draw each cell on the screen
        for row in grid:
            for cell in row:
                cell.draw(CELL_SIZE)

        # Create entrance and exit if the maze generation is completed
        if not running:
            start, end = create_entrance_exit(grid)

        pygame.display.flip()  # Update the full display surface to the screen

        # Save each frame of the maze generation process as an image
        frame_path = os.path.join("gif_frames", "frame_{}.jpg".format(str(len(frames)).zfill(5)))
        pygame.image.save(screen, frame_path)
        frames.append(frame_path)

    pygame.quit()  # Close the pygame window

    return grid, frames, start, end

    
def create_entrance_exit(grid, scenario=None):
    """
    Create an entrance and an exit in the maze based on a given scenario. If no scenario is provided, one 
    is selected randomly. In scenario 1, the entrance is created at any cell along the top border, and the 
    exit at any cell along the bottom border. In scenario 2, the entrance is created at any cell along the 
    left border, and the exit at any cell along the right border.

    Parameters:
    grid (2D list of Cell): The grid representing the maze.
    scenario (int): The scenario number (1 or 2). If not provided, one is selected randomly.

    Returns:
    start (Cell): The starting point (entrance) of the maze.
    end (Cell): The ending point (exit) of the maze.
    """
    
    # If a scenario isn't provided, pick one randomly
    if scenario is None:
        scenario = random.randint(1, 2)

    # Determine the length of the row and the column of the grid
    row_len = len(grid)
    col_len = len(grid[0])  # assuming the grid is a rectangle

    # Create entrance and exit based on the selected scenario
    if scenario == 1:
        # Scenario 1: Any cell along the top border for entrance, any cell along the bottom border for exit
        entrance = random.randint(0, col_len - 1)
        exit = random.randint(0, col_len - 1)
        start = grid[0][entrance]
        end = grid[row_len - 1][exit]
        start.walls['top'] = False
        end.walls['bottom'] = False
    else:
        # Scenario 2: Any cell along the left border for entrance, any cell along the right border for exit
        entrance = random.randint(0, row_len - 1)
        exit = random.randint(0, row_len - 1)
        start = grid[entrance][0]
        end = grid[exit][col_len - 1]
        start.walls['left'] = False
        end.walls['right'] = False
        
    return start, end


def remove_walls(current, next):
    """
    Remove the wall between two adjacent cells. The function determines the relative position of the next cell 
    to the current cell and removes the corresponding walls.

    Parameters:
    current (Cell): The current cell in the grid.
    next (Cell): The next cell to visit in the grid.
    """

    dx = current.x - next.x  # Determine the relative x-position of the next cell to the current cell
    
    # If the next cell is to the left of the current cell, remove the left wall of the current cell and the right wall of the next cell
    if dx == 1:  
        current.walls['left'] = False
        next.walls['right'] = False

    # If the next cell is to the right of the current cell, remove the right wall of the current cell and the left wall of the next cell
    elif dx == -1:
        current.walls['right'] = False
        next.walls['left'] = False

    dy = current.y - next.y  # Determine the relative y-position of the next cell to the current cell
    
    # If the next cell is above the current cell, remove the top wall of the current cell and the bottom wall of the next cell
    if dy == 1:
        current.walls['top'] = False
        next.walls['bottom'] = False

    # If the next cell is below the current cell, remove the bottom wall of the current cell and the top wall of the next cell
    elif dy == -1:
        current.walls['bottom'] = False
        next.walls['top'] = False
