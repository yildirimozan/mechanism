import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('logo.png')

cv2.imshow("original image",img)

dimension = img.shape

print("dimension of image: %d columns x  %d rows" %(dimension[0], dimension[1]))

totalnumofelem = img.size

print("Total number of elemnets: %d pixels" %(totalnumofelem))

(b,g,r) = img[50,70]

print("BlueChan: %d GreenChan: %d Red Chan: %d" %(b,g,r))

img_region = img[30:70, 50:90]

cv2.imshow("Region of Org. img",img_region)

img_gray = cv2.imread('logo.png',cv2.IMREAD_GRAYSCALE)

cv2.imshow("Geay Scale. img",img_gray)


# B,G,R = cv2.split(img)

B = img[:, :, 0]
G = img[:, :, 1]
R = img[:, :, 2]


cv2.imshow("Blue Channel",B)

img_4_matplotlib = cv2.merge([R,G,B])

plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(img_4_matplotlib)
plt.show()


cv2.waitKey(0)