import numpy as np
import cv2
import math


def perspectiveRightZoomOutX(image, imageWidth, imageHeight, perspectiveFactor):
    perspectiveFactorX = perspectiveFactor
    initCoord = np.float32([[0, 0], [0, imageHeight], [imageWidth, 0], [imageWidth, imageHeight]])
    finalCoord = np.float32([[0, 0], [0, imageHeight], [imageWidth, 0 + perspectiveFactorX], [imageWidth, imageHeight - perspectiveFactorX]])
    M = cv2.getPerspectiveTransform(initCoord, finalCoord)
    perspectiveRightZoomOutXImage = cv2.warpPerspective(image, M, (0, 0))
    return perspectiveRightZoomOutXImage


def perspectiveLeftZoomOutX(image, imageWidth, imageHeight, perspectiveFactor):
    perspectiveFactorX = perspectiveFactor
    initCoord = np.float32([[0, 0], [0, imageHeight], [imageWidth, 0], [imageWidth, imageHeight]])
    finalCoord = np.float32([[0, 0 + perspectiveFactorX], [0, imageHeight - perspectiveFactorX], [imageWidth, 0], [imageWidth, imageHeight]])
    M = cv2.getPerspectiveTransform(initCoord, finalCoord)
    perspectiveLeftZoomOutXImage = cv2.warpPerspective(image, M, (0, 0))
    return perspectiveLeftZoomOutXImage


def perspectiveRightZoomOutY(image, imageWidth, imageHeight, perspectiveFactor):
    perspectiveFactorY = perspectiveFactor
    initCoord = np.float32([[0, 0], [0, imageHeight], [imageWidth, 0], [imageWidth, imageHeight]])
    finalCoord = np.float32([[0 + perspectiveFactorY, 0], [0, imageHeight], [imageWidth - perspectiveFactorY, 0], [imageWidth, imageHeight]])
    M = cv2.getPerspectiveTransform(initCoord, finalCoord)
    perspectiveRightZoomOutYImage = cv2.warpPerspective(image, M, (0, 0))
    return perspectiveRightZoomOutYImage


def perspectiveLeftZoomOutY(image, imageWidth, imageHeight, perspectiveFactor):
    perspectiveFactorY = perspectiveFactor
    initCoord = np.float32([[0, 0], [0, imageHeight], [imageWidth, 0], [imageWidth, imageHeight]])
    finalCoord = np.float32([[0, 0], [0 + perspectiveFactorY, imageHeight], [imageWidth - perspectiveFactorY, 0], [imageWidth, imageHeight]])
    M = cv2.getPerspectiveTransform(initCoord, finalCoord)
    perspectiveLeftZoomOutYImage = cv2.warpPerspective(image, M, (0, 0))
    return perspectiveLeftZoomOutYImage


def perspectiveRightZoomInX(image, imageWidth, imageHeight, perspectiveFactor):
    perspectiveFactorX = perspectiveFactor
    initCoord = np.float32([[0, 0], [0, imageHeight], [imageWidth, 0], [imageWidth, imageHeight]])
    finalCoord = np.float32([[0, 0], [0, imageHeight], [imageWidth, 0 - perspectiveFactorX], [imageWidth, imageHeight + perspectiveFactorX]])
    M = cv2.getPerspectiveTransform(initCoord, finalCoord)
    perspectiveRightZoomInXImage = cv2.warpPerspective(image, M, (0, 0))
    return perspectiveRightZoomInXImage


def perspectiveLeftZoomInX(image, imageWidth, imageHeight, perspectiveFactor):
    perspectiveFactorX = perspectiveFactor
    initCoord = np.float32([[0, 0], [0, imageHeight], [imageWidth, 0], [imageWidth, imageHeight]])
    finalCoord = np.float32([[0, 0 - perspectiveFactorX], [0, imageHeight + perspectiveFactorX], [imageWidth, 0], [imageWidth, imageHeight]])
    M = cv2.getPerspectiveTransform(initCoord, finalCoord)
    perspectiveLeftZoomInXImage = cv2.warpPerspective(image, M, (0, 0))
    return perspectiveLeftZoomInXImage


