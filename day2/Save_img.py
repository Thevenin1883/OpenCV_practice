import cv2

img_src = "example.jpg"
img_dst = "example_res.jpg"

img = cv2.imread(img_src, cv2.IMREAD_GRAYSCALE)

if img is not None:
    cv2.imshow('image', img)
    cv2.imwrite(img_dst, img)
else:
    print("No img")

cv2.waitKey()
cv2.destroyAllWindows()