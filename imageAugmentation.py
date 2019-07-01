import numpy as np
import cv2
import math


def perspectiveRightZoomOutX(image, MinX, MinY, MaxX, MaxY, perspectiveFactor):
    perspectiveFactorX = perspectiveFactor
    initCoord = np.float32([[MinX,MinY],[MinX,MaxY],[MaxX,MinY],[MaxX,MaxY]])
    finalCoord = np.float32([[MinX,MinY],[MinX,MaxY],[MaxX,MinY+perspectiveFactorX],[MaxX,MaxY-perspectiveFactorX]])
    M = cv2.getPerspectiveTransform(initCoord,finalCoord)
    perspectiveRightZoomOutXImage = cv2.warpPerspective(image,M,(0,0))
    return perspectiveRightZoomOutXImage


def perspectiveLeftZoomOutX(image, MinX, MinY, MaxX, MaxY, perspectiveFactor):
    perspectiveFactorX = perspectiveFactor
    initCoord = np.float32([[MinX,MinY],[MinX,MaxY],[MaxX,MinY],[MaxX,MaxY]])
    finalCoord = np.float32([[MinX,MinY+perspectiveFactorX],[MinX,MaxY-perspectiveFactorX],[MaxX,MinY],[MaxX,MaxY]])
    M = cv2.getPerspectiveTransform(initCoord,finalCoord)
    perspectiveLeftZoomOutXImage = cv2.warpPerspective(image,M,(0,0))
    return perspectiveLeftZoomOutXImage


def perspectiveRightZoomOutY(image, MinX, MinY, MaxX, MaxY, perspectiveFactor):
    perspectiveFactorY = perspectiveFactor
    initCoord = np.float32([[MinX,MinY],[MinX,MaxY],[MaxX,MinY],[MaxX,MaxY]])
    finalCoord = np.float32([[MinX+perspectiveFactorY,MinY],[MinX,MaxY],[MaxX-perspectiveFactorY,MinY],[MaxX,MaxY]])
    M = cv2.getPerspectiveTransform(initCoord,finalCoord)
    perspectiveRightZoomOutYImage = cv2.warpPerspective(image,M,(0,0))
    return perspectiveRightZoomOutYImage


def perspectiveLeftZoomOutY(image, MinX, MinY, MaxX, MaxY, perspectiveFactor):
    perspectiveFactorY = perspectiveFactor
    initCoord = np.float32([[MinX,MinY],[MinX,MaxY],[MaxX,MinY],[MaxX,MaxY]])
    finalCoord = np.float32([[MinX,MinY],[MinX+perspectiveFactorY,MaxY],[MaxX-perspectiveFactorY,MinY],[MaxX,MaxY]])
    M = cv2.getPerspectiveTransform(initCoord,finalCoord)
    perspectiveLeftZoomOutYImage = cv2.warpPerspective(image,M,(0,0))
    return perspectiveLeftZoomOutYImage


def perspectiveRightZoomInX(image, MinX, MinY, MaxX, MaxY, perspectiveFactor):
    perspectiveFactorX = perspectiveFactor
    initCoord = np.float32([[MinX,MinY],[MinX,MaxY],[MaxX,MinY],[MaxX,MaxY]])
    finalCoord = np.float32([[MinX,MinY],[MinX,MaxY],[MaxX,MinY-perspectiveFactorX],[MaxX,MaxY+perspectiveFactorX]])
    M = cv2.getPerspectiveTransform(initCoord,finalCoord)
    perspectiveRightZoomInXImage = cv2.warpPerspective(image,M,(0,0))
    return perspectiveRightZoomInXImage


def perspectiveLeftZoomInX(image, MinX, MinY, MaxX, MaxY, perspectiveFactor):
    perspectiveFactorX = perspectiveFactor
    initCoord = np.float32([[MinX,MinY],[MinX,MaxY],[MaxX,MinY],[MaxX,MaxY]])
    finalCoord = np.float32([[MinX,MinY-perspectiveFactorX],[MinX,MaxY+perspectiveFactorX],[MaxX,MinY],[MaxX,MaxY]])
    M = cv2.getPerspectiveTransform(initCoord,finalCoord)
    perspectiveLeftZoomInXImage = cv2.warpPerspective(image,M,(0,0))
    return perspectiveLeftZoomInXImage


