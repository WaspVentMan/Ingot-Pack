# Changes to the color mode of all images within the chosen directory to RGBA.

import os
from PIL import Image

directory = "test"

def get_images_from_directory(directory):
    image_paths = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".png"):
                filepath = os.path.join(root, filename)
                image_paths.append(filepath)
    return image_paths

def set_rgb_color_mode(image_paths):
    if len(image_paths) <= 0:
        print("No images to convert")
        return

    for filepath in image_paths:
        image = Image.open(filepath)
        if image.mode != "RGB" or image.mode != "RGBA":
            image = image.convert("RGBA")
            image.save(filepath)

image_paths = get_images_from_directory(directory)
set_rgb_color_mode(image_paths)