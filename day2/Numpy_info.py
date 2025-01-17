import cv2
import numpy as np

img = cv2.imread('example.jpg') #직접 R,G,B값을 조작하여 GRAY값으로 교환

if img is None:
    print("이미지를 불러올 수 없습니다. 파일 경로를 확인하세요.")
    exit()

img_dst = img.astype(np.uint16)
b, g, r = cv2.split(img_dst)

gray = ((b + g + r)/3).astype(np.uint8)     

cv2.imshow('image', img)
cv2.imshow('gray', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
