# Image Geometric Transformations
This python file is used to perform various types of Geometric Transformation such as -
1. Perspective Change - Zoom In/Zoom Out - Right/Left - X/Y Axis (8 functions)
2. Translation - Positive/Negative - X/Y Axis (4 functions)
3. Scaling - Positive/Negative - X/Y/XY Axis (6 functions)
4. Shearing - Positive/Negative - X/Y Axis (2 functions)
5. Rotation - X/Y/Z Axis (3 functions) (Angle Parameter in Degree)
6. Flipping - X/Y Axis (2 functions)

All the functions have basic parameters of passing the Image, Image Width and Image Height along with passing of the Geometric Transformation FACTOR which is different for each type of transformtion.

Using this Python Script - 
1. Download the "imageAugmentation.py" file from the repository "image_augmentation".
2. Keep this file in same directory as your python files.
3. Use "import imageAugmentation as ia" in your python file.
4. Use the functions with 'ia', for example - "ia.rotateX(image, imageWidth, imageHeight, 60)" will return a rotated image by +60 degrees along X Axis.

Note - The main intention of this script is to help create dataset for machine learning projects with ease.
