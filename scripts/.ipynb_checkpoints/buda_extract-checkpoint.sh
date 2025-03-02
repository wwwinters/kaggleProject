#! /usr/bin/env bash

###############################################################################
#
# Title:  		Buda Extract
#
# Purpose:		Copy MRI images from Mateusz Buda's repository to this
#				this project's image directory		
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
# Paths to be used in this script
#
base_dir='/home/wiley/regis/'
src_dir=${base_dir}'archive/msds686/kaggleProject/images/buda/kaggle_3m/'
tgt_dir=${base_dir}'dataScience/kaggleProject/images/data/training/positive/'

#
# Get directory names
#
dirs=`ls -F ${src_dir}| grep '/'`

#
# Do the work
#
for dir in ${dirs};
do
   files=`ls ${src_dir}${dir}|grep -v mask`
   for file in ${files};
   do
      cp ${src_dir}${dir}${file} ${tgt_dir}
	done
done