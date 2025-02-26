#! /usr/bin/env python

import os, random
from random import sample

tgt_dir = '/home/wiley/regis/dataScience/kaggleProject/images/data/'

files = os.listdir(tgt_dir+'testing/negative/')
for file in sample(files, 1500):
    print('-->Removing: ', tgt_dir+'testing/negative/'+file)
    os.remove(tgt_dir+'/testing/negative/'+file)