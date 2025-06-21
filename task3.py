import cv2
import numpy as np

def rotate_image(image_path):
    # Read the image
    img = cv2.imread(image_path)
    h, w = img.shape[:2]
    
    # 45 degree rotation
    center = (w // 2, h // 2)
    M_45 = cv2.getRotationMatrix2D(center, 45, 1.0)
    rotated_45 = cv2.warpAffine(img, M_45, (w, h))
    
    # 90 degree rotation
    M_90 = cv2.getRotationMatrix2D(center, 90, 1.0)
    rotated_90 = cv2.warpAffine(img, M_90, (w, h))
    
    # Display results
    cv2.imshow('Original Image', img)
    cv2.imshow('Rotated 45 degrees', rotated_45)
    cv2.imshow('Rotated 90 degrees', rotated_90)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    