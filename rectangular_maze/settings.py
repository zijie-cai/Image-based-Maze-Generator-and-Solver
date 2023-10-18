import pygame
from .widgets import width_widget, height_widget

# Set cell size in pixels
CELL_SIZE = 12

# Define number of cells along the width from the width widget value
WIDTH_CELL_COUNT = width_widget.value

# Define number of cells along the height from the height widget value
HEIGHT_CELL_COUNT = height_widget.value

# Define the window size in pixels, based on the number of cells and the cell size
WIDTH, HEIGHT = WIDTH_CELL_COUNT * CELL_SIZE, HEIGHT_CELL_COUNT * CELL_SIZE

# Set frames per second for the Pygame screen refresh rate
FPS = 60

# Set the delay in milliseconds between each frame (set to 0 for no delay)
DELAY = 50

# Define color codes in RGB format for use in drawing the maze
BLACK = (0 ,0 ,0)  # Black color
RED = (255, 105, 97)  # Red color
WHITE = (255, 255, 255)  # White color
GREEN = (144, 238, 144)  # Green color

# Initialize the Pygame library
pygame.init()

# Create a Pygame window with the predefined size
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define a Pygame clock for controlling the frame rate
clock = pygame.time.Clock()
