import numpy as np
import matplotlib.pyplot as plt
from pylab import imshow
from PIL import Image


import scipy.signal


import sys
sys.path.append('../')


import curvature_1D as c1D
import curvature_2D_sameunit as c2D_sm
import curvature_2D_inequivalent as c2D_in
import savitzky_golay as sg



fichier_image="gr83.txt"
data = np.loadtxt(fichier_image)

num_line = len(data)
num_column = len(data[1])

EDC=-1.4    #colonne
MDC=0  #ligne


data=data[::-1]
ligne_original, colonne_original = data.shape

amplitude = 2.5e-5

plt.figure(1)
imshow(data, aspect="auto")
plt.title("Original image")
plt.xlabel("X")
plt.ylabel("Y")
#plt.close()

data2 = c2D_in.curv_2D(data, amplitude)
plt.figure(2)
imshow(data2, vmin=0, vmax=300, aspect="auto")
plt.title("Image treated")
plt.xlabel("alpha")
plt.ylabel("energy ")

filtered_data = sg.sgolay2d( data, window_size=11, order=4)

data3 = c2D_in.curv_2D(filtered_data, amplitude)
plt.figure(3)
imshow(data3, vmin=0, vmax=300, aspect="auto")
plt.title('Image treated after an filtering step')
plt.xlabel("alpha")
plt.ylabel("energy ")

plt.show()
plt.close()


