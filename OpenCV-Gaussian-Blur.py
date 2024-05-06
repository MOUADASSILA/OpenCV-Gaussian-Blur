#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 11:40:48 2024

@author: mac
"""

import cv2

new_image_path = "/Users/mac/Downloads/original.png"
new_image_cv2 = cv2.imread(new_image_path)

gaussian_chihaja_image_cv2 = cv2.GaussianBlur(new_image_cv2, (21,21),5)

cv2_gaussian_chihaja_image_path = "cv2_gaussian_chihaja_image.png"
cv2.imwrite(cv2_gaussian_chihaja_image_path, gaussian_chihaja_image_cv2)
cv2_gaussian_chihaja_image_path