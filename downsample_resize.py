# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 22:52:23 2020

@author: olivier Van den Nest
"""

import os
import csv
import shutil
import random
import numpy as np
from PIL import Image

train_path = './train.csv'
train_img_folder_path = 'INSERT YOUR PATH HERE'
new_train_img_folder_path = 'downsampled_train_resized'

def resize_img(row):
	image_loc = os.path.join(train_img_folder_path,row[0]+'.jpg')
	image = Image.open(image_loc)
	new_img = image.resize((224,224))
	new_img.save(os.path.join(new_train_img_folder_path,row[0]+'.jpg'))
			  

with open(train_path) as csvfile:
	reader = csv.reader(csvfile)
	nb_unknowns = 0
	for row in reader:
		if row[5] == 'unknown':
			nb_unknowns += 1
			nb_unknowns %= 10
			if not nb_unknowns:
				resize_img(row)
		elif not row[5] == 'diagnosis':
			resize_img(row)			
	csvfile.close()