def perspectiveRightZoomInY(image, MinX, MinY, MaxX, MaxY, perspectiveFactor):
    perspectiveFactorY = perspectiveFactor
    initCoord = np.float32([[MinX,MinY],[MinX,MaxY],[MaxX,MinY],[MaxX,MaxY]])
    finalCoord = np.float32([[MinX-perspectiveFactorY,MinY],[MinX,MaxY],[MaxX+perspectiveFactorY,MinY],[MaxX,MaxY]])
    M = cv2.getPerspectiveTransform(initCoord,finalCoord)
    perspectiveRightZoomInYImage = cv2.warpPerspective(image,M,(0,0))
    return perspectiveRightZoomInYImage


def perspectiveLeftZoomInY(image, MinX, MinY, MaxX, MaxY, perspectiveFactor):
    perspectiveFactorY = perspectiveFactor
    initCoord = np.float32([[MinX,MinY],[MinX,MaxY],[MaxX,MinY],[MaxX,MaxY]])
    finalCoord = np.float32([[MinX,MinY],[MinX-perspectiveFactorY,MaxY],[MaxX-perspectiveFactorY,MinY],[MaxX,MaxY]])
    M = cv2.getPerspectiveTransform(initCoord,finalCoord)
    perspectiveLeftZoomInYImage = cv2.warpPerspective(image,M,(0,0))
    return perspectiveLeftZoomInYImage


def translatePositiveX(image, MinX, MinY, MaxX, MaxY, translateFactor):
    translateFactorX = translateFactor
    initCoord = np.float32([[MinX,MinY],[MinX,MaxY],[MaxX,MinY],[MaxX,MaxY]])
    finalCoord = np.float32([[MinX-translateFactorX,MinY],[MinX-translateFactorX,MaxY],[MaxX-translateFactorX,MinY],[MaxX-translateFactorX,MaxY]])
    M = cv2.getPerspectiveTransform(initCoord,finalCoord)
    translatePositiveXImage = cv2.warpPerspective(image,M,(0,0))
    return translatePositiveXImage


def translateNegativeX(image, MinX, MinY, MaxX, MaxY, translateFactor):
    translateFactorX = translateFactor
    initCoord = np.float32([[MinX,MinY],[MinX,MaxY],[MaxX,MinY],[MaxX,MaxY]])
    finalCoord = np.float32([[MinX+translateFactorX,MinY],[MinX+translateFactorX,MaxY],[MaxX+translateFactorX,MinY],[MaxX+translateFactorX,MaxY]])
    M = cv2.getPerspectiveTransform(initCoord,finalCoord)
    translateNegativeXImage = cv2.warpPerspective(image,M,(0,0))
    return translateNegativeXImage


def translatePositiveY(image, MinX, MinY, MaxX, MaxY, translateFactor):
    translateFactorY = translateFactor
    initCoord = np.float32([[MinX,MinY],[MinX,MaxY],[MaxX,MinY],[MaxX,MaxY]])
    finalCoord = np.float32([[MinX,MinY-translateFactorY],[MinX,MaxY-translateFactorY],[MaxX,MinY-translateFactorY],[MaxX,MaxY-translateFactorY]])
    M = cv2.getPerspectiveTransform(initCoord,finalCoord)
    translatePositiveYImage = cv2.warpPerspective(image,M,(0,0))
    return translatePositiveYImage


def translateNegativeY(image, MinX, MinY, MaxX, MaxY, translateFactor):
    translateFactorY = translateFactor
    initCoord = np.float32([[MinX,MinY],[MinX,MaxY],[MaxX,MinY],[MaxX,MaxY]])
    finalCoord = np.float32([[MinX,MinY+translateFactorY],[MinX,MaxY+translateFactorY],[MaxX,MinY+translateFactorY],[MaxX,MaxY+translateFactorY]])
    M = cv2.getPerspectiveTransform(initCoord,finalCoord)
    translateNegativeYImage = cv2.warpPerspective(image,M,(0,0))
    return translateNegativeYImage

