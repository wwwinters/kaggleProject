#! /usr/bin/env python

###############################################################################
#
# Title:  		Create Validation Set
#
# Version:      0.1
#
# Purpose:		Randomly select 15% of files from the image classes and
#       		separate them into their own directory structure.  This
#				will be used during model development to validate its
#				performance
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
import os, shutil
import numpy as np

#
# Declare global variables
#
base_dir = '/home/wiley/regis/dataScience/msds686/week7/kaggleProject/images/data'
trn_dir = base_dir+'/training/'
val_dst = base_dir+'/validation/'

#
# Do the work
#

for category in ('negative', 'positive'):
    if not os.path.exists(val_dst+category):
        os.makedirs(val_dst+category)
    else:
        shutil.rmtree(val_dst+category)
        os.makedirs(val_dst+category)
    files = os.listdir(trn_dir+category)
    np.random.shuffle(files)
    num_samples = int(0.15*len(files))
    val_files = files[-num_samples:]
    for fname in val_files:
        shutil.move(trn_dir+category+'/'+fname,
                    val_dst+category+'/'+fname)