import PIL
import os
from PIL import Image

def resize(filepath):
    basewidth = 500
    try:
        img = Image.open(filepath)
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        img.save('resized_image.jpg')
    except IOError:
        print('image failure')
        os.remove(filepath)

    try:
        baseheight = 500
        img = Image.open('resized_image.jpg')
        hpercent = (baseheight / float(img.size[1]))
        wsize = int((float(img.size[0]) * float(hpercent)))
        img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
        img.save(filepath)
        os.remove('resized_image.jpg')
    except IOError:
        print('image failure')
        os.remove(filepath)


training_dir = os.getcwd() + '\\table'
for filename in os.listdir(training_dir):
    resize(os.path.join(training_dir, filename))
