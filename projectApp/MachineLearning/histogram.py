import cv2
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter
from PIL import Image


# https://python.hotexamples.com/examples/cv2/-/calcHist/python-calchist-function-examples.html
img = cv2.imread(r'C:\Users\buchi\OneDrive - Technological University Dublin\DT211c4\Dissertation\Dataset-Grabcut\Marigold\a6.jpg'
                      , cv2.IMREAD_COLOR)

imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
colour = ['b', 'g','r']
histH = cv2.calcHist([imgHsv], [0], None, [180], [0, 180])
histS = cv2.calcHist([imgHsv], [1], None, [256], [0, 256])
histV = cv2.calcHist([imgHsv], [2], None, [256], [0, 256])


maxTuple = (
    [i for i, j in enumerate(histH) if j == max(histH)][0],
    [i for i, j in enumerate(histS) if j == max(histS)][0],
    [i for i, j in enumerate(histV) if j == max(histV)][0],
)


# print(np.uint8([i for i, j in enumerate(histH) if j == max(histH)]))
# print(np.uint8([i for i, j in enumerate(histS) if j == max(histS)]))
# print(np.uint8([i for i, j in enumerate(histV) if j == max(histV)]))
arr = []
arr1 = []
arr2 = []
print("this is h")
for j in histH:
    # print(np.uint8(j))
    # arr[i] = (np.uint8(j))
    arr.append(np.uint8(int(j)))

print(arr)
print(Counter(arr))
print("this is s")
for j in histS:
    # print(np.uint8(j))
    # arr[i] = (np.uint8(j))
    arr1.append(np.uint8(int(j)))

print(arr1)
print(Counter(arr1))
print("this is v")

for j in histV:
    # print(np.uint8(j))
    # arr[i] = (np.uint8(j))
    arr2.append(np.uint8(int(j)))

print(arr2)
print(Counter(arr2))

color = np.uint8([[[maxTuple[0], maxTuple[1], maxTuple[2]]]])
mainColor = cv2.cvtColor(color, cv2.COLOR_HSV2RGB)
mainColor = (list(mainColor)[0][0][0], list(mainColor)[0][0][1], list(mainColor)[0][0][2])


print(mainColor)

# plot the graph
plt.plot(histH, color=colour[0])
plt.xlim([0, 256])
plt.show()


image = Image.open(r'C:\Users\buchi\OneDrive - Technological University Dublin\DT211c4\Dissertation\Dataset-Grabcut\Marigold\a6.jpg')
image.show()