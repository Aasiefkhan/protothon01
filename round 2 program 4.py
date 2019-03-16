import cv2 
image = cv2.imread('F:/sea.png')
cv2.imshow('original',image)
dimension = image.shape
print(dimension)
for i in range (0,dimension[0]):
    for j in range (0,dimension[1]):
        image[i][j] = image[i][j][0]*0.34 + image[i][j][1]*0.51 + image[i][j][2]*0.15
cv2.imshow('grayscale',image)
thresh = 75
im_bw = cv2.threshold(image, thresh, 255, cv2.THRESH_BINARY)[1]
cv2.imshow('monochrome',im_bw)
cv2.waitKey(0)
cv2.destroyAllWindows()