def perspectiveRightZoomInY(image, imageWidth, imageHeight, perspectiveFactor):
    perspectiveFactorY = perspectiveFactor
    initCoord = np.float32([[0, 0], [0, imageHeight], [imageWidth, 0], [imageWidth, imageHeight]])
    finalCoord = np.float32([[0 - perspectiveFactorY, 0], [0, imageHeight], [imageWidth + perspectiveFactorY, 0], [imageWidth, imageHeight]])
    M = cv2.getPerspectiveTransform(initCoord, finalCoord)
    perspectiveRightZoomInYImage = cv2.warpPerspective(image, M, (0, 0))
    return perspectiveRightZoomInYImage


def perspectiveLeftZoomInY(image, imageWidth, imageHeight, perspectiveFactor):
    perspectiveFactorY = perspectiveFactor
    initCoord = np.float32([[0, 0], [0, imageHeight], [imageWidth, 0], [imageWidth, imageHeight]])
    finalCoord = np.float32([[0, 0], [0 - perspectiveFactorY, imageHeight], [imageWidth - perspectiveFactorY, 0], [imageWidth, imageHeight]])
    M = cv2.getPerspectiveTransform(initCoord, finalCoord)
    perspectiveLeftZoomInYImage = cv2.warpPerspective(image, M, (0, 0))
    return perspectiveLeftZoomInYImage


def translatePositiveX(image, imageWidth, imageHeight, translateFactor):
    translateFactorX = translateFactor
    initCoord = np.float32([[0, 0], [0, imageHeight], [imageWidth, 0], [imageWidth, imageHeight]])
    finalCoord = np.float32([[0 - translateFactorX, 0], [0 - translateFactorX, imageHeight], [imageWidth - translateFactorX, 0], [imageWidth - translateFactorX, imageHeight]])
    M = cv2.getPerspectiveTransform(initCoord, finalCoord)
    translatePositiveXImage = cv2.warpPerspective(image, M, (0, 0))
    return translatePositiveXImage


def translateNegativeX(image, imageWidth, imageHeight, translateFactor):
    translateFactorX = translateFactor
    initCoord = np.float32([[0, 0], [0, imageHeight], [imageWidth, 0], [imageWidth, imageHeight]])
    finalCoord = np.float32([[0 + translateFactorX, 0], [0 + translateFactorX, imageHeight], [imageWidth + translateFactorX, 0], [imageWidth + translateFactorX, imageHeight]])
    M = cv2.getPerspectiveTransform(initCoord, finalCoord)
    translateNegativeXImage = cv2.warpPerspective(image, M, (0, 0))
    return translateNegativeXImage


def translatePositiveY(image, imageWidth, imageHeight, translateFactor):
    translateFactorY = translateFactor
    initCoord = np.float32([[0, 0], [0, imageHeight], [imageWidth, 0], [imageWidth, imageHeight]])
    finalCoord = np.float32([[0, 0 - translateFactorY], [0, imageHeight - translateFactorY], [imageWidth, 0 - translateFactorY], [imageWidth, imageHeight - translateFactorY]])
    M = cv2.getPerspectiveTransform(initCoord, finalCoord)
    translatePositiveYImage = cv2.warpPerspective(image, M, (0, 0))
    return translatePositiveYImage


def translateNegativeY(image, imageWidth, imageHeight, translateFactor):
    translateFactorY = translateFactor
    initCoord = np.float32([[0, 0], [0, imageHeight], [imageWidth, 0], [imageWidth, imageHeight]])
    finalCoord = np.float32([[0, 0 + translateFactorY], [0, imageHeight + translateFactorY], [imageWidth, 0 + translateFactorY], [imageWidth, imageHeight + translateFactorY]])
    M = cv2.getPerspectiveTransform(initCoord, finalCoord)
    translateNegativeYImage = cv2.warpPerspective(image, M, (0, 0))
    return translateNegativeYImage


def scalePositiveX(image, imageWidth, imageHeight, scaleFactor):
    scaleX = (scaleFactor * imageWidth)
    initCoord = np.float32([[0, 0], [0, imageHeight], [imageWidth, 0], [imageWidth, imageHeight]])
    finalCoord = np.float32([[0 - scaleX, 0], [0 - scaleX, imageHeight], [imageWidth + scaleX, 0], [imageWidth + scaleX, imageHeight]])
    M = cv2.getPerspectiveTransform(initCoord, finalCoord)
    scalePositiveXImage = cv2.warpPerspective(image, M, (0, 0))
    return scalePositiveXImage


