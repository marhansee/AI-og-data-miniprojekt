import cv2
import random
import numpy as np

img = cv2.imread("picture.jpg", cv2.IMREAD_GRAYSCALE)
row , col = img.shape
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
def add_noise(img):
    total_pixels = row*col
    pepper_pixels = int(total_pixels/10)
    salt_pixels = int(total_pixels/10)
    for i in range(pepper_pixels):
        y_coord = random.randint(0,row-1)

        x_coord = random.randint(0,col-1)
        img[y_coord][x_coord]=255
    
    for i in range(salt_pixels):
        y_coord = random.randint(0,row-1)

        x_coord = random.randint(0,col-1) 
        img[y_coord][x_coord]=0
    
    return img
cv2.imwrite('salt-and-pepper-picture.jpg',add_noise(img))
img_noise = cv2.imread('salt-and-pepper-picture.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow("image",img_noise)
cv2.waitKey(0)
cv2.destroyAllWindows()

mask = np.ones([3, 3], dtype=int)
mask = mask / 9
#average filtering
img_new_average = np.zeros([row, col], dtype=np.uint8)

for i in range(1, row-1):
    for j in range(1, col-1):
        temp = (img_noise[i-1, j-1]*mask[0, 0] + img_noise[i-1, j]*mask[0, 1] +
                img_noise[i-1, j+1]*mask[0, 2] + img_noise[i, j-1]*mask[1, 0] +
                img_noise[i, j]*mask[1, 1] + img_noise[i, j+1]*mask[1, 2] +
                img_noise[i+1, j-1]*mask[2, 0] + img_noise[i+1, j]*mask[2, 1] +
                img_noise[i+1, j+1]*mask[2, 2])

        img_new_average[i, j] = temp
cv2.imwrite('blurred_img_average.jpg', img_new_average)
cv2.imshow("Blurred Image_average.jpg", img_new_average)
cv2.waitKey(0)
cv2.destroyAllWindows()

#median filtering

img_new_median = np.zeros([row,col],dtype=np.uint8)

for i in range(1,row-1): 
    for j in range(1, col-1): 
        temp = [img_noise[i-1, j-1], 
               img_noise[i-1, j], 
               img_noise[i-1, j + 1], 
               img_noise[i, j-1], 
               img_noise[i, j], 
               img_noise[i, j + 1], 
               img_noise[i + 1, j-1], 
               img_noise[i + 1, j], 
               img_noise[i + 1, j + 1]] 
          
        temp = sorted(temp) 
        img_new_median[i, j]= temp[4] 

img_new_median = img_new_median.astype(np.uint8)
cv2.imwrite('blurred_image_median.jpg',img_new_median)
cv2.imshow('blurred_image_median.jpg', img_new_median)
cv2.waitKey(0)
cv2.destroyAllWindows()


