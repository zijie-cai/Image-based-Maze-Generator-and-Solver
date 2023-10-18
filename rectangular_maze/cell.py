import pygame
import random
from .settings import BLACK, WHITE, RED, GREEN, screen, WIDTH, HEIGHT, WIDTH_CELL_COUNT, HEIGHT_CELL_COUNT

class Cell:
    """
    Represents a single cell in the maze with properties determining its status and position.

    Attributes:
        x (int): The x-coordinate of the cell in the grid.
        y (int): The y-coordinate of the cell in the grid.
        walls (dict): Indicates whether each of the four walls (top, right, bottom, left) exist.
        visited (bool): Indicates whether the cell has been visited.
        backtracked (bool): Indicates whether the cell has been backtracked.
        current (bool): Indicates whether the cell is currently being visited.
        parent (Cell): The predecessor of this cell in the path found by A*.
        g (float): Distance from the start cell.
        h (float): Manhattan distance to the goal cell.
        f (float): Estimated cost of the path through this cell. f = g + h
    """
    def __init__(self, x, y):
        """
        Initialize the cell object at position (x, y).

        Parameters:
        x (int): The x-coordinate of the cell in the grid.
        y (int): The y-coordinate of the cell in the grid.
        """
        self.x = x
        self.y = y
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.visited = False
        self.backtracked = False
        self.current = False

        # A* properties
        self.parent = None
        self.g = float('inf')  # Distance to start node
        self.h = 0  # Distance to goal node
        self.f = float('inf')  # Total cost

    # Function to calculate the Manhattan distance to the goal
    def calculate_h(self, end):
        self.h = abs(end.x - self.x) + abs(end.y - self.y)
        self.f = self.g + self.h  # f = g + h

        
    def draw(self, CELL_SIZE):
        """
        Draw the cell on the screen based on its status. 
        The cell's status can be: current (green), backtracked (white), visited (red).
        Also, draw the walls of the cell if they exist.

        Parameters:
        CELL_SIZE (int): The size of each cell on the screen in pixels.
        """
        
        # Determine the pixel position of the cell on the screen
        x, y = self.x * CELL_SIZE, self.y * CELL_SIZE

        # Color the cell based on its state
        if self.current:
            pygame.draw.rect(screen, GREEN, (x, y, CELL_SIZE, CELL_SIZE))  # Current cell is green
        elif self.backtracked:
            pygame.draw.rect(screen, WHITE, (x, y, CELL_SIZE, CELL_SIZE))  # Backtracked cell is white
        elif self.visited:
            pygame.draw.rect(screen, RED, (x, y, CELL_SIZE, CELL_SIZE))  # Visited cell is red

        # Draw the cell's walls if they exist
        if self.walls['top']:
            pygame.draw.line(screen, BLACK, (x, y), (x + CELL_SIZE, y))  # Draw the top wall
        if self.walls['right']:
            pygame.draw.line(screen, BLACK, (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE))  # Draw the right wall
        if self.walls['bottom']:
            pygame.draw.line(screen, BLACK, (x + CELL_SIZE, y + CELL_SIZE), (x, y + CELL_SIZE))  # Draw the bottom wall
        if self.walls['left']:
            pygame.draw.line(screen, BLACK, (x, y + CELL_SIZE), (x, y))  # Draw the left wall


            
    def check_neighbors(self, grid, WIDTH_CELL_COUNT, HEIGHT_CELL_COUNT):
        """ 
        Check the neighboring cells to see if they have been visited.
        If they have not, add them to the list of potential next cells to visit.
        Randomly select one of these cells to be the next cell to visit.

        Parameters:
        grid (list): The grid representing the maze.
        WIDTH_CELL_COUNT (int): The total number of cells horizontally in the maze.
        HEIGHT_CELL_COUNT (int): The total number of cells vertically in the maze.

        Returns:
        neighbor (Cell): A randomly chosen neighboring cell that hasn't been visited.
        """
        
        neighbors = []

        # Check left neighbor cell
        if self.x > 0:
            left = grid[self.y][self.x - 1]
            if not left.visited:
                neighbors.append(left)

        # Check top neighbor cell
        if self.y > 0:
            top = grid[self.y - 1][self.x]
            if not top.visited:
                neighbors.append(top)

        # Check right neighbor cell
        if self.x < WIDTH_CELL_COUNT - 1:
            right = grid[self.y][self.x + 1]
            if not right.visited:
                neighbors.append(right)

        # Check bottom neighbor cell
        if self.y < HEIGHT_CELL_COUNT - 1:
            bottom = grid[self.y + 1][self.x]
            if not bottom.visited:
                neighbors.append(bottom)

        # If there are unvisited neighbors, return one randomly
        if neighbors:
            return random.choice(neighbors)
