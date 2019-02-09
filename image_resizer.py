import PIL
import os
from PIL import Image

def resize(filepath):
    basewidth = 640
    img = Image.open(filepath)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    img.save('resized_image.jpg')

    baseheight = 480
    img = Image.open('resized_image.jpg')
    hpercent = (baseheight / float(img.size[1]))
    wsize = int((float(img.size[0]) * float(hpercent)))
    img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
    img.save(filepath)
    os.remove('resized_image.jpg')


training_dir = os.getcwd() + '\car'
for filename in os.listdir(training_dir):
    resize(os.path.join(training_dir, filename))