def scalePositiveX(image, MinX, MinY, MaxX, MaxY, scaleFactor):
    scaleX = (scaleFactor*MaxX)
    initCoord = np.float32([[MinX,MinY],[MinX,MaxY],[MaxX,MinY],[MaxX,MaxY]])
    finalCoord = np.float32([[MinX-scaleX,MinY],[MinX-scaleX,MaxY],[MaxX+scaleX,MinY],[MaxX+scaleX,MaxY]])
    M = cv2.getPerspectiveTransform(initCoord,finalCoord)
    scalePositiveXImage = cv2.warpPerspective(image,M,(0,0))
    return scalePositiveXImage


def scaleNegativeX(image, MinX, MinY, MaxX, MaxY, scaleFactor):
    scaleX = (scaleFactor*MaxX)
    initCoord = np.float32([[MinX,MinY],[MinX,MaxY],[MaxX,MinY],[MaxX,MaxY]])
    finalCoord = np.float32([[MinX+scaleX,MinY],[MinX+scaleX,MaxY],[MaxX-scaleX,MinY],[MaxX-scaleX,MaxY]])
    M = cv2.getPerspectiveTransform(initCoord,finalCoord)
    scaleNegativeXImage = cv2.warpPerspective(image,M,(0,0))
    return scaleNegativeXImage

def scalePositiveY(image, MinX, MinY, MaxX, MaxY, scaleFactor):
    scaleY = (scaleFactor*MaxY)
    initCoord = np.float32([[MinX,MinY],[MinX,MaxY],[MaxX,MinY],[MaxX,MaxY]])
    finalCoord = np.float32([[MinX,MinY-scaleY],[MinX,MaxY+scaleY],[MaxX,MinY-scaleY],[MaxX,MaxY+scaleY]])
    M = cv2.getPerspectiveTransform(initCoord,finalCoord)
    scalePositiveYImage = cv2.warpPerspective(image,M,(0,0))
    return scalePositiveYImage


def scaleNegativeY(image, MinX, MinY, MaxX, MaxY, scaleFactor):
    scaleY = (scaleFactor*MaxY)
    initCoord = np.float32([[MinX,MinY],[MinX,MaxY],[MaxX,MinY],[MaxX,MaxY]])
    finalCoord = np.float32([[MinX,MinY+scaleY],[MinX,MaxY-scaleY],[MaxX,MinY+scaleY],[MaxX,MaxY-scaleY]])
    M = cv2.getPerspectiveTransform(initCoord,finalCoord)
    scaleNegativeYImage = cv2.warpPerspective(image,M,(0,0))
    return scaleNegativeYImage


def scalePositiveXY(image, MinX, MinY, MaxX, MaxY, scaleFactor):
    scaleX = (scaleFactor*MaxX)
    scaleY = (scaleFactor*MaxY)
    initCoord = np.float32([[MinX,MinY],[MinX,MaxY],[MaxX,MinY],[MaxX,MaxY]])
    finalCoord = np.float32([[MinX-scaleX,MinY-scaleY],[MinX-scaleX,MaxY+scaleY],[MaxX+scaleX,MinY-scaleY],[MaxX+scaleX,MaxY+scaleY]])
    M = cv2.getPerspectiveTransform(initCoord,finalCoord)
    scalePositiveXYImage = cv2.warpPerspective(image,M,(0,0))
    return scalePositiveXYImage


def scaleNegativeXY(image, MinX, MinY, MaxX, MaxY, scaleFactor):
    scaleX = (scaleFactor*MaxX)
    scaleY = (scaleFactor*MaxY)
    initCoord = np.float32([[MinX,MinY],[MinX,MaxY],[MaxX,MinY],[MaxX,MaxY]])
    finalCoord = np.float32([[MinX+scaleX,MinY+scaleY],[MinX+scaleX,MaxY-scaleY],[MaxX-scaleX,MinY+scaleY],[MaxX-scaleX,MaxY-scaleY]])
    M = cv2.getPerspectiveTransform(initCoord,finalCoord)
    scaleNegativeXYImage = cv2.warpPerspective(image,M,(0,0))
    return scaleNegativeXYImage


