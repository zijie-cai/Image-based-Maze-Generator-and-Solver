from PIL import Image, ImageDraw
import os

def draw_maze(maze, start, end, path=None, filename="maze_example/maze.png", cell_size=8, wall_color=(0, 0, 0), path_color=(255, 255, 255), shortest_path_color=(255, 105, 97)):
    """
    Draw the maze and the shortest path (if specified) and save it as an image. The maze is drawn on a white background,
    with walls represented by black lines. The shortest path (if specified) is drawn in red. The start and end points of the path 
    are also marked with specific colors. The output image is saved in the current directory as "maze.png".

    Parameters:
    maze (list): The grid representing the maze.
    start (Cell): The starting cell of the path.
    end (Cell): The ending cell of the path.
    path (list): The list of cells representing the shortest path. If None, the shortest path is not drawn.
    filename (str): The name of the output image file.
    cell_size (int): The size of each cell in the image in pixels. Default is 10.
    wall_color (tuple): The RGB color of the walls in the maze. Default is black.
    path_color (tuple): The RGB color of the paths in the maze. Default is white.
    shortest_path_color (tuple): The RGB color of the shortest path in the maze (if specified). Default is red.

    Returns:
    None
    """
    
    # Calculate the size of the image based on the maze dimensions and cell size
    height = len(maze) * cell_size + 2 * cell_size  # Additional padding for top and bottom borders
    width = len(maze[0]) * cell_size + 2 * cell_size  # Additional padding for left and right borders

    # Create a new image with a white background
    img = Image.new("RGB", (width, height), path_color)
    draw = ImageDraw.Draw(img)

    # Draw the maze by iterating over each cell
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            cell = maze[row][col]

            # Calculate the position of the cell in the image
            x1 = col * cell_size + cell_size  # Include padding for left border 
            y1 = row * cell_size + cell_size  # Include padding for top border
            x2 = x1 + cell_size
            y2 = y1 + cell_size

            # Draw walls for each cell as needed
            if cell.walls['top']:
                draw.line([(x1, y1), (x2, y1)], fill=wall_color)  # Top wall
            if cell.walls['right']:
                draw.line([(x2, y1), (x2, y2)], fill=wall_color)  # Right wall
            if cell.walls['bottom']:
                draw.line([(x1, y2), (x2, y2)], fill=wall_color)  # Bottom wall
            if cell.walls['left']:
                draw.line([(x1, y1), (x1, y2)], fill=wall_color)  # Left wall
                
        # Draw a circle at the start of the path
        start_cell = start
        start_x = start_cell.x * cell_size + cell_size + cell_size // 2
        start_y = start_cell.y * cell_size + cell_size + cell_size // 2
        draw.ellipse([(start_x-1.5, start_y-1.5), (start_x+1.5, start_y+1.5)], fill=(60, 179, 113))  # green circle

        # Draw a square at the end of the path
        end_cell = end
        end_x = end_cell.x * cell_size + cell_size + cell_size // 2
        end_y = end_cell.y * cell_size + cell_size + cell_size // 2
        draw.rectangle([(end_x-1.5, end_y-1.5), (end_x+1.5, end_y+1.5)], fill=(100, 149, 237))  # blue square
        
    # Draw the shortest path solution if one was provided
    if path:
        for i in range(len(path) - 1):  # we subtract 1 to avoid Index Error in the loop
            cell = path[i]
            next_cell = path[i + 1]  # get the next cell in the path

            # Calculate the center coordinates of the current cell and the next cell
            x1 = cell.x * cell_size + cell_size + cell_size // 2  # add an additional cell_size for the cell's top-left corner position
            y1 = cell.y * cell_size + cell_size + cell_size // 2
            x2 = next_cell.x * cell_size + cell_size + cell_size // 2
            y2 = next_cell.y * cell_size + cell_size + cell_size // 2

            draw.line([(x1, y1), (x2, y2)], fill=shortest_path_color, width=1)  # draw a line between the two centers
    
    # Create the directory if it does not exist
    if not os.path.exists('maze_example'):
        os.makedirs('maze_example')
        
    # Save the image in the maze_example directory
    img.save(filename)
