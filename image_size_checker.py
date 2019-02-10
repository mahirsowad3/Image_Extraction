import PIL
from PIL import Image
import os


def size_check(file_dir):
    im = Image.open(file_dir)
    width, height = im.size
    if width > 1000 or height > 1000:
        print("Check: " + file_dir)



training_dir = os.getcwd() + '\\table'
for filename in os.listdir(training_dir):
    size_check(os.path.join(training_dir, filename))