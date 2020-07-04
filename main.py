from PIL import Image
import numpy as np
import progressbar
import os, random
from imageFunctions import *

### Grab two images from the images directory
image_files = random.sample(os.listdir('./images'), 2)

if '.DS_Store' in image_files:
    while not '.DS_Store' in image_files:
        image_files = random.sample(os.listdir('./images'), 2)

print('Using:')
print(image_files)
images = [Image.open(f"./images/{filename}") for filename in image_files]

box = (0, 0, 700, 700)
cropped_images = [resize(image,700).crop(box) for image in images]

### convert first image to np Array
# image_array = np.array(cropped_images[0])
# nparray_to_image(image_array).show()
#
# # new_image_array = modified_image_array(np.array(cropped_images[0]), turn_white_things_yellow)
# new_image_array = modified_image_array(np.array(cropped_images[0]))
# nparray_to_image(new_image_array).show()

### perform logic based off of pixel values
image_arrays = [np.array(image) for image in cropped_images]
new_image = []
image_one = image_arrays[0]
image_two = image_arrays[1]
color_limit = random.randint(150, 400)

with progressbar.ProgressBar(max_value=len(image_one)) as bar:
    for row in range(len(image_one)):
        bar.update(row)
        new_row = []
        for col in range(len(image_one[0])):
            pixel = image_one[row][col]
            if(sum(color for color in pixel)>color_limit):
                new_row.append(image_two[row][col])
            else:
                new_row.append(pixel)
        new_image.append(new_row)

new_image = nparray_to_image(new_image)

new_image.show()

### Save images to file
new_image.save(f"./output/output.jpg")
