Stereo Image Analysis: Computation of Transformation Matrices and Exploration of Camera Geometry

# Stereo Image Analysis
## Computation of Transformation Matrices and Exploration of Camera Geometry

This project focuses on analyzing stereo images to compute various transformation matrices that represent the geometric relationships between two views. These computations include the Calibration Matrix, Homography Matrix, Rotation Matrix, and the Fundamental Matrix, essential for tasks like 3D reconstruction, motion analysis, and camera calibration.

### Project Structure

- `gui.py`: Contains graphical interface for recording a pair of corresponding points. (Part(a) of the assignment)
- `points.py`: Contains the matching points between the two stereo images.
- `stereo_analysis.py`: Main script that orchestrates the matrix computations for Homography, Rotation and fundamental matrix. (Part(b) of the assignment)

### Prerequisites

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/). Additionally, this project depends on the following Python libraries:

- NumPy
- OpenCV-Python

You can install these packages using pip:

*Make sure you have baltimore_A1.jpg and baltimore_A2.jpg. For ease, the both the images are attached in the directory

### Running the Project

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Run the `stereo_analysis.py` script to start the analysis:

python stereo_analysis.py

### Output

The script will compute and print the following matrices based on the stereo images provided:

- Calibration Matrix K
- Homography Matrix H
- Rotation Matrix R
- Fundamental Matrix F



### Authors

- Aseem Anand

### Contact Information

For any additional questions or comments, please email [aseem.anand.0609@gmail.com]

