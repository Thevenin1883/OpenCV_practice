import cv2

ex_file ="example.mp4"
vfile = cv2.VideoCapture(ex_file)

if vfile.isOpened():
    while True:
        vret, img = vfile.read()
        if vret: # vret값이 들어 오는 동안 
            cv2.imshow(ex_file, img) #이미지를 가져오고 
            cv2.waitKey(25) #프레임 설정 1000 / 25 => 40프레임
        else:
            break
else:
    print ("No video file")

vfile.release()
cv2.destroyAllWindows()