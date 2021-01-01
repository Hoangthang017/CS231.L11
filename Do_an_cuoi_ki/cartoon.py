#--------------------------------------------------------Code 1----------------------------------#

# import cv2 as cv
# import numpy as np
# import sys
# import math

# # Helper Functions

# def auto_canny(image, sigma=0.33):
#     v = np.median(image)

#     lower = int(max(0, (1.0 - sigma) * v))
#     upper = int(min(255, (1.0 + sigma) * v))
#     edged = cv.Canny(image, lower, upper)
#     return edged

# def Quantize_colors(img, a=24):
#     img = np.floor_divide(img, a)
#     img = img*a
#     img = img.astype(np.uint8)
#     return img

# #Code:

# img = cv.imread('./Test/test_1.jpg')


# # Applying median filtering to remove any salt and pepper noise present
# img = cv.medianBlur(img, 7)

# # Applying the Canny Edge detection
# gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# gray_img = auto_canny(gray_img)

# # Applying Dilation to thicken and smoothen the contours
# kernel = np.ones((2, 2), np.uint8)
# gray_img = cv.dilate(gray_img, kernel, iterations=1)

# # Applying Bilateral filtering to obtain Cartooning Effect
# for i in range(14):
#     img = cv.bilateralFilter(img, 9, 17, 17)

# # Quantizing colors to enhance the cartooning Effect
# img = Quantize_colors(img)

# # Merging the edges and the original image
# img[gray_img==255] = [0, 0, 0]

# # Cartoonized image
# cv.imwrite('cartoonized_.jpg', img)

# cv.destroyAllWindows()




#--------------------------Code 2-----------------------------------------------#
import numpy as np
import matplotlib.pyplot as plt

import cv2

ddepth = cv2.CV_8U
kernel_size = 300
img = cv2.imread('./Test/test_1.jpg')

img = np.asarray(img,np.uint8)

grayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


median = cv2.medianBlur(grayImage,7) 

 
Laplaced = cv2.Laplacian(median, ddepth, kernel_size)

ret,thresh = cv2.threshold(Laplaced,5,125,cv2.THRESH_BINARY)

thresh =255-thresh
thresh2 = cv2.cvtColor(thresh,cv2.COLOR_GRAY2RGB)

small = cv2.resize(img, (0,0), fx=0.5, fy=0.5) 



painting = cv2.bilateralFilter(small,9,75,75)


painting_resized = cv2.resize(painting, (thresh2.shape[1], thresh2.shape[0]))

dst = cv2.bitwise_and(painting_resized,thresh2)
cv2.imshow('dst',dst)
cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()