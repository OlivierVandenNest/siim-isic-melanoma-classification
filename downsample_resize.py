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
random.seed(10)

os.makedirs(os.path.join(new_train_img_folder_path,'unknown'))

def resize_img(img_name,diagnosis):
	image_loc = os.path.join(train_img_folder_path,img_name+'.jpg')
	image = Image.open(image_loc)
	new_img = image.resize((224,224))
	dest = os.path.join(new_train_img_folder_path,diagnosis)
	if not os.path.exists(dest):
		os.makedirs(dest)
	new_img.save(os.path.join(dest,img_name+'.jpg'))
			  

with open(train_path) as csvfile:
	reader = csv.reader(csvfile)
	nb_unknowns = 0
	with open('downsampled_train_resized.csv', 'w', newline='') as file:
	    writer = csv.writer(file)
		for row in reader:
			diagnosis = row[5]
			if diagnosis == 'unknown':
				nb_unknowns += 1
				nb_unknowns %= 10
				if not nb_unknowns:
					resize_img(row[0],diagnosis)
					writer.writerow(row)
			elif not diagnosis == 'diagnosis':
				resize_img(row[0],diagnosis)
				writer.writerow(row)
			else:
				writer.write(row)
		file.close()
	csvfile.close()