# Set frames per second for the Pygame screen refresh rate
FPS = 60

# Set the delay in milliseconds between each frame (set to 0 for no delay)
DELAY = 50

# Define color codes in RGB format for use in drawing the maze
BLACK = (0 ,0 ,0)  # Black color
RED = (255, 105, 97)  # Red color
WHITE = (255, 255, 255)  # White color
GREEN = (144, 238, 144)  # Green color
BLUE = (100, 149, 237)
YELLOW = (255, 255, 0)
PURPLE = (147, 112, 219)

color_dict = {
    'open': BLUE,  # Open cells (frontier) are blue
    'closed': GREEN,  # Closed cells (visited) are red
    'start': YELLOW,  # Start cell is yellow
    'end': PURPLE,  # End cell is purple
    'default': WHITE
}
