# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 12:51:16 2016

@author: Metis
"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

def bin_conv(array):
    array = array[::-1]
    cnt = 0
    for i in array:
        if int(i//1) == 1:
            cnt += 2**i
    return cnt
            


def check(locality, rule):
    binary = format(rule, '008b')
    if np.all(locality== [0,0,0]):
        return int(binary[0])
    elif np.all(locality== [0,0,1]):
        return int(binary[1])
    elif np.all(locality==[0,1,0]):
        return int(binary[2])
    elif np.all(locality==[0,1,1]):
        return int(binary[3])
    elif np.all(locality==[1,0,0]):
        return int(binary[4])
    elif np.all(locality==[1,0,1]):
        return int(binary[5])
    elif np.all(locality==[1,1,0]):
        return int(binary[6])
    elif np.all(locality==[1,1,1]):
        return int(binary[7])

def automata(size, rule):
    image = np.zeros((size/2-1,size))
    image[0][size/2] = 1
    for i in range(len(image)-1):
        for j in range(1, len(image[0])-1):
            image[i+1][j] = check(image[i][j-1:j+2], rule)
    return image

for i in range(144,256):
    plt.imshow(automata(501,i), interpolation='none', cmap='Greys')
    plt.show()