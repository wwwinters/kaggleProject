#! /usr/bin/env python

import os, random, shutil
from random import sample

src_dir = '/home/wiley/regis/dataScience/kaggleProject/images/data/training/negative/'
tgt_dir = '/home/wiley/regis/dataScience/kaggleProject/images/data/testing/negative/'

files = os.listdir(src_dir)
for file in sample(files, 600):
    print('-->Copying: ', src_dir+file)
    shutil.copy(src_dir+file, tgt_dir+file)