def scaleNegativeX(image, imageWidth, imageHeight, scaleFactor):
    scaleX = (scaleFactor * imageWidth)
    initCoord = np.float32([[0, 0], [0, imageHeight], [imageWidth, 0], [imageWidth, imageHeight]])
    finalCoord = np.float32([[0 + scaleX, 0], [0 + scaleX, imageHeight], [imageWidth - scaleX, 0], [imageWidth - scaleX, imageHeight]])
    M = cv2.getPerspectiveTransform(initCoord, finalCoord)
    scaleNegativeXImage = cv2.warpPerspective(image, M, (0, 0))
    return scaleNegativeXImage


def scalePositiveY(image, imageWidth, imageHeight, scaleFactor):
    scaleY = (scaleFactor * imageHeight)
    initCoord = np.float32([[0, 0], [0, imageHeight], [imageWidth, 0], [imageWidth, imageHeight]])
    finalCoord = np.float32([[0, 0 - scaleY], [0, imageHeight + scaleY], [imageWidth, 0 - scaleY], [imageWidth, imageHeight + scaleY]])
    M = cv2.getPerspectiveTransform(initCoord, finalCoord)
    scalePositiveYImage = cv2.warpPerspective(image, M, (0, 0))
    return scalePositiveYImage


def scaleNegativeY(image, imageWidth, imageHeight, scaleFactor):
    scaleY = (scaleFactor * imageHeight)
    initCoord = np.float32([[0, 0], [0, imageHeight], [imageWidth, 0], [imageWidth, imageHeight]])
    finalCoord = np.float32([[0, 0 + scaleY], [0, imageHeight - scaleY], [imageWidth, 0 + scaleY], [imageWidth, imageHeight - scaleY]])
    M = cv2.getPerspectiveTransform(initCoord, finalCoord)
    scaleNegativeYImage = cv2.warpPerspective(image, M, (0, 0))
    return scaleNegativeYImage


def scalePositiveXY(image, imageWidth, imageHeight, scaleFactor):
    scaleX = (scaleFactor * imageWidth)
    scaleY = (scaleFactor * imageHeight)
    initCoord = np.float32([[0, 0], [0, imageHeight], [imageWidth, 0], [imageWidth, imageHeight]])
    finalCoord = np.float32([[0 - scaleX, 0 - scaleY], [0 - scaleX, imageHeight + scaleY], [imageWidth + scaleX, 0 - scaleY], [imageWidth + scaleX, imageHeight + scaleY]])
    M = cv2.getPerspectiveTransform(initCoord, finalCoord)
    scalePositiveXYImage = cv2.warpPerspective(image, M, (0, 0))
    return scalePositiveXYImage


def scaleNegativeXY(image, imageWidth, imageHeight, scaleFactor):
    scaleX = (scaleFactor * imageWidth)
    scaleY = (scaleFactor * imageHeight)
    initCoord = np.float32([[0, 0], [0, imageHeight], [imageWidth, 0], [imageWidth, imageHeight]])
    finalCoord = np.float32([[0 + scaleX, 0 + scaleY], [0 + scaleX, imageHeight - scaleY], [imageWidth - scaleX, 0 + scaleY], [imageWidth - scaleX, imageHeight - scaleY]])
    M = cv2.getPerspectiveTransform(initCoord, finalCoord)
    scaleNegativeXYImage = cv2.warpPerspective(image, M, (0, 0))
    return scaleNegativeXYImage


def shearX(image, imageWidth, imageHeight, shearFactorBottomX=0, shearFactorTopX=0):
    initCoord = np.float32([[0, 0], [0, imageHeight], [imageWidth, 0], [imageWidth, imageHeight]])
    finalCoord = np.float32([[0 + shearFactorTopX, 0], [0 + shearFactorBottomX, imageHeight], [imageWidth + shearFactorTopX, 0], [imageWidth + shearFactorBottomX, imageHeight]])
    M = cv2.getPerspectiveTransform(initCoord, finalCoord)
    shearXImage = cv2.warpPerspective(image, M, (0, 0))
    return shearXImage


def shearY(image, imageWidth, imageHeight, shearFactorLeftY=0, shearFactorRightY=0):
    initCoord = np.float32([[0, 0], [0, imageHeight], [imageWidth, 0], [imageWidth, imageHeight]])
    finalCoord = np.float32([[0, 0 - shearFactorLeftY], [0, imageHeight - shearFactorLeftY], [imageWidth, 0 - shearFactorRightY], [imageWidth, imageHeight - shearFactorRightY]])
    M = cv2.getPerspectiveTransform(initCoord, finalCoord)
    shearYImage = cv2.warpPerspective(image, M, (0, 0))
    return shearYImage


