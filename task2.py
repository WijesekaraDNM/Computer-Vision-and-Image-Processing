import cv2
import numpy as np

def spatial_averaging(image_path):
    # Read the image
    img = cv2.imread(image_path)
    
    # 3x3 average
    kernel_3x3 = np.ones((3,3), np.float32) / 9
    avg_3x3 = cv2.filter2D(img, -1, kernel_3x3)
    
    # 10x10 average
    kernel_10x10 = np.ones((10,10), np.float32) / 100
    avg_10x10 = cv2.filter2D(img, -1, kernel_10x10)
    
    # 20x20 average
    kernel_20x20 = np.ones((20,20), np.float32) / 400
    avg_20x20 = cv2.filter2D(img, -1, kernel_20x20)
    
    # Display results
    cv2.imshow('Original Image', img)
    cv2.imshow('3x3 Average', avg_3x3)
    cv2.imshow('10x10 Average', avg_10x10)
    cv2.imshow('20x20 Average', avg_20x20)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
