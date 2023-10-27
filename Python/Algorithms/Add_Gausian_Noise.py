import cv2
import numpy as np
from PIL import Image, ImageFilter
from numpy import sqrt
img = cv2.imread(’filename’)
for fil in [0.01,0.02,0.03,0.04,0.05,0.1,0.15,0.2,0.25]:
mean = 0
var=fil # var means variance
stddev = sqrt(var)
noise = np.zeros(img.shape, np.uint8)
cv2.randn(noise, mean, stddev)
noisy_img = cv2.add(img, noise)
cv2.imwrite(’G-Noise’+str(fil)+’.jpg’, noisy_img)
