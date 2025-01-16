import cv2

img_src = "day1/example.jpg"

img1 = cv2.imread(img_src, 1)
img2 = cv2.imread(img_src, 0)
img3 = cv2.imread(img_src, -1)

#flag 값
#cv2.IMREAD_COLOR default값 == 1
#cv2.IMREAD_GRAYSCALE 흑백 처리 == 0
#cv2.UNCHANGED == -1

cv2.imshow('Example image1', img1) #title name(여러 창을 띄울때는 이름을 다르게 해야함), 객체
cv2.imshow('Example image2', img2)
cv2.imshow('Example image3', img3)

cv2.waitKey() #입력값이 들어올 떄 까지 대기
cv2.destroyAllWindows() #입력이 돌아오면 종료

