import cv2
import numpy as np

def block_averaging(image_path, block_size):
    # Read the image
    img = cv2.imread(image_path)
    h, w = img.shape[:2]
    
    # Calculate number of blocks in each dimension
    h_blocks = h // block_size
    w_blocks = w // block_size
    
    # Create output image
    output = np.zeros_like(img)
    
    # Process each block
    for i in range(h_blocks):
        for j in range(w_blocks):
            # Get the block
            block = img[i*block_size:(i+1)*block_size, j*block_size:(j+1)*block_size]
            
            # Calculate average color
            avg_color = np.mean(block, axis=(0, 1))
            
            # Apply average color to all pixels in the block
            output[i*block_size:(i+1)*block_size, j*block_size:(j+1)*block_size] = avg_color
    
    # Display results
    cv2.imshow('Original Image', img)
    cv2.imshow(f'Block Averaging {block_size}x{block_size}', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

