from PIL import Image
import imageio
import os

img_list = []
img_list = [item for item in input('Enter files with space:- ').split()]

print(img_list)

images = []

for filename in img_list:
    images.append(imageio.imread(filename))

path = input('Enter path were file should be saved with forward slash')
imageio.mimsave(path, images)
