# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 16:09:09 2016

@author: Metis
"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import pyfits

timesteps = 20
rule = 19

def bin_conv(array):
    array = array[::-1]
    cnt = 0
    for idx, i in enumerate(array):
        if int(np.round(i)) == 1:
            cnt += 2**idx
    return cnt


def check_locality(rule, locality):
    index = bin_conv(locality)
    binary = format(rule, '032b')
    return int(binary[index])
    
    
def Threshold(image, thresh):
    im = image.copy()
    for i in range(len(im)):
        for j in range(len(im[0])):
            if im[i][j] < thresh:
                im[i][j]=0
            else:
                im[i][j]=1
    return im   
    
    
def twod(image, rule, timesteps):
    x_size = len(image)
    y_size = len(image[0])
    next_image = np.zeros((x_size, y_size))
    for t in xrange(timesteps):
        for i in xrange(x_size):
            for j in xrange(y_size):
                next_image[i,j] = check_locality(rule, [image[i,(j+1)%y_size], image[(i-1)%x_size,j], image[i,j], image[(i+1)%x_size,j], image[i,(j-1)%y_size]])
        image = next_image.copy()
        next_image = np.ones((x_size, y_size))
    return image
    
    
print format(rule, '032b')
        
size=50
seed = np.ones((size,size))
seed[25,25] = 0
#seed[24,25] = 0
#seed[26,25] = 0
#seed[25,24] = 0
#seed[25,26] = 0

im = pyfits.open('CenALobes.fits')[0].data
#seed = Threshold(im,np.percentile(im, 85))

for i in range(10007147, 10010000, 2):
    image = twod(seed, i, timesteps)
    plt.imshow(image, interpolation='nearest', cmap='viridis')
    plt.colorbar()
    print i
    plt.show()