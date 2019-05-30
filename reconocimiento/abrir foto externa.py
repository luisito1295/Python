#aja# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 19:16:36 2018

@author: luisl
"""

'''from skimage import io

img = io.imread('a.jpg')
io.imshow(img)
io.show()'''
'''
# Librerias necesarias
from skimage import io
from skimage import filters
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

# Abrimos la imagen
imagen = io.imread("a.jpg")
imagen_g = rgb2gray(imagen)

# Filtros: sobel, roberts, prewitt
filtros = [filters.sobel, filters.roberts, filters.prewitt]

for filtro in filtros:
    # Aplicamos cada uno de los filtros
    img_fil = filtro(imagen_g)
    
    # Mostramos los resultados 
    plt.imshow(img_fil)
    plt.show()'''

'''#Mejoramiento del contraste:
from skimage import exposure
from skimage import io
import numpy as np
import matplotlib.pyplot as plt

imagen = io.imread("h.jpg")

# Estiramiento de contraste
p2, p98 = np.percentile(imagen, (2,98))
img_rescale = exposure.rescale_intensity(imagen, in_range=(p2,p98))

# Ecualización
img_eq = exposure.equalize_hist(imagen)

# Ecualización adaptiva
img_adapteq = exposure.equalize_adapthist(imagen, clip_limit=0.03)

for eq in (img_eq, img_adapteq):
    plt.imshow(eq)
    plt.show()'''


'''#Eliminación de ruido:    
from skimage import io
from skimage.filters.rank import median
#from skimage.morphology import disk
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

imagen = io.imread("a.jpg")
img_gray = rgb2gray(imagen)

med = median(img_gray)

plt.imshow(med)
plt.show()
'''

'''#Restauración:
from skimage import restoration
from scipy.signal import convolve2d
from skimage import io
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pyplot as plt

imagen = io.imread("a.jpg")

img = rgb2gray(imagen)

psf = np.ones((5,5)) / 25

img = convolve2d(img, psf, 'same')
img += 0.1 * img.std() * np.random.standard_normal((img.shape))
deconvolved_img = restoration.wiener(img, psf, 100)

plt.imshow(deconvolved_img)
plt.show()'''



'''
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from scipy.signal import convolve2d as conv2

from skimage import color, data, restoration

img = io.imread("a.jpg")

astro = color.rgb2gray(img)

psf = np.ones((5, 5)) / 25
astro = conv2(astro, psf, 'same')
# Add Noise to Image
astro_noisy = astro.copy()
astro_noisy += (np.random.poisson(lam=25, size=astro.shape) - 10) / 255.

# Restore Image using Richardson-Lucy algorithm
deconvolved_RL = restoration.richardson_lucy(astro_noisy, psf, iterations=30)

fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(8, 5))
plt.gray()

for a in (ax[0], ax[1], ax[2]):
       a.axis('off')

ax[0].imshow(astro)
ax[0].set_title('Original Data')

ax[1].imshow(astro_noisy)
ax[1].set_title('Noisy data')

ax[2].imshow(deconvolved_RL, vmin=astro_noisy.min(), vmax=astro_noisy.max())
ax[2].set_title('Restoration using\nRichardson-Lucy')


fig.subplots_adjust(wspace=0.02, hspace=0.2,
                    top=0.9, bottom=0.05, left=0, right=1)
plt.show()'''
import matplotlib.pyplot as plt
from skimage import io,color

img = io.imread('a.jpg')
imggris=color.rgb2gray(img)
plt.subplot(211)
io.imshow(img)
plt.subplot(212)
io.imshow(imggris)
io.show()