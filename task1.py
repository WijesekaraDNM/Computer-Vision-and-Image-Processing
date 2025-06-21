import cv2
import numpy as np

def reduce_intensity_levels(image_path, levels):
    # Read the image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Calculate the scaling factor
    scale = 256 / levels
    
    # Reduce intensity levels
    reduced_img = np.floor(img / scale) * scale
    
    # Convert to uint8
    reduced_img = reduced_img.astype(np.uint8)
    
    # Display results
    cv2.imshow('Original Image', img)
    cv2.imshow(f'Reduced to {levels} levels', reduced_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
