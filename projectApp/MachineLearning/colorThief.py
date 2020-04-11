import cv2
from colorthief import ColorThief
import os
import matplotlib.pyplot as plt
import numpy as np

sourceDir = r"C:\Users\buchi\OneDrive - Technological University Dublin\DT211c4\Dissertation\Dataset-Grabcut\Sunflower"
imageDirs = os.listdir(sourceDir)
domi = []
#
# for image in imageDirs:
#     path = os.path.join(sourceDir, image)  # full path of each image
#     print(path)
#
#     color_thief = ColorThief(path)
#     # get the dominant color
#     # dominant_color = color_thief.get_color(quality=1)
#     # print(dominant_color)
#
#     palette = color_thief.get_palette(color_count=6)
#
#     #print(palette)
#
#     min_value = min(palette)
#
#     result = []
#     for i in palette:
#         if i > min_value:
#             result.append(i)
#
#     # print(result)
#     # print(palette[0])
#     # get top dominant colour
#     dominant_colour = result[0]
#
#     # add to the list
#     domi.append(dominant_colour)
#
#
# print(domi)
# print(len(domi))



# plt.imshow(domi)
# plt.show()





# color_thief = ColorThief(r"C:\Users\buchi\OneDrive - Technological University Dublin\DT211c4\Dissertation\Dataset-Grabcut\Barbeton Daisy\g11.jpg")
# # get the dominant color
# # dominant_color = color_thief.get_color(quality=1)
# # print(dominant_color)
#
# palette = color_thief.get_palette(color_count=6)
#
# print(palette)
#
# min_value = min(palette)
# print(min_value)
# result = []
# for i in palette:
#     if i > min_value:
#         result.append(i)
#
# # print(result)
# print(result[0])
#
