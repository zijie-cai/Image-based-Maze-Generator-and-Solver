import ipywidgets as widgets

# Function to create a text widget for specifying the width of the maze.
def maze_width_widget():
    return widgets.BoundedIntText(
        value=30,  # The initial value.
        min=10,  # The minimum allowable value.
        max=50,  # The maximum allowable value.
        step=1,  # The amount by which the value increases/decreases.
        description='Maze Width:',  # The text displayed beside the widget.
        disabled=False,  # If True, the user cannot interact with the widget.
        continuous_update=False,  # If True, the widget value updates while dragging the slider.
        orientation='horizontal',  # The orientation of the widget.
        readout=True,  # If True, the current value is displayed.
        readout_format='d'  # Format of the value display ('d' is for integer).
    )

# Function to create a text widget for specifying the height of the maze.
def maze_height_widget():
    return widgets.BoundedIntText(
        value=30,  # The initial value.
        min=10,  # The minimum allowable value.
        max=50,  # The maximum allowable value.
        step=1,  # The amount by which the value increases/decreases.
        description='Maze Height:',  # The text displayed beside the widget.
        disabled=False,  # If True, the user cannot interact with the widget.
        continuous_update=False,  # If True, the widget value updates while dragging the slider.
        orientation='horizontal',  # The orientation of the widget.
        readout=True,  # If True, the current value is displayed.
        readout_format='d'  # Format of the value display ('d' is for integer).
    )

# Create and assign the widgets to be used elsewhere
width_widget = maze_width_widget()
height_widget = maze_height_widget()