def rotateX(image, imageWidth, imageHeight, rotateXAngleBy):
    rotateXAngleBy = 60 + rotateXAngleBy / 3
    subtractX = math.sqrt((imageHeight * imageHeight) - ((imageHeight / 2) * (imageHeight / 2)))
    subtractY = math.cos(math.radians(rotateXAngleBy)) * imageHeight
    LineX = math.sin(math.radians(rotateXAngleBy)) * imageWidth
    LineY = imageWidth / 2
    X = LineX - subtractX
    Y = LineY - subtractY
    initCoord = np.float32([[0, 0], [0, imageHeight], [imageWidth, 0], [imageWidth, imageHeight]])
    finalCoord = np.float32([[0 + X, 0 + Y], [0 - X, imageHeight - Y], [imageWidth - X, 0 + Y], [imageWidth + X, imageHeight - Y]])
    M = cv2.getPerspectiveTransform(initCoord, finalCoord)
    rotateXImage = cv2.warpPerspective(image, M, (0, 0))
    return rotateXImage


def rotateY(image, imageWidth, imageHeight, rotateYAngleBy):
    rotateYAngleBy = 60 + rotateYAngleBy / 3
    subtractY = math.sqrt((imageWidth * imageWidth) - ((imageWidth / 2) * (imageWidth / 2)))
    subtractX = math.cos(math.radians(rotateYAngleBy)) * imageWidth
    LineY = math.sin(math.radians(rotateYAngleBy)) * imageWidth
    LineX = imageWidth / 2
    Y = LineY - subtractY
    X = LineX - subtractX
    initCoord = np.float32([[0, 0], [0, imageHeight], [imageWidth, 0], [imageWidth, imageHeight]])
    finalCoord = np.float32([[0 + X, 0 - Y], [0 + X, imageHeight + Y], [imageWidth - X, 0 + Y], [imageWidth - X, imageHeight - Y]])
    M = cv2.getPerspectiveTransform(initCoord, finalCoord)
    rotateYImage = cv2.warpPerspective(image, M, (0, 0))
    return rotateYImage


def rotateZ(image, imageWidth, imageHeight, rotateZAngleBY):
    rotationMatrix = cv2.getRotationMatrix2D((imageWidth / 2, imageHeight / 2), (rotateZAngleBY), 1)
    rotateZImage = cv2.warpAffine(image, rotationMatrix, (imageWidth, imageHeight))
    return rotateZImage


def flipX(image, imageWidth, imageHeight):
    flipFactorX = 120
    subtractY = math.sqrt((imageWidth * imageWidth) - ((imageWidth / 2) * (imageWidth / 2)))
    subtractX = math.cos(math.radians(flipFactorX)) * imageWidth
    LineY = math.sin(math.radians(flipFactorX)) * imageWidth
    LineX = imageWidth / 2
    Y = LineY - subtractY
    X = LineX - subtractX
    initCoord = np.float32([[0, 0], [0, imageHeight], [imageWidth, 0], [imageWidth, imageHeight]])
    finalCoord = np.float32([[0 + X, 0 - Y], [0 + X, imageHeight + Y], [imageWidth - X, 0 + Y], [imageWidth - X, imageHeight - Y]])
    M = cv2.getPerspectiveTransform(initCoord, finalCoord)
    flipXImage = cv2.warpPerspective(image, M, (0, 0))
    return flipXImage


def flipY(image, imageWidth, imageHeight):
    flipFactorY = 120
    subtractX = math.sqrt((imageHeight * imageHeight) - ((imageHeight / 2) * (imageHeight / 2)))
    subtractY = math.cos(math.radians(flipFactorY)) * imageHeight
    LineX = math.sin(math.radians(flipFactorY)) * imageWidth
    LineY = imageWidth / 2
    X = LineX - subtractX
    Y = LineY - subtractY
    initCoord = np.float32([[0, 0], [0, imageHeight], [imageWidth, 0], [imageWidth, imageHeight]])
    finalCoord = np.float32([[0 + X, 0 + Y], [0 - X, imageHeight - Y], [imageWidth - X, 0 + Y], [imageWidth + X, imageHeight - Y]])
    M = cv2.getPerspectiveTransform(initCoord, finalCoord)
    flipYImage = cv2.warpPerspective(image, M, (0, 0))
    return flipYImage
