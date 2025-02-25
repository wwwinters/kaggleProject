#! /usr/bin/env python

###############################################################################
#
# Title:  		Extract Images
#
# Version:      0.1
#
# Purpose: 		Images are stored along with their tags in a matlab
#          		formated file.  This script examines the file's lable and
#          		extracts the image to one of three directories base on the
#          		image's classification
#
# Author:   	Wiley Winters
#
# Class:		MSDS 686 - Deep Learning
#
# Assignment:	Kaggle Project
#
# Date:       
#
###############################################################################

#
# Load required libraries and packages
#
import os, re, sys
import os.path
from matplotlib import pyplot as plt
import numpy as np
import h5py
from PIL import Image
from glob import glob

#
# Declare global variables
#
home_dir = '/home/wiley/regis/dataScience/'
trgt_dir = home_dir+'msds686/week7/kaggleProject/images/data/training/positive'
base_dir = '/home/wiley/regis/archive/msds686/kaggleProject/images/cheng/'
total_files = 0
dirs = ['brainTumorDataPublic_1-766',
        'brainTumorDataPublic_767-1532',
        'brainTumorDataPublic_1533-2298',
        'brainTumorDataPublic_2299-3064']

#
# Function to convert mat to jpg
#
def mat_to_jpg(dir, file, num):
    global total_files
    src_file = base_dir+dir+'/'+file
    h5_file = h5py.File(src_file, 'r')
    jpg = file[:-3] + 'jpg'
    cjdata = h5_file['cjdata']
    image = np.array(cjdata.get('image')).astype(np.float64)
    label = cjdata.get('label')[0,0]
    h5_file.close()
    hi = np.max(image)
    lo = np.min(image)
    image = (((image - lo) / (hi - lo)) * 255).astype(np.uint8)
    im = Image.fromarray(image)
    im.save(trgt_dir+'/'+jpg)
    total_files += 1
    print('Saving', jpg, 'File no ', num)

for dir in dirs:
    path = base_dir+dir
    files = os.listdir(path)
    for file in files:
        mat_to_jpg(dir, file, total_files)

print('Finished converting all files: ', total_files)   