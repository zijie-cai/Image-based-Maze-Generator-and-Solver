import random
import pygame
from .settings import BLACK, RED, WHITE, GREEN, BLUE, YELLOW, PURPLE, color_dict

class Cell:
    """
    Represents a single cell in the maze with properties determining its status and position.

    Attributes:
        x (int): The x-coordinate of the cell in the grid.
        y (int): The y-coordinate of the cell in the grid.
        walls (dict): Indicates whether each of the four walls (top, right, bottom, left) exist.
        status (str): The status of the cell ('open', 'closed', 'path', 'start', 'end').
        parent (Cell): The predecessor of this cell in the path found by A*.
        g (float): Distance from the start cell.
        h (float): Manhattan distance to the goal cell.
        f (float): Estimated cost of the path through this cell. f = g + h
    """
    def __init__(self, x, y, status='default'):
        """
        Initialize the cell object at position (x, y).

        Parameters:
        x (int): The x-coordinate of the cell in the grid.
        y (int): The y-coordinate of the cell in the grid.
        """
        self.x = x
        self.y = y
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}

        # A* properties
        self.status = status  # Track the status of the cell
        self.parent = None
        self.g = float('inf')  # Distance to start node
        self.h = 0  # Distance to goal node
        self.f = float('inf')  # Total cost

    # Function to calculate the Manhattan distance to the goal
    def calculate_h(self, end):
        self.h = abs(end.x - self.x) + abs(end.y - self.y)
        self.f = self.g + self.h  # f = g + h

    def draw(self, screen, color_dict, cell_size):
        x, y = self.x * cell_size, self.y * cell_size
        color = color_dict[self.status] if self.status else color_dict['default']
        pygame.draw.rect(screen, color, (x, y, cell_size, cell_size))
        
         # Draw the cell's walls if they exist
        if self.walls['top']:
            pygame.draw.line(screen, BLACK, (x, y), (x + cell_size, y))  # Draw the top wall
        if self.walls['right']:
            pygame.draw.line(screen, BLACK, (x + cell_size, y), (x + cell_size, y + cell_size))  # Draw the right wall
        if self.walls['bottom']:
            pygame.draw.line(screen, BLACK, (x + cell_size, y + cell_size), (x, y + cell_size))  # Draw the bottom wall
        if self.walls['left']:
            pygame.draw.line(screen, BLACK, (x, y + cell_size), (x, y))  # Draw the left wall
