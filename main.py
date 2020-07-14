from PIL import Image
import numpy as np
import progressbar
import os, random
from TwitterAPI import TwitterAPI
from imageFunctions import *
from keys import *

if (twitter_api_key is not ''):
      api = TwitterAPI(twitter_api_key, twitter_api_secret, twitter_access_token, twitter_access_token_secret)

### Grab two images from the images directory
image_files = random.sample(os.listdir('./images'), 2)

while '.DS_Store' in image_files:
    image_files = random.sample(os.listdir('./images'), 2)

images = [Image.open(f"./images/{filename}") for filename in image_files]

box = (0, 0, 700, 700)
cropped_images = [resize(image,700).crop(box) for image in images]

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

### Save images to file
new_image.save(f"./output/output.jpg")

## Try to tweet the image
if (twitter_api_key is not ''):
    try:
        file = open("./output/output.jpg", 'rb')
        data = file.read()

        r = api.request('statuses/update_with_media', {'status':' and '.join(image_files)}, {'media[]':data})
    except UnicodeDecodeError:
        print("there was an issue")
else:
    new_image.show()