def shearX(image, MinX, MinY, MaxX, MaxY,shearFactorBottomX=0, shearFactorTopX=0):
    initCoord = np.float32([[MinX,MinY],[MinX,MaxY],[MaxX,MinY],[MaxX,MaxY]])
    finalCoord = np.float32([[MinX+shearFactorTopX,MinY],[MinX+shearFactorBottomX,MaxY],[MaxX+shearFactorTopX,MinY],[MaxX+shearFactorBottomX,MaxY]])
    M = cv2.getPerspectiveTransform(initCoord,finalCoord)
    shearXImage = cv2.warpPerspective(image,M,(0,0))
    return shearXImage


def shearY(image, MinX, MinY, MaxX, MaxY,shearFactorLeftY=0, shearFactorRightY=0):
    initCoord = np.float32([[MinX,MinY],[MinX,MaxY],[MaxX,MinY],[MaxX,MaxY]])
    finalCoord = np.float32([[MinX,MinY-shearFactorLeftY],[MinX,MaxY-shearFactorLeftY],[MaxX,MinY-shearFactorRightY],[MaxX,MaxY-shearFactorRightY]])
    M = cv2.getPerspectiveTransform(initCoord,finalCoord)
    shearYImage = cv2.warpPerspective(image,M,(0,0))
    return shearYImage


def rotateX(image, width, height, rotateXAngleBy):
    MinX, MinY, MaxX, MaxY = 0, 0, width, height
    rotateXAngleBy = 60 + rotateXAngleBy/3
    subtractX = math.sqrt((MaxY*MaxY)-((MaxY/2)*(MaxY/2)))
    subtractY = math.cos(math.radians(rotateXAngleBy))*MaxY
    LineX = math.sin(math.radians(rotateXAngleBy))*MaxX 
    LineY = MaxX/2
    X = LineX - subtractX
    Y = LineY - subtractY
    initCoord = np.float32([[MinX,MinY],[MinX,MaxY],[MaxX,MinY],[MaxX,MaxY]])
    finalCoord = np.float32([[MinX+X,MinY+Y],[MinX-X,MaxY-Y],[MaxX-X,MinY+Y],[MaxX+X,MaxY-Y]])
    M = cv2.getPerspectiveTransform(initCoord,finalCoord)
    rotateXImage = cv2.warpPerspective(image,M,(0,0))
    return rotateXImage


def rotateY(image, width, height, rotateYAngleBy):
    MinX, MinY, MaxX, MaxY = 0, 0, width, height
    rotateYAngleBy = 60 + rotateYAngleBy/3
    subtractY = math.sqrt((MaxX*MaxX)-((MaxX/2)*(MaxX/2)))
    subtractX = math.cos(math.radians(rotateYAngleBy))*MaxX
    LineY = math.sin(math.radians(rotateYAngleBy))*MaxX 
    LineX = MaxX/2
    Y = LineY - subtractY
    X = LineX - subtractX
    initCoord = np.float32([[MinX,MinY],[MinX,MaxY],[MaxX,MinY],[MaxX,MaxY]])
    finalCoord = np.float32([[MinX+X,MinY-Y],[MinX+X,MaxY+Y],[MaxX-X,MinY+Y],[MaxX-X,MaxY-Y]])
    M = cv2.getPerspectiveTransform(initCoord,finalCoord)
    rotateYImage = cv2.warpPerspective(image,M,(0,0))
    return rotateYImage


def rotateZ(image, width, height, rotateZAngleBY):
    rotationMatrix = cv2.getRotationMatrix2D((width/2,height/2),(rotateZAngleBY),1)
    rotateZImage = cv2.warpAffine(image, rotationMatrix, (width,height))
    return rotateZImage
