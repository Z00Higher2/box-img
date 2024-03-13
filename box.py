import numpy as np


MAX_H = 512
MAX_W = 512

# Function to read the input image from a file
def read_image():
    with open("inImage.pgm", "r") as file:
        # Read and validate the PGM file header
        assert file.readline().strip() == 'P2'
        
        # Skip any comments in the file
        while file.peek(1) == b'#':
            file.readline()
        
        # Read image width, height, and maximum pixel value
        width, height = map(int, file.readline().split())
        assert width <= MAX_W
        assert height <= MAX_H
        max_val = int(file.readline().strip())
        assert max_val == 255
        
        # Read pixel values into the image array
        image = np.zeros((height, width), dtype=np.int32)
        for row in range(height):
            image[row] = list(map(int, file.readline().split()))
        
        return image, height, width

# Function to write the output image to a file
def write_image(image):
    height, width = image.shape
    
    with open("outImage.pgm", "w") as file:
        # Write the PGM file header
        file.write("P2\n")
        file.write(f"{width} {height}\n")
        file.write("255\n")
        
        # Write pixel values to the output file
        for row in range(height):
            for col in range(width):
                file.write(f"{image[row, col]} ")
            file.write("\n")

def main():
    # Read the input image from the file
    img, h, w = read_image()

    # Copy the input image to the output image
    out = np.copy(img)

    # Calculate dimensions and position of the 50/50 dimensional box
    box_width = w // 2
    box_height = h // 2
    box_start_x = (w - box_width) // 2
    box_start_y = (h - box_height) // 2

    # Perform the image processing (creating the 50/50 dimensional box)
    out[box_start_y:box_start_y + box_height, box_start_x:box_start_x + box_width] = 255

    # Write the processed image to the output file
    write_image(out)

if __name__ == "__main__":
    main()
