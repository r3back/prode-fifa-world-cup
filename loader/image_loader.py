import io
import os
import pathlib
from tkinter import PhotoImage
from PIL import Image, ImageTk

try:
    # Python2
    import Tkinter as tk
    from urllib2 import urlopen
except ImportError:
    # Python3
    import tkinter as tk
    from urllib.request import urlopen


class ImageLoader:
    @staticmethod
    def get_image_from_file(nombre):
        path = str(pathlib.Path(__file__).parent.resolve()) + '/../resources/images'

        os.chdir(path)

        return PhotoImage(file=nombre)

    @staticmethod
    def get_image_from_url(url):
        my_page = urlopen(url)
        # create an image file object
        my_picture = io.BytesIO(my_page.read())
        # use PIL to open image formats like .jpg  .png  .gif  etc.
        pil_img = Image.open(my_picture)
        # convert to an image Tkinter can use
        return ImageTk.PhotoImage(pil_img)

    @staticmethod
    def get_image_from_url_resized(url, height, width):
        my_page = urlopen(url)
        # create an image file object
        my_picture = io.BytesIO(my_page.read())
        # use PIL to open image formats like .jpg  .png  .gif  etc.
        pil_img = Image.open(my_picture)

        new_image= pil_img.resize((height, width), Image.ANTIALIAS)

        # convert to an image Tkinter can use
        return ImageTk.PhotoImage(new_image)
