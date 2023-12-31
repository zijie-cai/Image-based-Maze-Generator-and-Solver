# Image-based Maze Generator and Solver 🌐🔍

## Overview
This repository showcases an intuitive image-based maze generator and solver. The project employs fundamental image processing and path search algorithms and includes detailed Jupyter Notebook guides for both the generator and solver. Engaging visualizations make understanding the algorithms more enjoyable and informative.

## 📸 Visual Demonstrations
Here is a live visualization of how the maze is being generated: 
<br>

![maze](https://github.com/zijie-cai/Image-based-Maze-Generator-and-Solver/assets/74931355/f71ae74c-dfc3-4561-9910-cb3e7e362659)

Here is an example of a generated maze image input for the solver and the output image with the shortest path marked from the solver:
<br>

![maze_input](https://github.com/zijie-cai/Image-based-Maze-Generator-and-Solver/assets/74931355/116af2c3-e94d-4475-a518-c993ebe75bd8)
![maze_output](https://github.com/zijie-cai/Image-based-Maze-Generator-and-Solver/assets/74931355/5c766d0d-7ed3-486a-bb1c-e3f5871853f1)

## 📚 Technologies Used
- Python
- OpenCV
- Pygame
- NumPy

## 🛠 Installation and Setup
- Create and activate a Python virtual environment (venv/conda):
    ```bash
    python3 -m venv env 
    source env/bin/activate # Unix/MacOS
    ./env/Scripts/activate # Windows
    ```
    Alternatively: 
    ```bash
    conda env create -f environment.yml
    conda activate env
    ```

- Upgrade pip and install required libraries (skip if using conda):
    ```bash
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

**Note:** To successfully run the code, you **must** complete the installation and setup steps.

## 🏃‍♂️ How to Run
Step-by-step guides for both generating mazes and solving them can be found at `Generator.ipynb` and `Solver.ipynb`.

1. Clone or download the repository.
2. Open the corresponding Jupyter Notebook files (`Generator.ipynb` for maze generation and `Solver.ipynb` for maze solving).

## 🌟 Features
- Maze Image Generation
- Image-based Maze Solving
- Visual Demonstrations
- Configurable Parameters

## 🚀 Future Updates
Planning to add obstacles and different maze shapes. Also looking to include more pathfinding algorithms with visualizations.

## 👏 Contributions
Open to contributions! If you have suggestions or improvements, feel free to fork the repo and create a pull request.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
