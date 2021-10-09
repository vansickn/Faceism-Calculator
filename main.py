from img_viewer import *
from tkinter import *
from measure_face import *
from PIL import ImageTk, Image
import os
from pathlib import Path


def listdir_nohidden(path):
    # Exclude all with . in the start
    return [i for i in os.listdir(path) if i[0] != "."]


# To configure, add a list of image paths into List_images, and the while loop and imgViewer will do the rest
List_images = []
for p in listdir_nohidden('../FaceismRatioCalculator'):
    if os.path.isdir(p):
        for folder in listdir_nohidden(p):
            print(folder)
            for file in listdir_nohidden('../FaceismRatioCalculator' + '/' + p + '/' + folder):
                print(file)
                if file == 'LQ.png':
                    List_images.append(
                        '../FaceismRatioCalculator' + '/' + p + '/' + folder + '/' + file)


MeasureFace(List_images).measure_picture_list()
