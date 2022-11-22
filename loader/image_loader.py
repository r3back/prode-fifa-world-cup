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
    __instance = None
    picture = None

    @staticmethod
    def get_instance():
        if ImageLoader.__instance is None:
            ImageLoader.__instance = ImageLoader()
        return ImageLoader.__instance

    def get_image_from_file(self, nombre):
        path = str(pathlib.Path(__file__).parent.resolve()) + '/../resources/images'

        os.chdir(path)

        print(os.listdir())

        print("Loader: " + str(PhotoImage(file=nombre)))

        self.picture = PhotoImage(file=nombre)

        return self.picture

    @staticmethod
    def get_image_from_file(nombre):
        path = str(pathlib.Path(__file__).parent.resolve()) + '/../resources/images'

        os.chdir(path)

        print(os.listdir())

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
