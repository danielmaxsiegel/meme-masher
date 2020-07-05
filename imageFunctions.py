from PIL import Image
import numpy as np

### Modifiers
def nparray_to_image(array):
    return Image.fromarray(np.uint8(array))

def modified_image_array(array, modification=None):
    output = []
    for row in array:
        new_row = []
        for pixel in row:
            if modification is None:
                new_row.append(pixel)
            else:
                new_row.append(modification(pixel))
        output.append(new_row)
    return output

### Size
def resize(image,smallest_side):
    current_size = image.size
    x,y = current_size
    if x > y:
        ratio = smallest_side / y
    else:
        ratio = smallest_side / x
    return image.resize([int(side * ratio) for side in current_size])

### Color
def redify(pixel):
    red,green,blue = pixel
    new_red = red + 40
    if new_red > 255:
        new_red = 255
    return [new_red,green,blue]

def greenify(pixel):
    red,green,blue = pixel
    new_green = green + 40
    if new_green > 255:
        new_green = 255
    return [red,new_green,blue]

def blueify(pixel):
    red, green, blue = pixel
    new_red = red + 60
    if (new_red > 255):
        new_red = 255
    return [new_red, green, blue]

def turn_white_things_yellow(pixel):
    if sum(color for color in pixel) > 500:
        return [255,255,0]
    else:
        return pixel




# Usage
### convert first image to np Array
# image_array = np.array(cropped_images[0])
# nparray_to_image(image_array).show()
#
# # new_image_array = modified_image_array(np.array(cropped_images[0]), turn_white_things_yellow)
# new_image_array = modified_image_array(np.array(cropped_images[0]))
# nparray_to_image(new_image_array).show()
