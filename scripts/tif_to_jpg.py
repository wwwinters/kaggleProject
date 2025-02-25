#! /usr/bin/env python

###############################################################################
#
# Title:  		Convert tif to jpg
#
# Purpose:		Conver tif formatted images to jpg.  This is to ensure encoding
#				consistance between the images during model training
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
import cv2 as cv
import os

home_dir = '/home/wiley/regis'
src_dir = home_dir+'/dataScience/msds686/week7/kaggleProject/images/data/training/'
labels = ['negative', 'positive']

for label in labels:
    base_path = src_dir+label+'/'
    for file in os.listdir(base_path):
        if file[-3:] != 'jpg':
            print('file: '+file)
            read = cv.imread(base_path+file)
            out = file.split('.')[0]+'.jpg'
            cv.imwrite(base_path+out,read,[int(cv.IMWRITE_JPEG_QUALITY), 200])
        
