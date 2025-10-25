import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Image

#---------------------Addition or Brightness---------------------------

base_dir = os.path.dirname(__file__)  # Gets the folder where your script is
image_bgr = os.path.join(base_dir, "images", "New_Zealand_Coast.jpg") #to read from os

image_bgr = cv2.imread(image_bgr, cv2.IMREAD_COLOR)
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

# plt.imshow(image_rgb)
# plt.title("New Zealand Coast")
# plt.axis('off')
# plt.show()

matrix = np.ones(image_rgb.shape, dtype="uint8")*50

img_rgb_brighter = cv2.add(image_rgb, matrix)
img_rgb_darker = cv2.subtract(image_rgb, matrix)

plt.figure(figsize=[18,5]) #18 inches width and 5 inches height
plt.subplot(131); plt.imshow(img_rgb_darker); plt.title("Darker");
plt.subplot(132); plt.imshow(image_rgb); plt.title("Original");
plt.subplot(133); plt.imshow(img_rgb_brighter); plt.title("Brighter");

# plt.show()

#---------------Multiplication or Contrast-------------------------

matrix1 = np.ones(image_rgb.shape) * 0.8
matrix2 = np.ones(image_rgb.shape) * 1.2

img_rgb_lower = np.uint8(cv2.multiply(np.float64(image_rgb), matrix1))
img_rgb_higher = np.uint8(cv2.multiply(np.float64(image_rgb), matrix2))

#show image

plt.figure(figsize= [18, 5])
plt.subplot(131); plt.imshow(img_rgb_lower); plt.title("Lower Contrast")
plt.subplot(132); plt.imshow(image_rgb); plt.title("Original")
plt.subplot(133); plt.imshow(img_rgb_higher); plt.title("Higher contrast")

# plt.show()

#---------------Image Thresholding----------------------

#----syntax----
# retval, dst = cv2.threshold( src, thresh, maxval, type[, dst] )
# dst = cv.adaptiveThreshold( src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst] 

image_windows = os.path.join(base_dir, "images", "building-windows.jpg") #to read from os
image_windows = cv2.imread(image_windows, cv2.IMREAD_GRAYSCALE)

retval, img_thresh = cv2.threshold(image_windows, 100, 255, cv2.THRESH_BINARY)

plt.figure(figsize= [18, 5])

plt.subplot(121); plt.imshow(image_windows, cmap= "gray"); plt.title("Original")
plt.subplot(122); plt.imshow(img_thresh, cmap= "gray"); plt.title("Thresholded")
# plt.show()

print(img_thresh.shape)

#-------------Application: Sheet Music Reader----------------

img_piano_sheet = os.path.join(base_dir, "images", "Piano_Sheet_Music.png")
img_piano_sheet = cv2.imread(img_piano_sheet, cv2.IMREAD_GRAYSCALE)

#Perform global thresholding
retval, img_thresh_gbl_1 = cv2.threshold(img_piano_sheet, 50, 255, cv2.THRESH_BINARY)

# Perform global thresholding
retval, img_thresh_gbl_2 = cv2.threshold(img_piano_sheet, 130, 255, cv2.THRESH_BINARY)

# Perform adaptive thresholding
img_thresh_adp = cv2.adaptiveThreshold(img_piano_sheet, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 7)

# Show the images
plt.figure(figsize=[18,15])
plt.subplot(221); plt.imshow(img_piano_sheet,        cmap="gray");  plt.title("Original");
plt.subplot(222); plt.imshow(img_thresh_gbl_1,cmap="gray");  plt.title("Thresholded (global: 50)");
plt.subplot(223); plt.imshow(img_thresh_gbl_2,cmap="gray");  plt.title("Thresholded (global: 130)");
plt.subplot(224); plt.imshow(img_thresh_adp,  cmap="gray");  plt.title("Thresholded (adaptive)");

# plt.show()

