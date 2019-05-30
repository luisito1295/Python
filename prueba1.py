# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 16:41:40 2018

@author: lpere
"""
from skimage import io
import matplotlib.pyplot as plt
import numpy as np
from skimage import data
from skimage.color import rgb2hed
from matplotlib.colors import LinearSegmentedColormap
from skimage import filters
from skimage.color import rgb2gray

# Create an artificial color close to the orginal one
cmap_hema = LinearSegmentedColormap.from_list('mycmap', ['white', 'navy'])
cmap_dab = LinearSegmentedColormap.from_list('mycmap', ['white','saddlebrown'])
cmap_eosin = LinearSegmentedColormap.from_list('mycmap', ['darkviolet','white'])
cmap_bn = LinearSegmentedColormap.from_list('mymap',['white','black'])

imagen = io.imread("a.jpg")
imagen_g = rgb2gray(imagen)

fig, axes = plt.subplots(4, 4, figsize=(13, 13), sharex=True, sharey=True)
ax = axes.ravel()

ax[0].imshow(imagen)
ax[0].set_title("Original image")

ax[1].imshow(imagen[:, :, 0], cmap=cmap_hema)
ax[1].set_title("Hematoxylin")

ax[2].imshow(imagen[:, :, 1], cmap=cmap_eosin)
ax[2].set_title("Eosin")

ax[3].imshow(imagen[:, :, 2], cmap=cmap_dab)
ax[3].set_title("DAB")

ax[4].imshow(imagen[:, :, 2], cmap=cmap_bn)
ax[4].set_title("Blanco y Negro")


for a in ax.ravel():
    a.axis('off')

fig.tight_layout()
plt.show()