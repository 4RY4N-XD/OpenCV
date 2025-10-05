import os
import cv2
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

base_dir = os.path.dirname(__file__)  # Gets the folder where your script is
image = os.path.join(base_dir, "images", "Apollo_11_Launch.jpg") #to read from os

image = cv2.imread(image, cv2.IMREAD_COLOR)

# -----------------------------------------------------------------------------
# Drawing a line 

#Syntax---------- img = cv2.line(img, pt1, pt2, color[, thickness[, lineType[, shift]]])

imageLine = image.copy()

# The line starts from (200,100) and ends at (400,100)
# The color of the line is YELLOW (Recall that OpenCV uses BGR format)
# Thickness of line is 5px
# Linetype is cv2.LINE_AA

cv2.line(imageLine, (200,100), (400, 100), (0, 255, 255), thickness= 5, lineType= cv2.LINE_AA)
plt.imshow(cv2.cvtColor(imageLine, cv2.COLOR_BGR2RGB))
# plt.show()


# ----------------------------------------------------------------------------------
# Drawing a Circle

#Syntax------------- img = cv2.circle(img, center, radius, color[, thickness[, lineType[, shift]]])

imageCircle = image.copy()

cv2.circle(imageCircle, (900, 500), 100, (0,0,255), thickness= 5, lineType= cv2.LINE_AA)
#if thickness is negative then it will fill up the circle
plt.imshow(imageCircle[:,:,:: -1])
plt.show()


# ----------------------------------------------------------------------------------------
# Drawing a Rectangle

#Syntax------------- img = cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]]

imageRectangle = image.copy()

cv2.rectangle(imageRectangle, (500,100), (700, 600), (255,0,255), thickness= 5, lineType= cv2.LINE_8)
plt.imshow(imageRectangle[:,:,::-1])
# plt.show()

#---------------------------------------------------------------------------------------------
#Adding Text

# Functional syntx
# img = cv2.putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])

# img: The output image that has been annotated.

# The function has 6 required arguments:

# img: Image on which the text has to be written.

# text: Text string to be written.

# org: Bottom-left corner of the text string in the image.

# fontFace: Font type

# fontScale: Font scale factor that is multiplied by the font-specific base size.

# color: Font color

# Other optional arguments that are important for us to know include:

# thickness: Integer specifying the line thickness for the text. Default value is 1.

# lineType: Type of the line. Default value is 8 which stands for an 8-connected line. Usually, cv2.LINE_AA (antialiased or smooth line) is used for the lineType.

imageText = image.copy()
text = "Apollo 11 Saturn V Launch, July 16, 1969"
fontScale = 2.3 #if it got negative value like -1 then it will got upside down
fontFace = cv2.FONT_HERSHEY_PLAIN
fontColor = (0, 255, 0)
fontThickness = 2

cv2.putText(imageText, text, (200, 700), fontFace, fontScale, fontColor, fontThickness, cv2.LINE_AA);

# Display the image
plt.imshow(imageText[:, :, ::-1])
# plt.show()
