#! /usr/bin/env python

###############################################################################
#
# Title:  		Create Testset
#
# Version:      0.1
#
# Purpose:		Randomly select 20% of files from the image classes and
#       		separate them into their own directory structure.  This
#				will be used during model development to test its
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
base_dir = '/home/wiley/regis/dataScience/kaggleProject/images/data'
trn_dir = base_dir+'/training/'
tst_dst = base_dir+'/testing/'

#
# Do the work
#

for category in ('negative', 'positive'):
    if not os.path.exists(tst_dst+category):
        os.makedirs(tst_dst+category)
    else:
        shutil.rmtree(tst_dst+category)
        os.makedirs(tst_dst+category)
    files = os.listdir(trn_dir+category)
    np.random.shuffle(files)
    num_samples = int(0.2*len(files))
    tst_files = files[-num_samples:]
    for fname in tst_files:
        shutil.move(trn_dir+category+'/'+fname,
                    tst_dst+category+'/'+fname)