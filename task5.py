import cv2
import numpy as np
from task1 import reduce_intensity_levels
from task2 import spatial_averaging
from task3 import rotate_image
from task4 import block_averaging

def main():
    print("Image Processing Operations:")
    print("1. Reduce Intensity Levels")
    print("2. Spatial Averaging")
    print("3. Image Rotation")
    print("4. Block Averaging")
    
    choice = int(input("Enter your choice (1-4): "))
    image_path = input("Enter image path: ")
    
    if choice == 1:
        levels = int(input("Enter number of intensity levels (power of 2): "))
        success = reduce_intensity_levels(image_path, levels)
    elif choice == 2:
        success = spatial_averaging(image_path)
    elif choice == 3:
        success = rotate_image(image_path)
    elif choice == 4:
        block_size = int(input("Enter block size (3, 5, or 7): "))
        success = block_averaging(image_path, block_size)
    else:
        print("Invalid choice!")

# Include all the functions defined above

if __name__ == "__main__":
    main()