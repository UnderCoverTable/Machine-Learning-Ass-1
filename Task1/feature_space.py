import pandas as pd
from PIL import Image
import numpy


trainDF = pd.read_excel('Train.xlsx')

imagePaths = trainDF['Path'].tolist()


image = Image.open(imagePaths[0])

print(image.format)
print(image.size)
print(image.mode)

np_array_img = numpy.array(image)
np_array_img = np_array_img.flatten()
print(np_array_img)
print(len(np_array_img))