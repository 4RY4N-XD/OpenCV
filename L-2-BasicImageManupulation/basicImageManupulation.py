import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
from IPython.display import display
import os

base_dir = os.path.dirname(__file__)  # Gets the folder where your script is
checker_board_img = os.path.join(base_dir, "images", "checkerboard_18x18.png") #to read from os
NZ_boat_img = os.path.join(base_dir, "images", "New_Zealand_Boat.jpg")

#Read image as gray Scale
cb_img = cv2.imread(checker_board_img, 0) #0 to use display in gray, 1 to color, -1 in original

# Check if checkerboard image loaded successfully
if cb_img is None:
    raise FileNotFoundError(f"Could not load checkerboard image at: {checker_board_img}")

#Set color map to gray scale for proper rendering
plt.imshow(cb_img, cmap='gray')
print("Checkerboard shape:", cb_img.shape)
# plt.title("checker_board")
# plt.show()

# ---------------------------------------------------------------------------------------

#Accessing individual pixel

#print first pixel of the first black box
print(cb_img[0,0])

#print first pixel of the right of first black box
print(cb_img[0,6])

# -----------------------------------------------------------------------------------------

#Modifying Image Pixels

cb_img_copy = cb_img.copy()
cb_img_copy[2,2] = 200
cb_img_copy[2,3] = 200
cb_img_copy[3,2] = 200
cb_img_copy[3,3] = 200

#same as above
# cb_img_copy[2:4, 2:4] = 200

plt.imshow(cb_img_copy, cmap= "gray")
print("Modified checkerboard shape:", cb_img_copy.shape)
# plt.title("modified Checker board")
# plt.show()

# ------------------------------------------------------------------------------------------

#Cropping images

img_NZ_bgr = cv2.imread(NZ_boat_img, cv2.IMREAD_COLOR)

# Check if NZ boat image loaded successfully
if img_NZ_bgr is None:
    raise FileNotFoundError(f"Could not load NZ boat image at: {NZ_boat_img}")

img_NZ_rgb = img_NZ_bgr[:,:,::-1]

plt.imshow(img_NZ_rgb)
print("NZ Boat image shape:", img_NZ_rgb.shape)
# plt.title("NZ_boat_pic")
# plt.show()

#--------crop out the middle region of the image-------

cropped_region = img_NZ_rgb[200:400, 300:600]
plt.imshow(cropped_region)
# plt.show()

# -----------------------------------------------------------

# Resizing Images

#Syntax --- dst = resize( src, dsize[, dst[, fx[, fy[, interpolation]]]] )

# Method-1: Specifying Scaling Factor using fx and fy

resized_cropped_region_2x = cv2.resize(cropped_region, None, fx= 2, fy = 2)
plt.imshow(resized_cropped_region_2x)
# plt.show()

# Method-2: Specifying exact size of the output image

desired_width = 100
desired_height = 200
dim = (desired_width, desired_height)

resized_cropped_region = cv2.resize(cropped_region, dsize= dim, interpolation= cv2.INTER_AREA) #default interpolation = cv2.INTER_LINEAR
plt.imshow(resized_cropped_region)
# plt.show()

# : Resize while maintaining aspect ratio

desired_width = 100
aspect_ratio = desired_width/cropped_region.shape[1]
desired_height = int(cropped_region.shape[0]*aspect_ratio)
dim = (desired_width, desired_height)

resized_cropped_region = cv2.resize(cropped_region, dsize= dim, interpolation= cv2.INTER_AREA)
plt.imshow(resized_cropped_region)
# plt.show()

# # Actually show the (cropped) resized image (saving it)

# Create output folder and save image there
output_dir = os.path.join(base_dir, "output")
os.makedirs(output_dir, exist_ok=True)

resized_cropped_region_2x_bgr = resized_cropped_region_2x[:,:,::-1] #Swap channel since we reading it with cv and it using BGR while in plt RGB is used
save_path = os.path.join(output_dir, "resized_cropped_region_2x.png")
cv2.imwrite(save_path, resized_cropped_region_2x_bgr) #Save resized image to disk

img = Image.open(save_path)
img.show()

#-----------------------------------------------------------------------------------

#Flipping Images

#Syntax ---- dst = cv.flip( src, flipCode )

img_NZ_rgb_flipped_horz = cv2.flip(img_NZ_rgb, 1)
img_NZ_rgb_flipped_vert = cv2.flip(img_NZ_rgb, 0)
img_NZ_rgb_flipped_both = cv2.flip(img_NZ_rgb, -1)

# Show the images
plt.figure(figsize=(18, 5))  #It will create a 18 inch wide and 5 inch height figure to store all 4 images, 4.5 inch of each, figsize measure in inches not in pixel
plt.subplot(141);plt.imshow(img_NZ_rgb_flipped_horz);plt.title("Horizontal Flip")
plt.subplot(142);plt.imshow(img_NZ_rgb_flipped_vert);plt.title("Vertical Flip")
plt.subplot(143);plt.imshow(img_NZ_rgb_flipped_both);plt.title("Both Flipped")
plt.subplot(144);plt.imshow(img_NZ_rgb);plt.title("Original")

# plt.show()