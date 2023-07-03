# Maximizes the lossless PNG compression on all images in a directory.

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

def set_png_compression_level(image_paths):
    if len(image_paths) <= 0:
        print("No images to change")
        return

    for filepath in image_paths:
        image = Image.open(filepath)
        image.save(filepath, format="PNG", compress_level=9)

image_paths = get_images_from_directory(directory)
set_png_compression_level(image_paths)