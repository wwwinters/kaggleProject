#! /usr/bin/env python

import os, shutil, kagglehub

tgt_dir = '/home/wiley/regis/archive/msds686/kaggleProject/images/'

bhuvaji_path = kagglehub.dataset_download('sartajbhuvaji/brain-tumor-classification-mri')
buda_path = kagglehub.dataset_download('mateuszbuda/lgg-mri-segmentation')
larxel_path = kagglehub.dataset_download('andrewmvd/brain-tumor-segmentation-in-mri-brats-2015')
yeafi_path = kagglehub.dataset_download('ashfakyeafi/brain-mri-images')

bhuvaji_files = os.listdir(bhuvaji_path)
for file in bhuvaji_files:
    