#! /usr/bin/env python

###############################################################################
#
# Title:  		Extract Images
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
from os import path
import os, re, sys
from matplotlib import pyplot as plt
import numpy as np
import h5py
from PIL import Image
from glob import glob

#
# Declare global variables
#
base_dir = '/home/wiley/regis/dataScience/msds686/week7/kaggleProject/images'
src_dir = base_dir+'/1512427/images/'
meni_dst = base_dir+'/meningioma/'
glio_dst = base_dir+'/glioma/'
pitu_dst = base_dir+'/pituitary/'
total_files = 0

#
# Get file names
#
files = os.listdir(src_dir)

#
# Function to convert mat to jpg
#
def mat_to_jpg(file, num):
    global total_files
    src_file = src_dir+file
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
    # The mat file contains a label field that is associated with
    # a tumor type.
    # 1 -- Meningioma
    # 2 -- Glioma
    # 3 -- Pituitary
    # Converted files will be stored by tumor type
    if label == 1:
        im.save(meni_dst+jpg)
        total_files += 1
    if label == 2:
        im.save(glio_dst+jpg)
        total_files += 1
    if label == 3:
        im.save(pitu_dst+jpg)
        total_files += 1
 
    print('Saving', jpg, 'File no ', num)
        
for file in files:
    mat_to_jpg(file, total_files)
    
print('Finished converting all files: ', total_files)   