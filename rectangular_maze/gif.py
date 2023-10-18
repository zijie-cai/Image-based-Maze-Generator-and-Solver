from moviepy.editor import ImageSequenceClip
import os, glob
from .settings import FPS

def maze_gif(frames):
    """
    This function generates a GIF animation from a sequence of image frames. 
    It then removes the frames from the filesystem after the GIF is created.

    Parameters:
    frames (list): List of paths to the image frames.
    """
    
    # Create the directory if it does not exist
    if not os.path.exists('maze_example'):
        os.makedirs('maze_example')
    
    # Create a GIF from the frames with a set frames-per-second rate.
    clip = ImageSequenceClip(frames, fps=FPS)
    
    # Write the created GIF to a file named 'maze.gif'.
    clip.write_gif("maze_example/maze.gif")

    # After the GIF is created, remove all frame images from the 'gif_frames' directory.
    frames = glob.glob('gif_frames/*')
    
    # Loop through each frame in the directory and remove it.
    for frame in frames:
        os.remove(frame)
