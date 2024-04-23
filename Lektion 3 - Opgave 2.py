import cv2
import numpy as np  

img = cv2.imread("picture.jpg", cv2.IMREAD_GRAYSCALE)
row, col = img.shape
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

mean = 0 
std = 50

gaussian_noise = np.random.normal(mean,std,img.shape)

img_noised = img + gaussian_noise

img_noised = np.clip(img_noised, 0, 255).astype(np.uint8)

cv2.imshow("image",img_noised)
cv2.waitKey(0)
cv2.destroyAllWindows

mask = np.ones([3, 3], dtype=int)
mask = mask / 9
#average filtering
img_new_average = np.zeros([row, col], dtype=np.uint8)

for i in range(1, row-1):
    for j in range(1, col-1):
        temp = (img_noised[i-1, j-1]*mask[0, 0] + img_noised[i-1, j]*mask[0, 1] +
                img_noised[i-1, j+1]*mask[0, 2] + img_noised[i, j-1]*mask[1, 0] +
                img_noised[i, j]*mask[1, 1] + img_noised[i, j+1]*mask[1, 2] +
                img_noised[i+1, j-1]*mask[2, 0] + img_noised[i+1, j]*mask[2, 1] +
                img_noised[i+1, j+1]*mask[2, 2])

        img_new_average[i, j] = temp
cv2.imwrite('blurred_img_average_gauss.jpg', img_new_average)
cv2.imshow("Blurred Image_average_gauss.jpg", img_new_average)
cv2.waitKey(0)
cv2.destroyAllWindows()

#median filtering

img_new_median = np.zeros([row,col],dtype=np.uint8)

for i in range(1,row-1): 
    for j in range(1, col-1): 
        temp = [img_noised[i-1, j-1], 
               img_noised[i-1, j], 
               img_noised[i-1, j + 1], 
               img_noised[i, j-1], 
               img_noised[i, j], 
               img_noised[i, j + 1], 
               img_noised[i + 1, j-1], 
               img_noised[i + 1, j], 
               img_noised[i + 1, j + 1]] 
          
        temp = sorted(temp) 
        img_new_median[i, j]= temp[4] 

img_new_median = img_new_median.astype(np.uint8)
cv2.imwrite('blurred_image_median_guass.jpg',img_new_median)
cv2.imshow('blurred_image_median_gauss.jpg', img_new_median)
cv2.waitKey(0)
cv2.destroyAllWindows()