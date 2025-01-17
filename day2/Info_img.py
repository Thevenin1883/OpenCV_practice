import cv2
img  = cv2.imread("example.jpg")

print(type(img)) #이미지는 배열형태로 저장되어 있다.
print(img)
print(img.ndim) # 출력 3: 가로, 세로, 색 3차원 값 (차원수 확인)
print(img.shape)
print(img.size) # img 사이즈