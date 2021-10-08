from img_viewer import *
from tkinter import *
from PIL import ImageTk, Image
import os


List_images = []
for p in os.listdir('../FaceismRatioCalculator'):
    if os.path.isdir(p):
        for folder in os.listdir(p):
            if folder != '.DS_Store':
                for file in os.listdir('../FaceismRatioCalculator' + '/' + p + '/' + folder):
                    if file == 'LQ.png':
                        List_images.append(
                            '../FaceismRatioCalculator' + '/' + p + '/' + folder + '/' + file)

i = 0
while i <= len(List_images):
    t = imgViewer(List_images[i])
    t.createFrame()
    if t.face_exists():
        points = t.get_face_points()
        print(points)
        top_head = points[0]
        bottom_chin = points[1]
        bottom_torso = points[2]
        # [] is x value [1] is y value
        ratio = (bottom_chin[1] - top_head[1]) / \
            (bottom_torso[1] - top_head[1])
        f = open(str(List_images[i]).replace(
            "LQ.png", "") + 'faceismRatio.txt', "w")
        f.write(str(ratio))
        f.close()
    i += 1
