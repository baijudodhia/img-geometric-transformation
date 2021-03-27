import sys
import cv2
from GeometricTransformations import GeometricTransformations as gt

if __name__ == "__main__":
    img = cv2.imread(str(sys.argv[1]))
    # cv2.imshow('image', img)
    i = 0
    while i != 7:
        print("Press enter number")
        print("1. Perspective Change")
        print("2. Translate")
        print("3. Scale")
        print("4. Shear")
        print("5. Rotate")
        print("6. Flip")
        print("7. END")
        try:
            i = int(input())
        except:
            i = 0
        if i == 1:
            print("Enter Perspective Type")
            print("1. Left Zoom In X")
            print("2. Left Zoom In Y")
            print("3. Left Zoom Out X")
            print("4. Left Zoom Out Y")
            print("5. Right Zoom In X")
            print("6. Right Zoom In Y")
            print("7. Right Zoom Out X")
            print("8. Right Zoom Out Y")
            j = int(input())
            print("Enter Perspective Factor")
            if j == 1:
                k = int(input())
                ih, iw, ic = img.shape
                img = gt.perspectiveLeftZoomInX(img,iw,ih,k)
                cv2.imwrite('img_perspectiveLeftZoomInX.jpg', img)
            elif j == 2:
                k = int(input())
                ih, iw, ic = img.shape
                img = gt.perspectiveLeftZoomInY(img,iw,ih,k)
                cv2.imwrite('img_perspectiveLeftZoomInY.jpg', img)
            elif j == 3:
                k = int(input())
                ih, iw, ic = img.shape
                img = gt.perspectiveLeftZoomOutX(img,iw,ih,k)
                cv2.imwrite('img_perspectiveLeftZoomOutX.jpg', img)
            elif j == 4:
                k = int(input())
                ih, iw, ic = img.shape
                img = gt.perspectiveLeftZoomOutY(img,iw,ih,k)
                cv2.imwrite('img_perspectiveLeftZoomOutY.jpg', img)
            elif j == 5:
                k = int(input())
                ih, iw, ic = img.shape
                img = gt.perspectiveRightZoomInX(img,iw,ih,k)
                cv2.imwrite('img_perspectiveRightZoomInX.jpg', img)
            elif j == 6:
                k = int(input())
                ih, iw, ic = img.shape
                img = gt.perspectiveRightZoomInY(img,iw,ih,k)
                cv2.imwrite('img_perspectiveRightZoomInY.jpg', img)
            elif j == 7:
                k = int(input())
                ih, iw, ic = img.shape
                img = gt.perspectiveRightZoomOutX(img,iw,ih,k)
                cv2.imwrite('img_perspectiveRightZoomOutX.jpg', img)
            elif j == 8:
                k = int(input())
                ih, iw, ic = img.shape
                img = gt.perspectiveRightZoomOutY(img,iw,ih,k)
                cv2.imwrite('img_perspectiveRightZoomOutY.jpg', img)
        elif i ==  2:
            print("Enter Translation Type")
            print("1. Negative X")
            print("2. Negative Y")
            print("3. Positive X")
            print("4. Positive Y")
            j = int(input())
            print("Enter Translation Factor")
            if j == 1:
                k = int(input())
                ih, iw, ic = img.shape
                img = gt.translateNegativeX(img,iw,ih,k)
                cv2.imwrite('img_translateNegativeX.jpg', img)
            elif j == 2:
                k = int(input())
                ih, iw, ic = img.shape
                img = gt.translateNegativeY(img,iw,ih,k)
                cv2.imwrite('img_translateNegativeY.jpg', img)
            elif j == 3:
                k = int(input())
                ih, iw, ic = img.shape
                img = gt.translatePositiveX(img,iw,ih,k)
                cv2.imwrite('img_translatePositiveX.jpg', img)
            elif j == 4:
                k = int(input())
                ih, iw, ic = img.shape
                img = gt.translatePositiveY(img,iw,ih,k)
                cv2.imwrite('img_translatePositiveY.jpg', img)
        elif i ==  3:
            print("Enter Scale Type")
            print("1. Negative X")
            print("2. Negative Y")
            print("3. Negative XY")
            print("4. Positive X")
            print("5. Positive Y")
            print("6. Positive XY")
            j = int(input())
            print("Enter Translation Factor")
            if j == 1:
                k = int(input())
                ih, iw, ic = img.shape
                img = gt.scaleNegativeX(img,iw,ih,k)
                cv2.imwrite('img_scaleNegativeX.jpg', img)
            elif j == 2:
                k = int(input())
                ih, iw, ic = img.shape
                img = gt.scaleNegativeY(img,iw,ih,k)
                cv2.imwrite('img_scaleNegativeY.jpg', img)
            elif j == 3:
                k = int(input())
                ih, iw, ic = img.shape
                img = gt.scaleNegativeXY(img,iw,ih,k)
                cv2.imwrite('img_scaleNegativeXY.jpg', img)
            elif j == 4:
                k = int(input())
                ih, iw, ic = img.shape
                img = gt.scalePositiveX(img,iw,ih,k)
                cv2.imwrite('img_scalePositiveX.jpg', img)
            elif j == 5:
                k = int(input())
                ih, iw, ic = img.shape
                img = gt.scalePositiveY(img,iw,ih,k)
                cv2.imwrite('img_scalePositiveY.jpg', img)
            elif j == 6:
                k = int(input())
                ih, iw, ic = img.shape
                img = gt.scalePositiveXY(img,iw,ih,k)
                cv2.imwrite('img_scalePositiveXY.jpg', img)
        elif i ==  4:
            print("Enter Shear Type")
            print("1. Shear X")
            print("2. Shear Y")
            j = int(input())
            print("Enter Shear Factor")
            if j == 1:
                k = int(input())
                ih, iw, ic = img.shape
                img = gt.shearX(img,iw,ih,k)
                cv2.imwrite('img_shearX.jpg', img)
            elif j == 2:
                k = int(input())
                ih, iw, ic = img.shape
                img = gt.shearY(img,iw,ih,k)
                cv2.imwrite('img_shearY.jpg', img)
        elif i ==  5:
            print("Enter Rotate Type")
            print("1. Rotate X")
            print("2. Rotate Y")
            print("3. Rotate Z")
            j = int(input())
            print("Enter Shear Factor")
            if j == 1:
                k = int(input())
                ih, iw, ic = img.shape
                img = gt.rotateX(img,iw,ih,k)
                cv2.imwrite('img_rotateX.jpg', img)
            elif j == 2:
                k = int(input())
                ih, iw, ic = img.shape
                img = gt.rotateY(img,iw,ih,k)
                cv2.imwrite('img_rotateY.jpg', img)
            elif j == 3:
                k = int(input())
                ih, iw, ic = img.shape
                img = gt.rotateZ(img,iw,ih,k)
                cv2.imwrite('img_rotateZ.jpg', img)
        elif i ==  6:
            print("Enter Flip Type")
            print("1. Flip X")
            print("2. Flip Y")
            j = int(input())
            if j == 1:
                ih, iw, ic = img.shape
                img = gt.flipX(img,iw,ih)
                cv2.imwrite('img_flipX.jpg', img)
            elif j == 2:
                ih, iw, ic = img.shape
                img = gt.flipY(img,iw,ih)
                cv2.imwrite('img_flipY.jpg', img)
        elif i == 7:
            break
        else:
            print("You entered wrong value!")