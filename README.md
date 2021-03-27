[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1xt1oV4b_egSAQjk9HbDGl9bes_j8NR8Z?usp=sharing)


# Image Geometric Transformations
This python file is used to perform various types of Geometric Transformation such as -
1. Perspective Change - Zoom In/Zoom Out - Right/Left - X/Y Axis (8 functions)
2. Translation - Positive/Negative - X/Y Axis (4 functions)
3. Scaling - Positive/Negative - X/Y/XY Axis (6 functions)
4. Shearing - Positive/Negative - X/Y Axis (2 functions)
5. Rotation - X/Y/Z Axis (3 functions) (Angle Parameter in Degree)
6. Flipping - X/Y Axis (2 functions)

All the functions have basic parameters of passing the Image, Image Width and Image Height along with passing of the Geometric Transformation FACTOR which is different for each type of transformation.

Using this Python Script - 
1. Download the "GeometricTransformations.py" file from the repository "img-geometric-transformation".
2. Keep this file in same directory as your python files.
3. Use "import GeometricTransformations as gt" in your python file.
4. Use the functions with 'gt', for example - "gt.rotateX(image, imageWidth, imageHeight, 60)" will return a rotated image by +60 degrees along X Axis.

Testing the Python Script -
1. Clone the repository.
2. Add a test image (e.g. "test.jpg") to the folder.
3. Open command line and change directory to same folder path as this repository.
4. Run the following command and follow the instructions
```bash
> python main.py "path_to_image"
```
5. Example
```bash
> python main.py "test.jpg"
```
