import os
from PIL import Image

directory_list = ['bed', 'car', 'chair', 'door', 'stairs', 'table']


def change_files(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith('.jpe'):
            abs_filename = os.path.join(directory, filename)
            root_name = os.path.splitext(filename)[0]
            abs_root_name = os.path.join(directory, root_name)
            os.rename(abs_filename, abs_root_name + '.jpg')
        elif filename.lower().endswith('.png'):
            abs_filename = os.path.join(directory, filename)
            root_name = os.path.splitext(filename)[0]
            abs_root_name = os.path.join(directory, root_name)
            im = Image.open(abs_filename)
            try:
                rgb_im = im.convert('RGB')
                rgb_im.save(abs_root_name + '.jpg')
            except IOError:
                print("Found an unreadable image.")

            os.remove(abs_filename)


training_dir = os.getcwd() + '\\table'
change_files(training_dir)